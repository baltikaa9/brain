import sys
import matplotlib

from draw import draw3d, draw3dдырявое, draw2d
from brain_app import Ui_MainWindow

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
                                         title=f'Геометрия (слой {self.image})', projection='3d')
        # canvas_geometry.ax.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = NavigationToolbar(self.canvas_geometry, self)

        self.layout_geometry = QVBoxLayout()
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.layout_geometry.addWidget(self.toolbar)

        canvas_layer = MplCanvas(self)
        toolbar = NavigationToolbar(self.canvas_geometry, self)

        layout_layer = QVBoxLayout()
        layout_layer.addWidget(canvas_layer)
        layout_layer.addWidget(toolbar)

        canvas_temperature = MplCanvas(self)
        toolbar = NavigationToolbar(canvas_temperature, self)

        layout_temperature = QVBoxLayout()
        layout_temperature.addWidget(canvas_temperature)
        layout_temperature.addWidget(toolbar)

        # Create a placeholder widget to hold our toolbar and canvas.
        # widget = QWidget()
        self.ui.widget_geometry.setLayout(self.layout_geometry)
        self.ui.widget_layer.setLayout(layout_layer)
        self.ui.widget_temperature.setLayout(layout_temperature)
        # self.setCentralWidget(widget)

        self.ui.pushButton.clicked.connect(self.__prev)
        self.ui.pushButton_2.clicked.connect(self.__next)


        draw3d(132, self.canvas_geometry.ax, 'images')
        # draw3dдырявое(132, self.canvas_geometry.ax, 'images')

        # draw2d(self.image, self.canvas_geometry.ax, 'images')


        # self.show()

    def __next(self):
        if self.image >= 132:
            return

        self.image += 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar)
        self.toolbar.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar.hide()

        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar)

        draw2d(self.image, self.canvas_geometry.ax, 'images')
        # self.show()

    def __prev(self):
        if self.image <= 1:
            return

        self.image -= 1
        self.layout_geometry.removeWidget(self.canvas_geometry)
        self.layout_geometry.removeWidget(self.toolbar)
        self.toolbar.deleteLater()
        self.canvas_geometry.deleteLater()
        self.canvas_geometry.hide()
        self.toolbar.hide()

        # self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})')  # (self.fig)
        self.canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, title=f'Геометрия (слой {self.image})', projection='3d')  # (self.fig)
        self.layout_geometry.addWidget(self.canvas_geometry)
        self.toolbar = NavigationToolbar(self.canvas_geometry, self)
        self.layout_geometry.addWidget(self.toolbar)

        draw2d(self.image, self.canvas_geometry.ax, 'images')
        # draw3dдырявое(132, self.canvas_geometry.ax, 'images')
        # self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
