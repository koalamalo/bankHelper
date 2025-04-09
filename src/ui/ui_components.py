from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class EconomicChart(QWidget):
    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.add_subplot(111)
        self.ax.set_title(title)
        self.update_chart(data)

    def update_chart(self, data):
        if not data: return
        years = [d["year"] for d in data]
        values = [d["value"] for d in data]
        self.ax.clear()
        self.ax.plot(years, values, marker='o', color="#2E86AB")
        self.ax.set_title(self.ax.get_title())
        self.ax.grid(True)
        self.canvas.draw()
