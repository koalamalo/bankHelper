import sys
import os
from PySide6.QtWidgets import QMainWindow, QLabel, QFrame, QPushButton, QWidget
from PySide6.QtCore import QSize
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
from controllers.controllerMainWindow import banderas as b, dash as d
from ui.main_window import Ui_MainWindow
from controllers.main_controller import MainController
from controllers.controllerAnimator import SidebarAnimator as sa, FlagButtonAnimator as fa

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
        self.iconsize = QSize(80, 60)
        

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
        self.flag_animator = fa(self.flagButton, self.nextFlagButton, self.iconsize)
        self.sidebarAnimator = sa(self.sideBarFrame)
        self.sidebarAnimator.install()
        
        b.set_flag(self.flags[self.current_flag_index], self.flagButton, self.iconsize)
        self.flagButton.clicked.connect(self.next_flag)
        
        self.salirButton.clicked.connect(self.close)
        
        #DebugWidgets
        widgets = [self.mainFrame, self.sideBarFrame, self.flagButton, self.nextFlagButton, self.mainText, self.inicioButton, self.nosButton, self.configButton, self.salirButton, self.dashWidget, self.flagWidget]
        for widget in widgets:
            if not widget:
                print(f"❌ Error: Widget {widget} no encontrado")
                sys.exit(1)
            else:
                print(f"✅ {widget} cargado correctamente")
    
    def next_flag(self):
        self.current_flag_index = (self.current_flag_index + 1) % len(self.flags)
        next_data = self.flags[self.current_flag_index]
        # Ruta al icono
        flag_fp = os.path.join(BASE_DIR, "media", "flags", next_data["filename"])
        # Iniciar animación, y tras ella, recargar el dashboard
        self.flag_animator.animate_to(
            flag_fp,
            on_finished=lambda: d.load_country_dashboard(
                self.controller,
                self.paisText,
                self.inflationLabel,
                self.pibLabel,
                self.unemployLabel,
                self.chartWidget,
                next_data["iso"]
            )
        )