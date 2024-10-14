import sys
import matplotlib

from main_window import Ui_MainWindow

matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QFrame

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, num=1, width=5, height=4, dpi=100, projection=None, title=None):
        fig = Figure(figsize=(width, height), dpi=dpi, facecolor='#f0f0f0')
        self.axes = fig.add_subplot(111, projection=projection, facecolor='#f0f0f0')
        if title:
            self.axes.set_title(title)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        canvas_geometry = MplCanvas(self, num=1, width=5, height=4, dpi=100, projection='3d', title='Геометрия')
        # canvas_geometry.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(canvas_geometry, self)

        layout_geometry = QVBoxLayout()
        layout_geometry.addWidget(canvas_geometry)
        layout_geometry.addWidget(toolbar)

        canvas_layer = MplCanvas(self)
        toolbar = NavigationToolbar(canvas_geometry, self)

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
        self.ui.widget_geometry.setLayout(layout_geometry)
        self.ui.widget_layer.setLayout(layout_layer)
        self.ui.widget_temperature.setLayout(layout_temperature)
        # self.setCentralWidget(widget)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()
