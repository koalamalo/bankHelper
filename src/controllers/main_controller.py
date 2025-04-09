from models.data_fetcher import DataFetcher
from models.data_processor import DataProcessor

class MainController:
    def __init__(self):
        self.cache = {}

    def get_country_info(self, iso_code):
        if iso_code in self.cache:
            return self.cache[iso_code]

        country_data = DataFetcher.get_country_data_by_code(iso_code)
        if not country_data:
            print(f"⚠️ No se pudieron obtener datos para {iso_code}.")
            return {}

        # Indicadores que queremos obtener
        indicators = {
            "inflation": "FP.CPI.TOTL.ZG",
            "gdp": "NY.GDP.MKTP.CD",
            "unemployment": "SL.UEM.TOTL.ZS"
        }

        indicator_data = self.get_multiple_indicators(iso_code, indicators)

        # Procesar y resumir todo
        summary = DataProcessor.summarize_country_data(
            country_data,
            inflation=indicator_data.get("inflation"),
            gdp=indicator_data.get("gdp"),
            unemployment=indicator_data.get("unemployment")
        )

        self.cache[iso_code] = summary
        return summary

    def get_multiple_indicators(self, iso_code, indicators: dict):
        result = {}
        for key, wb_code in indicators.items():
            raw_data = DataFetcher.get_world_bank_indicator(iso_code, wb_code, years=1)
            result[key] = raw_data
        return result

    def get_gdp_series(self, iso_code):
        raw_series = DataFetcher.get_world_bank_indicator(iso_code, "NY.GDP.MKTP.CD")
        return DataProcessor.extract_indicator_series(raw_series)

