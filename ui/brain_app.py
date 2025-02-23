# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brain_app.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1000)
        font = QFont()
        font.setFamilies([u"JetBrainsMonoNL NFP"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font: 12pt \"JetBrainsMonoNL NFP\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1921, 991))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_geometry = QWidget(self.layoutWidget)
        self.widget_geometry.setObjectName(u"widget_geometry")

        self.verticalLayout_3.addWidget(self.widget_geometry)

        self.layout_settings = QVBoxLayout()
        self.layout_settings.setObjectName(u"layout_settings")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.layout_settings.addLayout(self.horizontalLayout_9)

        self.label_settings = QLabel(self.layoutWidget)
        self.label_settings.setObjectName(u"label_settings")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_settings.sizePolicy().hasHeightForWidth())
        self.label_settings.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"JetBrainsMonoNL NFP"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_settings.setFont(font1)
        self.label_settings.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16pt;")
        self.label_settings.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_settings.addWidget(self.label_settings)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_time = QLabel(self.layoutWidget)
        self.label_time.setObjectName(u"label_time")

        self.verticalLayout_2.addWidget(self.label_time)

        self.label_hx = QLabel(self.layoutWidget)
        self.label_hx.setObjectName(u"label_hx")

        self.verticalLayout_2.addWidget(self.label_hx)

        self.label_ht = QLabel(self.layoutWidget)
        self.label_ht.setObjectName(u"label_ht")

        self.verticalLayout_2.addWidget(self.label_ht)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_time = QLineEdit(self.layoutWidget)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout.addWidget(self.lineEdit_time)

        self.lineEdit_hx = QLineEdit(self.layoutWidget)
        self.lineEdit_hx.setObjectName(u"lineEdit_hx")
        self.lineEdit_hx.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout.addWidget(self.lineEdit_hx)

        self.lineEdit_ht = QLineEdit(self.layoutWidget)
        self.lineEdit_ht.setObjectName(u"lineEdit_ht")
        self.lineEdit_ht.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout.addWidget(self.lineEdit_ht)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.layout_settings.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.layout_settings)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.layout_init_conds = QVBoxLayout()
        self.layout_init_conds.setObjectName(u"layout_init_conds")
        self.label_init_conds = QLabel(self.layoutWidget)
        self.label_init_conds.setObjectName(u"label_init_conds")
        sizePolicy.setHeightForWidth(self.label_init_conds.sizePolicy().hasHeightForWidth())
        self.label_init_conds.setSizePolicy(sizePolicy)
        self.label_init_conds.setFont(font1)
        self.label_init_conds.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16pt;")
        self.label_init_conds.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_init_conds.addWidget(self.label_init_conds)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_k = QLabel(self.layoutWidget)
        self.label_k.setObjectName(u"label_k")

        self.verticalLayout_4.addWidget(self.label_k)

        self.label_c = QLabel(self.layoutWidget)
        self.label_c.setObjectName(u"label_c")

        self.verticalLayout_4.addWidget(self.label_c)

        self.label_rho = QLabel(self.layoutWidget)
        self.label_rho.setObjectName(u"label_rho")

        self.verticalLayout_4.addWidget(self.label_rho)

        self.label_t0 = QLabel(self.layoutWidget)
        self.label_t0.setObjectName(u"label_t0")

        self.verticalLayout_4.addWidget(self.label_t0)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lineEdit_k = QLineEdit(self.layoutWidget)
        self.lineEdit_k.setObjectName(u"lineEdit_k")
        self.lineEdit_k.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout_5.addWidget(self.lineEdit_k)

        self.lineEdit_c = QLineEdit(self.layoutWidget)
        self.lineEdit_c.setObjectName(u"lineEdit_c")
        self.lineEdit_c.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout_5.addWidget(self.lineEdit_c)

        self.lineEdit_rho = QLineEdit(self.layoutWidget)
        self.lineEdit_rho.setObjectName(u"lineEdit_rho")
        self.lineEdit_rho.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout_5.addWidget(self.lineEdit_rho)

        self.lineEdit_t0 = QLineEdit(self.layoutWidget)
        self.lineEdit_t0.setObjectName(u"lineEdit_t0")
        self.lineEdit_t0.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.verticalLayout_5.addWidget(self.lineEdit_t0)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.layout_init_conds.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addLayout(self.layout_init_conds)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_upload_imgs = QPushButton(self.layoutWidget)
        self.pushButton_upload_imgs.setObjectName(u"pushButton_upload_imgs")
        self.pushButton_upload_imgs.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 0, 0, 30);\n"
