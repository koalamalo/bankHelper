import os
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QSize, QEvent
from PySide6.QtGui import QIcon, QPixmap

class SidebarAnimator:
    def __init__(self, sidebar_frame, min_width=50, max_width=200, duration=300):
        self.frame = sidebar_frame
        self.min_width = min_width
        self.max_width = max_width
        self.duration = duration

    def expand(self):
        anim = QPropertyAnimation(self.frame, b"minimumWidth", self.frame)
        anim.setDuration(self.duration)
        anim.setStartValue(self.min_width)
        anim.setEndValue(self.max_width)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()
        self._anim = anim  # mantener referencia para que no se recolecte

    def collapse(self):
        anim = QPropertyAnimation(self.frame, b"minimumWidth", self.frame)
        anim.setDuration(self.duration)
        anim.setStartValue(self.max_width)
        anim.setEndValue(self.min_width)
        anim.setEasingCurve(QEasingCurve.InOutQuad)
        anim.start()
        self._anim = anim

    def install(self):
        """Instala el filtro de eventos para expandir/colapsar al entrar/salir."""
        self.frame.installEventFilter(self.frame)  # sólo para mantener la referencia
        # Usaremos una closure para no tener que escribir eventFilter en MainWindow
        orig_filter = self.frame.eventFilter

        def _filter(obj, event):
            if obj is self.frame:
                if event.type() == QEvent.Enter:
                    self.expand()
                elif event.type() == QEvent.Leave:
                    self.collapse()
            return orig_filter(obj, event)

        # Reemplazamos el método en tiempo de ejecución
        self.frame.eventFilter = _filter
        
class FlagButtonAnimator:
    def __init__(self, current_btn, next_btn, icon_size: QSize):

        self.curr = current_btn
        self.next = next_btn
        self.icon_size = icon_size

        self.next.setVisible(False)
        self.next.setFlat(True)
        self.next.setStyleSheet("background: transparent; border: none;")

    def animate_to(self, flag_filepath: str, on_finished=None):

        pixmap = QPixmap(flag_filepath)
        self.next.setIcon(QIcon(pixmap))
        self.next.setIconSize(self.icon_size)

        curr_geom = self.curr.geometry()
        w, h = curr_geom.width(), curr_geom.height()
        left_exit   = QRect(curr_geom.x() - w, curr_geom.y(), w, h)
        right_enter = QRect(curr_geom.x() + w, curr_geom.y(), w, h)

        self.next.setGeometry(right_enter)
        self.next.setFixedSize(w, h)
        self.next.show()

        anim_out = QPropertyAnimation(self.curr, b"geometry", self.curr)
        anim_out.setDuration(600)
        anim_out.setStartValue(curr_geom)
        anim_out.setEndValue(left_exit)
        anim_out.setEasingCurve(QEasingCurve.OutElastic)

        anim_in = QPropertyAnimation(self.next, b"geometry", self.next)
        anim_in.setDuration(600)
        anim_in.setStartValue(right_enter)
        anim_in.setEndValue(curr_geom)
        anim_in.setEasingCurve(QEasingCurve.OutElastic)

        def _on_in_finished():
            self.curr.setIcon(self.next.icon())
            self.curr.setGeometry(curr_geom)
            self.next.hide()
            if on_finished:
                on_finished()

        anim_in.finished.connect(_on_in_finished)

        anim_out.start()
        anim_in.start()

