import sys
import matplotlib
import numpy as np

from computer import pennes
from draw import draw3d, draw3dдырявое, draw2d
from computer import thermal_conductivity
from ui.main_window import Ui_MainWindow

matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QFrame

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, num=1, width=5, height=4, dpi=100, projection=None, title=None):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#f0f0f0')
        self.ax = fig.add_subplot(111, projection=projection, facecolor='#f0f0f0')
        if title:
            self.ax.set_title(title)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image = 1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title='Геометрия')
        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100,
                                         title=f'Геометрия (слой {self.image})')
        # canvas_geometry.ax.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)

        self.layout_geometry = QVBoxLayout()
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        self.canvas_layer = MplCanvas(self)
        self.toolbar_layer = NavigationToolbar(self.canvas_layer, self)

        self.layout_layer = QVBoxLayout()
        self.layout_layer.addWidget(self.canvas_layer)
        self.layout_layer.addWidget(self.toolbar_layer)

        self.canvas_temperature = MplCanvas(self)
        self.toolbar_temperature = NavigationToolbar(self.canvas_temperature, self)

        self.layout_temperature = QVBoxLayout()
        self.layout_temperature.addWidget(self.canvas_temperature)
        self.layout_temperature.addWidget(self.toolbar_temperature)

        # Create a placeholder widget to hold our toolbar and canvas.
        # widget = QWidget()
        self.ui.widget_geometry.setLayout(self.layout_geometry)
        self.ui.widget_layer.setLayout(self.layout_layer)
        self.ui.widget_temperature.setLayout(self.layout_temperature)
        # self.setCentralWidget(widget)

        self.ui.pushButton_left.clicked.connect(self.__prev)
        self.ui.pushButton_right.clicked.connect(self.__next)
        self.ui.pushButton_start.clicked.connect(self.__start)
        self.ui.pushButton_plot_temp.clicked.connect(self.__plot_temp)


        # draw3d(132, self.canvas_geometry.ax, 'images')
        # draw3dдырявое(132, self.canvas_geometry.ax, 'images')

        draw2d(self.image, self.canvas_geometry.ax, 'images')


        # self.show()

    def __next(self):
        if self.image >= 132:
            return

        self.image += 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar_geometry)
        self.toolbar_geometry.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar_geometry.hide()

        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        draw2d(self.image, self.canvas_geometry.ax, 'images')
        # self.show()

    def __prev(self):
        if self.image <= 1:
            return

        self.image -= 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar_geometry)
        self.toolbar_geometry.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar_geometry.hide()

        # self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        draw2d(self.image, self.canvas_geometry.ax, 'images')
        # draw3dдырявое(132, self.canvas_geometry.ax, 'images')
        # self.show()

    def __start(self):
        T_left = float(self.ui.lineEdit_T_left.text())
        T_right = float(self.ui.lineEdit_T_right.text())
        T_top = float(self.ui.lineEdit_T_top.text())
        T_bottom = float(self.ui.lineEdit_T_bottom.text())
        T_outside = float(self.ui.lineEdit_T_outside.text())

        # Вызов функции с новыми параметрами
        Ts = pennes(
            layer=self.image,
            T_left=T_left,
            T_right=T_right,
            T_top=T_top,
            T_bottom=T_bottom,
            T_outside=T_outside
        )
        # Ts = thermal_conductivity(self.image)
        # Ts = pennes(self.image)

        self.Ts = Ts

        self.layout_layer.removeWidget(self.canvas_layer)
        self.layout_layer.removeWidget(self.toolbar_layer)
        self.toolbar_layer.deleteLater()
        self.canvas_layer.deleteLater()
        self.canvas_layer.hide()
        self.toolbar_layer.hide()

        # self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_layer = MplCanvas(self)  # (self.fig)
        self.layout_layer.addWidget(self.canvas_layer)
        self.toolbar_layer = NavigationToolbar(self.canvas_layer, self)
        self.layout_layer.addWidget(self.toolbar_layer)

        print(Ts.keys())

        # Получаем последний момент времени
        last_time = max(Ts.keys())  # Находим максимальный ключ
        last_temp = np.array(Ts[last_time])  # Берём последний температурный массив

        # temp = self.canvas_layer.ax.imshow(Ts[list(Ts.keys())[-1]])
        img = self.canvas_layer.ax.imshow(last_temp.T, origin='lower')
        self.canvas_layer.figure.colorbar(img, label='Температура (°C)')
        self.canvas_layer.ax.set_title(f'Время: {last_time} с')
        # plt.show()
        # self.ui.widget_layer.show()
        # self.ui.widget_temperature.show()

    def __plot_temp(self):
        try:
            Ts = self.Ts
        except AttributeError:
            print(self.ui.lineEdit_x.text(), self.ui.lineEdit_y.text())
            return

        self.layout_temperature.removeWidget(self.canvas_temperature)
        self.layout_temperature.removeWidget(self.toolbar_temperature)
        self.toolbar_temperature.deleteLater()
        self.canvas_temperature.deleteLater()
        self.canvas_temperature.hide()
        self.toolbar_temperature.hide()

        # self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_temperature = MplCanvas(self)  # (self.fig)
        self.layout_temperature.addWidget(self.canvas_temperature)
        self.toolbar_temperature = NavigationToolbar(self.canvas_temperature, self)
        self.layout_temperature.addWidget(self.toolbar_temperature)

        x = int(self.ui.lineEdit_x.text())
        y = int(self.ui.lineEdit_y.text())

        T = []

        for temps in Ts.values():
            T.append(temps[y][x])

        self.canvas_temperature.ax.plot(Ts.keys(), T)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
