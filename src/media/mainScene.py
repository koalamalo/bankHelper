import sys
import os
from PySide6.QtWidgets import QMainWindow, QLabel, QFrame, QPushButton, QWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QEvent, QSize
from PySide6.QtGui import QPixmap, QIcon
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
from controllers.controllerMainWindow import banderas as b, dash as d
from ui.main_window import Ui_MainWindow
from controllers.main_controller import MainController

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.controller = MainController()
        
        #Ui
        self.setupUi(self)
        self.setWindowTitle("BankHelper")
        self.setFixedSize(800, 600)
        
        #atributos
        self.current_flag_index = 0
        self.flags = b.flags
        

        #Widgets
        self.mainFrame = self.findChild(QFrame, "mainFrame")
        self.sideBarFrame = self.findChild(QFrame, "sideBarFrame")
        self.mainText = self.findChild(QLabel, 'mainText')
        self.paisText = self.findChild(QLabel, 'paisText')
        self.inflationLabel = self.findChild(QLabel, 'inflationLabel')
        self.pibLabel = self.findChild(QLabel, 'pibLabel')
        self.unemployLabel = self.findChild(QLabel, 'unemployLabel')
        self.flagButton = self.findChild(QPushButton, 'flagButton')
        self.nextFlagButton = self.findChild(QPushButton, 'nextFlagButton')
        self.inicioButton = self.findChild(QPushButton, 'inicioButton')
        self.nosButton = self.findChild(QPushButton, 'nosButton')
        self.configButton = self.findChild(QPushButton, 'configButton')
        self.salirButton = self.findChild(QPushButton, 'salirButton')
        self.dashWidget = self.findChild(QWidget, 'dashWidget')
        self.flagWidget = self.findChild(QWidget, 'flagWidget')
        self.chartWidget = self.findChild(QWidget, 'chartWidget')
        
        #Inicializar botones
        b.flagButtonInit(self.nextFlagButton)
        
        self.set_flag(self.flags[self.current_flag_index])
        self.flagButton.mousePressEvent = self.next_flag
        
        self.salirButton.clicked.connect(self.close)
        
        self.sideBarFrame.installEventFilter(self)
        
        #DebugWidgets
        widgets = [self.mainFrame, self.sideBarFrame, self.flagButton, self.nextFlagButton, self.mainText, self.inicioButton, self.nosButton, self.configButton, self.salirButton, self.dashWidget, self.flagWidget]
        for widget in widgets:
            if not widget:
                print(f"❌ Error: Widget {widget} no encontrado")
                sys.exit(1)
            else:
                print(f"✅ {widget} cargado correctamente")
        
        

    def set_flag(self, flag_data):
        flag_filename = flag_data["filename"]
        flag_path = os.path.join(BASE_DIR, "media", "flags", flag_filename)
        pixmap = QPixmap(flag_path)
        if pixmap.isNull():
            print(f"❌ Error: No se pudo cargar la imagen {flag_path}")
        else:
            desired_size = QSize(80, 60)
            self.flagButton.setIcon(QIcon(pixmap))
            self.flagButton.setIconSize(desired_size)
            self.flagButton.setFixedSize(desired_size.width()+20, desired_size.height()+20)

            
            #centered = self.centered_rect(self.flagWidget, self.flagButton.width(), self.flagButton.height())
            #self.flagButton.setGeometry(centered)
    
    def next_flag(self, event):
        #centered = self.centered_rect(self.flagWidget, self.flagButton.width(), self.flagButton.height())
        #current_geom = centered
        
        current_geom = self.flagButton.geometry()
        w = current_geom.width()
        h = current_geom.height()
        x = current_geom.x()
        y = current_geom.y()

        left_exit = QRect(x - w, y, w, h)
        right_enter = QRect(x + w, y, w, h)
        #left_exit = QRect(centered.x() - centered.width(), centered.y(), centered.width(), centered.height())
        #right_enter = QRect(centered.x() + centered.width(), centered.y(), centered.width(), centered.height())

        self.current_flag_index = (self.current_flag_index + 1) % len(self.flags)
        next_flag = self.flags[self.current_flag_index]
        flag_path = os.path.join(BASE_DIR, "media", "flags", next_flag["filename"])
        pixmap = QPixmap(flag_path)

        self.nextFlagButton.setIcon(QIcon(pixmap))
        self.nextFlagButton.setIconSize(QSize(80, 60))
        self.nextFlagButton.setFixedSize(w, h)
        self.nextFlagButton.setGeometry(right_enter)
        self.nextFlagButton.setVisible(True)

        anim_out = QPropertyAnimation(self.flagButton, b"geometry", self)
        anim_out.setDuration(600)
        anim_out.setStartValue(current_geom)
        anim_out.setEndValue(left_exit)
        anim_out.setEasingCurve(QEasingCurve.OutElastic)
        
        anim_in = QPropertyAnimation(self.nextFlagButton, b"geometry", self)
        anim_in.setDuration(600)
        anim_in.setStartValue(right_enter)
        anim_in.setEndValue(current_geom)
        anim_in.setEasingCurve(QEasingCurve.OutElastic)

        def on_finished():
            self.set_flag(next_flag)
            self.flagButton.setGeometry(current_geom)
            self.nextFlagButton.setVisible(False)
            d.load_country_dashboard(self.controller, self.paisText, self.inflationLabel, self.pibLabel, self.unemployLabel, self.chartWidget, next_flag["iso"])

        anim_in.finished.connect(on_finished)
        anim_out.start()
        anim_in.start()
        
    def expand_sidebar(self):
        anim = QPropertyAnimation(self.sideBarFrame, b"minimumWidth")
        anim.setDuration(300)
        anim.setStartValue(50)
        anim.setEndValue(200)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()
        self.sidebar_anim = anim
        
    def collapse_sidebar(self):
        anim = QPropertyAnimation(self.sideBarFrame, b"minimumWidth")
        anim.setDuration(300)
        anim.setStartValue(200)
        anim.setEndValue(50)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()
        self.sidebar_anim = anim
        
    def eventFilter(self, obj, event):
        if obj == self.sideBarFrame:
            if event.type() == QEvent.Enter:
                self.expand_sidebar()
            elif event.type() == QEvent.Leave:
                self.collapse_sidebar()
        return super().eventFilter(obj, event)
                
                
    """def centered_rect(self, container: QWidget, widget_width: int, widget_height: int) -> QRect:
    c_w = container.width()
    c_h = container.height()
    x = (c_w - widget_width) // 2
    y = (c_h - widget_height) // 2
    return QRect(x, y, widget_width, widget_height)"""