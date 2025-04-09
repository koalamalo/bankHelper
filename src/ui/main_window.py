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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 884)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sideBarFrame = QFrame(self.centralwidget)
        self.sideBarFrame.setObjectName(u"sideBarFrame")
        self.sideBarFrame.setMinimumSize(QSize(50, 0))
        self.sideBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sideBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.sideBarLayout = QVBoxLayout(self.sideBarFrame)
        self.sideBarLayout.setObjectName(u"sideBarLayout")
        self.inicioButton = QPushButton(self.sideBarFrame)
        self.inicioButton.setObjectName(u"inicioButton")
        font = QFont()
        font.setFamilies([u"URW Gothic"])
        font.setPointSize(18)
        self.inicioButton.setFont(font)

        self.sideBarLayout.addWidget(self.inicioButton)

        self.configButton = QPushButton(self.sideBarFrame)
        self.configButton.setObjectName(u"configButton")
        self.configButton.setFont(font)

        self.sideBarLayout.addWidget(self.configButton)

        self.nosButton = QPushButton(self.sideBarFrame)
        self.nosButton.setObjectName(u"nosButton")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Sans"])
        font1.setPointSize(18)
        self.nosButton.setFont(font1)

        self.sideBarLayout.addWidget(self.nosButton)

        self.flagWidget = QWidget(self.sideBarFrame)
        self.flagWidget.setObjectName(u"flagWidget")
        self.flagButton = QPushButton(self.flagWidget)
        self.flagButton.setObjectName(u"flagButton")
        self.flagButton.setGeometry(QRect(10, 150, 171, 101))
        self.nextFlagButton = QPushButton(self.flagWidget)
        self.nextFlagButton.setObjectName(u"nextFlagButton")
        self.nextFlagButton.setGeometry(QRect(10, 150, 171, 101))
        self.paisText = QLabel(self.flagWidget)
        self.paisText.setObjectName(u"paisText")
        self.paisText.setGeometry(QRect(0, 110, 201, 20))
        self.paisText.setFont(font)
        self.paisText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nextFlagButton.raise_()
        self.flagButton.raise_()
        self.paisText.raise_()

        self.sideBarLayout.addWidget(self.flagWidget)

        self.salirButton = QPushButton(self.sideBarFrame)
        self.salirButton.setObjectName(u"salirButton")
        self.salirButton.setFont(font)

        self.sideBarLayout.addWidget(self.salirButton)

        self.sideBarLayout.setStretch(0, 1)
        self.sideBarLayout.setStretch(1, 1)
        self.sideBarLayout.setStretch(2, 1)
        self.sideBarLayout.setStretch(4, 1)

        self.horizontalLayout.addWidget(self.sideBarFrame)

        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.mainLayout = QVBoxLayout(self.mainFrame)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainText = QLabel(self.mainFrame)
        self.mainText.setObjectName(u"mainText")
        font2 = QFont()
        font2.setFamilies([u"URW Gothic"])
        font2.setPointSize(36)
        font2.setBold(False)
        font2.setItalic(False)
        self.mainText.setFont(font2)

        self.mainLayout.addWidget(self.mainText, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.dashWidget = QWidget(self.mainFrame)
        self.dashWidget.setObjectName(u"dashWidget")
        self.verticalLayout = QVBoxLayout(self.dashWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pibLabel = QLabel(self.dashWidget)
        self.pibLabel.setObjectName(u"pibLabel")
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setPointSize(15)
        self.pibLabel.setFont(font3)

        self.verticalLayout.addWidget(self.pibLabel)

        self.inflationLabel = QLabel(self.dashWidget)
        self.inflationLabel.setObjectName(u"inflationLabel")
        self.inflationLabel.setFont(font3)

        self.verticalLayout.addWidget(self.inflationLabel)

        self.unemployLabel = QLabel(self.dashWidget)
        self.unemployLabel.setObjectName(u"unemployLabel")
        self.unemployLabel.setFont(font3)

        self.verticalLayout.addWidget(self.unemployLabel)

        self.chartWidget = QWidget(self.dashWidget)
        self.chartWidget.setObjectName(u"chartWidget")
        self.verticalLayout_2 = QVBoxLayout(self.chartWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addWidget(self.chartWidget)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 6)

        self.mainLayout.addWidget(self.dashWidget)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 5)

        self.horizontalLayout.addWidget(self.mainFrame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"The Bank Helper", None))
        self.inicioButton.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.configButton.setText(QCoreApplication.translate("MainWindow", u"Configuracion", None))
        self.nosButton.setText(QCoreApplication.translate("MainWindow", u"Nosotros", None))
        self.flagButton.setText("")
        self.nextFlagButton.setText("")
        self.paisText.setText(QCoreApplication.translate("MainWindow", u"Koala", None))
        self.salirButton.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.mainText.setText(QCoreApplication.translate("MainWindow", u"The Bank Helper", None))
        self.pibLabel.setText(QCoreApplication.translate("MainWindow", u"PIB", None))
        self.inflationLabel.setText(QCoreApplication.translate("MainWindow", u"Inflacion", None))
        self.unemployLabel.setText(QCoreApplication.translate("MainWindow", u"Desempleo", None))
    # retranslateUi

