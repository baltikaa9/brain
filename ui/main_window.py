# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1021, 683)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font = QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_temperature = QWidget(self.groupBox_4)
        self.widget_temperature.setObjectName(u"widget_temperature")
        font1 = QFont()
        font1.setPointSize(12)
        self.widget_temperature.setFont(font1)

        self.verticalLayout_3.addWidget(self.widget_temperature)

        self.widget_7 = QWidget(self.groupBox_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.spinBox_x = QSpinBox(self.widget_7)
        self.spinBox_x.setObjectName(u"spinBox_x")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_x.sizePolicy().hasHeightForWidth())
        self.spinBox_x.setSizePolicy(sizePolicy)
        self.spinBox_x.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_x)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.spinBox_y = QSpinBox(self.widget_7)
        self.spinBox_y.setObjectName(u"spinBox_y")
        sizePolicy.setHeightForWidth(self.spinBox_y.sizePolicy().hasHeightForWidth())
        self.spinBox_y.setSizePolicy(sizePolicy)
        self.spinBox_y.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.spinBox_y)

        self.pushButton_plot_temp = QPushButton(self.widget_7)
        self.pushButton_plot_temp.setObjectName(u"pushButton_plot_temp")

        self.horizontalLayout_3.addWidget(self.pushButton_plot_temp)


        self.verticalLayout_3.addWidget(self.widget_7)


        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        self.formLayout_2 = QFormLayout(self.widget_6)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.doubleSpinBox_time = QDoubleSpinBox(self.widget_6)
        self.doubleSpinBox_time.setObjectName(u"doubleSpinBox_time")
        self.doubleSpinBox_time.setMaximum(1000.000000000000000)
        self.doubleSpinBox_time.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.doubleSpinBox_time.setValue(10.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_time)

        self.doubleSpinBox_dx = QDoubleSpinBox(self.widget_6)
        self.doubleSpinBox_dx.setObjectName(u"doubleSpinBox_dx")
        self.doubleSpinBox_dx.setDecimals(3)
        self.doubleSpinBox_dx.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dx.setValue(1.000000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_dx)

        self.doubleSpinBox_dt = QDoubleSpinBox(self.widget_6)
        self.doubleSpinBox_dt.setObjectName(u"doubleSpinBox_dt")
        self.doubleSpinBox_dt.setDecimals(3)
        self.doubleSpinBox_dt.setSingleStep(0.100000000000000)
        self.doubleSpinBox_dt.setValue(0.100000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_dt)


        self.verticalLayout_7.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_buttons = QFrame(self.centralwidget)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(16777215, 300))
        self.frame_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_buttons)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_3 = QPushButton(self.frame_buttons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.lineEdit_data_path = QLineEdit(self.frame_buttons)
        self.lineEdit_data_path.setObjectName(u"lineEdit_data_path")
        self.lineEdit_data_path.setFont(font1)

        self.verticalLayout_5.addWidget(self.lineEdit_data_path)

        self.pushButton_4 = QPushButton(self.frame_buttons)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_start = QPushButton(self.frame_buttons)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setFont(font1)

        self.verticalLayout_5.addWidget(self.pushButton_start)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.frame_buttons, 0, 3, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_geometry = QWidget(self.groupBox_5)
        self.widget_geometry.setObjectName(u"widget_geometry")

        self.verticalLayout_6.addWidget(self.widget_geometry)

        self.widget_2 = QWidget(self.groupBox_5)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_left = QPushButton(self.widget_2)
        self.pushButton_left.setObjectName(u"pushButton_left")

        self.horizontalLayout.addWidget(self.pushButton_left)

        self.pushButton_right = QPushButton(self.widget_2)
        self.pushButton_right.setObjectName(u"pushButton_right")

        self.horizontalLayout.addWidget(self.pushButton_right)


        self.verticalLayout_6.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_layer = QWidget(self.groupBox_3)
        self.widget_layer.setObjectName(u"widget_layer")
        self.widget_layer.setFont(font1)

        self.verticalLayout_2.addWidget(self.widget_layer)


        self.gridLayout.addWidget(self.groupBox_3, 1, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 250))
        self.groupBox_2.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.groupBox_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.formLayout = QFormLayout(self.widget_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_T_outside = QLabel(self.widget_3)
        self.label_T_outside.setObjectName(u"label_T_outside")
        self.label_T_outside.setMinimumSize(QSize(0, 20))
        self.label_T_outside.setFont(font2)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_T_outside)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.doubleSpinBox_lam = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_lam.setObjectName(u"doubleSpinBox_lam")
        self.doubleSpinBox_lam.setDecimals(3)
        self.doubleSpinBox_lam.setMaximum(100.000000000000000)
        self.doubleSpinBox_lam.setSingleStep(0.010000000000000)
        self.doubleSpinBox_lam.setValue(0.251000000000000)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_lam)

        self.doubleSpinBox_c = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_c.setObjectName(u"doubleSpinBox_c")
        self.doubleSpinBox_c.setDecimals(0)
        self.doubleSpinBox_c.setMaximum(10000.000000000000000)
        self.doubleSpinBox_c.setValue(3150.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_c)

        self.doubleSpinBox_rho = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_rho.setObjectName(u"doubleSpinBox_rho")
        self.doubleSpinBox_rho.setDecimals(0)
        self.doubleSpinBox_rho.setMaximum(10000.000000000000000)
        self.doubleSpinBox_rho.setValue(1108.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_rho)

        self.doubleSpinBox_T_init = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_T_init.setObjectName(u"doubleSpinBox_T_init")
        self.doubleSpinBox_T_init.setDecimals(1)
        self.doubleSpinBox_T_init.setMinimum(-100.000000000000000)
        self.doubleSpinBox_T_init.setValue(38.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_T_init)

        self.doubleSpinBox_T_outside = QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_T_outside.setObjectName(u"doubleSpinBox_T_outside")
        self.doubleSpinBox_T_outside.setDecimals(1)
        self.doubleSpinBox_T_outside.setMinimum(-100.000000000000000)
        self.doubleSpinBox_T_outside.setValue(20.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_T_outside)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.pushButton_plot_temp.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043f\u043e \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0443", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.doubleSpinBox_time.setSuffix(QCoreApplication.translate("MainWindow", u"c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0442\u043e\u0447\u0435\u043a", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u044f", None))
        self.pushButton_left.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_right.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0435\u043f\u043b\u043e\u043f\u0440\u043e\u0432\u043e\u0434\u043d\u043e\u0441\u0442\u0438 (k)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043f\u043b\u043e\u0435\u043c\u043a\u043e\u0441\u0442\u044c (c)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0442\u043a\u0430\u043d\u0435\u0439 (\u03c1)", None))
        self.label_T_outside.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u0441\u043d\u0430\u0440\u0443\u0436\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.doubleSpinBox_T_init.setSuffix(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.doubleSpinBox_T_outside.setSuffix(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
    # retranslateUi

