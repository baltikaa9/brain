import csv
import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from draw import draw2d, draw3d
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog

class Form:
    def __init__(self):

        self._init_root()
        self._create_frame1()
        self._create_frame2()
        self._create_frame3()
        self._create_frame4()
        # self._create_textbox()
        # self._create_buttons()


    def _init_root(self):
        self.root = tk.Tk()
        self.root.wm_title('2D/3D brain')
        self.root.geometry('1920x1080')
        self.root.config()
        self.root.protocol("WM_DELETE_WINDOW", lambda: (self.root.destroy(), plt.close()))

    def _create_frame1(self):
        """Геометрия"""
        self._frame1 = tk.Frame(self.root)
        self._frame1.place(x=0, y=0, relwidth=0.33, relheight=0.5)

        self.fig_geometry = plt.figure(num=1)
        self.ax_geometry = self.fig_geometry.add_subplot(111, projection='3d')
        self._canvas1 = FigureCanvasTkAgg(self.fig_geometry, master=self._frame1)
        self._canvas1.get_tk_widget().place(x=0, rely=0.1, relwidth=1, relheight=0.9)

        self._toolbar = NavigationToolbar2Tk(self._canvas1, self.root)
        self._toolbar.update()

        self.label_geometry = tk.Label(self._frame1, text='Геометрия')
        self.label_geometry.place(relx=0.4, y=10)

    def _create_frame2(self):
        """Начальные условия"""
        self._frame2 = tk.Frame(self.root)
        self._frame2.place(x=0, rely=0.5, relwidth=0.33, relheight=0.5)

        self._create_labels_frame2()
        self._create_textboxes_frame2()

    def _create_frame3(self):
        """Остальные настройки"""
        self._frame3 = tk.Frame(self.root)
        self._frame3.place(relx=0.33, y=0, relwidth=0.33, relheight=1)

        self._create_labels_frame3()
        self._create_textboxes_frame3()
        self._create_buttons_frame3()

    def _create_frame4(self):
        """Визуализация"""
        self._frame4 = tk.Frame(self.root)
        self._frame4.place(relx=0.66, y=0, relwidth=0.34, relheight=1)

        self.fig_visualization = plt.figure(num=2)
        self.ax_layer = self.fig_visualization.add_subplot(211)
        self.ax_temperature = self.fig_visualization.add_subplot(212)
        self._canvas2 = FigureCanvasTkAgg(self.fig_visualization, master=self._frame4)
        self._canvas2.get_tk_widget().place(x=0, rely=0.05, relwidth=1, relheight=0.95)

        self._create_labels_frame4()


    def _create_labels_frame2(self):
        self.label_init_conditions = tk.Label(self._frame2, text='Начальные условия')
        self.label_lambda = tk.Label(self._frame2, text='λ')
        self.label_c = tk.Label(self._frame2, text='c')
        self.label_rho = tk.Label(self._frame2, text='ρ')
        self.label_T0 = tk.Label(self._frame2, text='T0')

        self.label_init_conditions.place(relx=0.4, y=10)
        self.label_lambda.place(relx=0.1, rely=0.2)
        self.label_c.place(relx=0.1, rely=0.4)
        self.label_rho.place(relx=0.1, rely=0.6)
        self.label_T0.place(relx=0.1, rely=0.8)

    def _create_textboxes_frame2(self):
        self.textbox_lambda = ttk.Entry(self._frame2)
        self.textbox_c = ttk.Entry(self._frame2)
        self.textbox_rho = ttk.Entry(self._frame2)
        self.textbox_T0 = ttk.Entry(self._frame2)

        self.textbox_lambda.place(relx=0.2, rely=0.2)
        self.textbox_c.place(relx=0.2, rely=0.4)
        self.textbox_rho.place(relx=0.2, rely=0.6)
        self.textbox_T0.place(relx=0.2, rely=0.8)

    def _create_labels_frame3(self):
        self.label_settings = tk.Label(self._frame3, text='Настройки')
        self.label_boundary_conditions = tk.Label(self._frame3, text='Граничные условия')
        self.label_time = tk.Label(self._frame3, text='Время')
        self.label_h = tk.Label(self._frame3, text='Размер шага')

        self.label_settings.place(relx=0.4, y=10)
        self.label_boundary_conditions.place(relx=0.1, rely=0.1)
        self.label_time.place(relx=0.1, rely=0.2)
        self.label_h.place(relx=0.1, rely=0.3)

    def _create_textboxes_frame3(self):
        self.textbox_boundary = ttk.Entry(self._frame3)
        self.textbox_time = ttk.Entry(self._frame3)
        self.textbox_h = ttk.Entry(self._frame3)

        self.textbox_boundary.place(relx=0.3, rely=0.1)
        self.textbox_time.place(relx=0.3, rely=0.2)
        self.textbox_h.place(relx=0.3, rely=0.3)

    def _create_buttons_frame3(self):
        self.btn_start = ttk.Button(self._frame3, text='Запуск', command=lambda : ...)
        self.btn_start.place(relx=0.4, rely=0.9)

    def _create_labels_frame4(self):
        self.label_visualization = tk.Label(self._frame4, text='Визуализация')
        self.label_visualization.place(relx=0.4, y=10)


    def csv_file(self):
        with open('points.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(('x', 'y', 'z'))
            for i in range(len(self.x)):
                print(i)
                writer.writerow((self.x[i], self.y[i], self.z[i]))

    def load_images(self):
        self.folder_path = filedialog.askdirectory()

    def get_draw2d(self):
        i = int(self.textbox_2d.get())
        # plt.clf()
        draw2d(i, self.fig_geometry, self.folder_path)
        self._canvas1.draw()

    def get_draw3d(self):
        i = int(self.textbox_3d.get())
        # plt.clf()
        self.x, self.y, self.z = draw3d(i, self.fig_geometry, self.folder_path)
        self._canvas1.draw()
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    form = Form()
    form.run()