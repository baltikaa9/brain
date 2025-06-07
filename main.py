import csv
import os
import sys

import matplotlib
import numpy as np
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from computer import pennes
from draw import draw2d
from draw import get_points
from draw import open_image
from ui.main_window import Ui_MainWindow

matplotlib.use('Qt5Agg')

font = {
    'size': 16,
}

matplotlib.rc('font', **font)

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, num=1, width=5, height=4, dpi=100, projection=None, title=None):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#f0f0f0')
        self.ax = fig.add_subplot(111, projection=projection, facecolor='#f0f0f0')
        if title:
            self.ax.set_title(title)
        super().__init__(fig)


class MainWindow(QMainWindow):
    DIRECTORY_IS_NOT_SPECIFIED = 'Не выбрана директория'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.image = 1
        self.points = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.canvas_geometry = MplCanvas(self, num=1, width=5)
        self.canvas_geometry.ax.set_xlabel('X', fontsize=16)
        self.canvas_geometry.ax.set_ylabel('Y', fontsize=16)

        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)

        self.layout_geometry = QVBoxLayout()
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        self.canvas_layer = MplCanvas(self, width=5, height=4)
        self.toolbar_layer = NavigationToolbar(self.canvas_layer, self)

        self.layout_layer = QVBoxLayout()
        self.layout_layer.addWidget(self.canvas_layer)
        self.layout_layer.addWidget(self.toolbar_layer)

        self.canvas_temperature = MplCanvas(self, width=5, height=4)
        self.toolbar_temperature = NavigationToolbar(self.canvas_temperature, self)

        self.layout_temperature = QVBoxLayout()
        self.layout_temperature.addWidget(self.canvas_temperature)
        self.layout_temperature.addWidget(self.toolbar_temperature)

        self.ui.widget_geometry.setLayout(self.layout_geometry)
        self.ui.widget_layer.setLayout(self.layout_layer)
        self.ui.widget_temperature.setLayout(self.layout_temperature)

        self.ui.pushButton_left.clicked.connect(self.__prev)
        self.ui.pushButton_right.clicked.connect(self.__next)
        self.ui.pushButton_start.clicked.connect(self.__start)
        self.ui.pushButton_plot_temp.clicked.connect(self.__plot_temp)
        self.ui.pushButton_3.clicked.connect(self.__show_file_dialog)
        self.ui.pushButton_4.clicked.connect(self.__export_csv)

        # draw2d(self.image, self.canvas_geometry.ax, 'images')

    def __next(self):
        if self.image >= 132 or not self.points:
            return

        self.image += 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar_geometry)
        self.toolbar_geometry.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar_geometry.hide()

        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_geometry.ax.set_xlabel('X', fontsize=16)
        self.canvas_geometry.ax.set_ylabel('Y', fontsize=16)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        # draw2d(self.image, self.canvas_geometry.ax, 'images')

        # if not os.path.isdir(self.ui.lineEdit_data_path.text()):
        #     QMessageBox.warning(self, 'Ошибка', self.DIRECTORY_IS_NOT_SPECIFIED)
        #     return

        if self.points:
            draw2d(self.image, self.canvas_geometry.ax, self.points)

    def __prev(self):
        if self.image <= 1 or not self.points:
            return

        self.image -= 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar_geometry)
        self.toolbar_geometry.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar_geometry.hide()

        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_geometry.ax.set_xlabel('X', fontsize=16)
        self.canvas_geometry.ax.set_ylabel('Y', fontsize=16)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        # draw2d(self.image, self.canvas_geometry.ax, 'images')

        # if not os.path.isdir(self.ui.lineEdit_data_path.text()):
        #     QMessageBox.warning(self, 'Ошибка', self.DIRECTORY_IS_NOT_SPECIFIED)
        #     return
        draw2d(self.image, self.canvas_geometry.ax, self.points)

    def __start(self):
        t_max = self.ui.doubleSpinBox_time.value()
        dx = self.ui.doubleSpinBox_dx.value()
        dt = self.ui.doubleSpinBox_dt.value()
        lam = self.ui.doubleSpinBox_lam.value()
        c = self.ui.doubleSpinBox_c.value()
        rho = self.ui.doubleSpinBox_rho.value()
        T_init = self.ui.doubleSpinBox_T_init.value()
        T_outside = self.ui.doubleSpinBox_T_outside.value()

        if not os.path.isdir(self.ui.lineEdit_data_path.text()):
            QMessageBox.warning(self, 'Ошибка', self.DIRECTORY_IS_NOT_SPECIFIED)
            return

        points = get_points(open_image(self.image, self.ui.lineEdit_data_path.text()))

        Ts = pennes(
            points=points,
            T_outside=T_outside,
            t_max=t_max,
            dx=dx,
            dt=dt,
            lam=lam,
            c=c,
            rho=rho,
            T_init=T_init,
        )

        self.Ts = Ts

        self.layout_layer.removeWidget(self.canvas_layer)
        self.layout_layer.removeWidget(self.toolbar_layer)
        self.toolbar_layer.deleteLater()
        self.canvas_layer.deleteLater()
        self.canvas_layer.hide()
        self.toolbar_layer.hide()

        self.canvas_layer = MplCanvas(self)  # (self.fig)
        self.layout_layer.addWidget(self.canvas_layer)
        self.toolbar_layer = NavigationToolbar(self.canvas_layer, self)
        self.layout_layer.addWidget(self.toolbar_layer)

        # print(Ts.keys())

        # Получаем последний момент времени
        last_time = max(Ts.keys())  # Находим максимальный ключ
        last_temp = np.array(Ts[last_time])  # Берём последний температурный массив

        img = self.canvas_layer.ax.imshow(last_temp.T, origin='lower')
        self.canvas_layer.figure.colorbar(img, label='Температура (°C)')
        self.canvas_layer.ax.set_xlabel('X', fontsize=16)
        self.canvas_layer.ax.set_ylabel('Y', fontsize=16)
        self.canvas_layer.ax.set_title(f'Время: {last_time} с')

    def __plot_temp(self):
        try:
            Ts = self.Ts
        except AttributeError:
            print(self.ui.spinBox_x.value(), self.ui.spinBox_y.value())
            return

        self.layout_temperature.removeWidget(self.canvas_temperature)
        self.layout_temperature.removeWidget(self.toolbar_temperature)
        self.toolbar_temperature.deleteLater()
        self.canvas_temperature.deleteLater()
        self.canvas_temperature.hide()
        self.toolbar_temperature.hide()

        self.canvas_temperature = MplCanvas(self)  # (self.fig)
        self.layout_temperature.addWidget(self.canvas_temperature)
        self.toolbar_temperature = NavigationToolbar(self.canvas_temperature, self)
        self.layout_temperature.addWidget(self.toolbar_temperature)

        x = self.ui.spinBox_x.value()
        y = self.ui.spinBox_y.value()

        T = []

        for temps in Ts.values():
            T.append(temps[x][y])

        self.canvas_temperature.ax.plot(Ts.keys(), T)

        self.canvas_temperature.ax.set_xlabel('t', fontsize=16)
        self.canvas_temperature.ax.set_ylabel("T", fontsize=16)

    def __show_file_dialog(self):
        directory = QFileDialog.getExistingDirectory()
        self.ui.lineEdit_data_path.setText(directory)

        try:
            self.points = get_points(open_image(self.image, self.ui.lineEdit_data_path.text()), False)
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Ошибка', str(e))
            return

        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar_geometry)
        self.toolbar_geometry.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar_geometry.hide()

        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100,
                                         title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_geometry.ax.set_xlabel('X', fontsize=16)
        self.canvas_geometry.ax.set_ylabel('Y', fontsize=16)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar_geometry = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar_geometry)

        draw2d(self.image, self.canvas_geometry.ax, self.points)

    def __export_csv(self):
        if not os.path.isdir(directory := self.ui.lineEdit_data_path.text()):
            QMessageBox.warning(self, 'Ошибка', self.DIRECTORY_IS_NOT_SPECIFIED)
            return

        file_path = QFileDialog.getSaveFileName(
            parent=self,
            caption='Select a file',
            dir=os.getcwd(),
            filter='(*.csv)',
        )[0]

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(('x', 'y', 'z'))
            for z in range(1, 133):
                x, y = get_points(open_image(self.image, directory))
                for i in range(len(x)):
                    print(i)
                    writer.writerow((x[i], y[i], z))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
