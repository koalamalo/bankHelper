from ui.ui_components import EconomicChart as ec
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QEvent

def load_country_dashboard(controller, paisText, inflationLabel, pibLabel, unemployLabel, chartWidget, iso_code):
        country_info = controller.get_country_info(iso_code)
        gdp_data = controller.get_gdp_series(iso_code)

        print("📦 Datos país:", country_info)  # Te ayudará a depurar

        # Mostrar info en los labels
        if country_info:
            name_value = country_info.get("name", {})
            if isinstance(name_value, dict):
                name_value = name_value.get("common", "")
            paisText.setText(name_value)

            inflationLabel.setText(f"{country_info.get('inflation', 'N/A')}%")
            pibLabel.setText(f"${country_info.get('gdp', 'N/A')} USD")
            unemployLabel.setText(f"{country_info.get('unemployment', 'N/A')}%")
        else:
            print(f"⚠️ No hay datos para {iso_code}")

        # Limpiar layout de gráfica previa
        layout = chartWidget.layout()
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
        else:
            from PySide6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout()
            chartWidget.setLayout(layout)

        # Añadir nueva gráfica
        if gdp_data:
            chart = ec("PIB en USD (últimos años)", gdp_data)
            layout.addWidget(chart)
            