"	border: 1px solid rgba(0, 0, 0, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0, 0, 0, 70);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_upload_imgs)

        self.pushButton_export = QPushButton(self.layoutWidget)
        self.pushButton_export.setObjectName(u"pushButton_export")
        self.pushButton_export.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 0, 0, 30);\n"
"	border: 1px solid rgba(0, 0, 0, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0, 0, 0, 70);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_export)

        self.pushButton_run = QPushButton(self.layoutWidget)
        self.pushButton_run.setObjectName(u"pushButton_run")
        self.pushButton_run.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(0, 0, 0, 30);\n"
"	border: 1px solid rgba(0, 0, 0, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(0, 0, 0, 70);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_run)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_vizual = QLabel(self.layoutWidget)
        self.label_vizual.setObjectName(u"label_vizual")
        sizePolicy.setHeightForWidth(self.label_vizual.sizePolicy().hasHeightForWidth())
        self.label_vizual.setSizePolicy(sizePolicy)
        self.label_vizual.setFont(font1)
        self.label_vizual.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16pt;")
        self.label_vizual.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_vizual)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_layer_num = QLabel(self.layoutWidget)
        self.label_layer_num.setObjectName(u"label_layer_num")
        sizePolicy.setHeightForWidth(self.label_layer_num.sizePolicy().hasHeightForWidth())
        self.label_layer_num.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_layer_num)

        self.lineEdit_layer_num = QLineEdit(self.layoutWidget)
        self.lineEdit_layer_num.setObjectName(u"lineEdit_layer_num")
        self.lineEdit_layer_num.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_4.addWidget(self.lineEdit_layer_num)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.widget_layer = QWidget(self.layoutWidget)
        self.widget_layer.setObjectName(u"widget_layer")

        self.verticalLayout_7.addWidget(self.widget_layer)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_x = QLineEdit(self.layoutWidget)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_5.addWidget(self.lineEdit_x)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.lineEdit_y = QLineEdit(self.layoutWidget)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_6.addWidget(self.lineEdit_y)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.lineEdit_z = QLineEdit(self.layoutWidget)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setEnabled(False)
        self.lineEdit_z.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;")

        self.horizontalLayout_7.addWidget(self.lineEdit_z)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.widget_temperature = QWidget(self.layoutWidget)
        self.widget_temperature.setObjectName(u"widget_temperature")

        self.verticalLayout_6.addWidget(self.widget_temperature)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f (\u0441)", None))
        self.label_hx.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043f\u043e \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0443", None))
        self.label_ht.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0430\u0433\u0430 \u043f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.lineEdit_ht.setText("")
        self.label_init_conds.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u043e\u0432\u0438\u044f", None))
        self.label_k.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0442\u0435\u043f\u043b\u043e\u043f\u0440\u043e\u0432\u043e\u0434\u043d\u043e\u0441\u0442\u0438 (k)", None))
        self.label_c.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0435\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043f\u043b\u043e\u0435\u043c\u043a\u043e\u0441\u0442\u044c (c)", None))
        self.label_rho.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0442\u043a\u0430\u043d\u0435\u0439 (\u03c1)", None))
        self.label_t0.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 (T0)", None))
        self.pushButton_upload_imgs.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.pushButton_export.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0442\u043e\u0447\u0435\u043a", None))
        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u043a", None))
        self.label_vizual.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_layer_num.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0441\u043b\u043e\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"z", None))
    # retranslateUi

