class DataProcessor:
    @staticmethod
    def summarize_country_data(country_data, **indicators):
        summary = {}
        # Nombre del país (sacamos el "common")
        summary["name"] = country_data.get("name", {}).get("common", "N/A")
        
        summary["inflation"] = DataProcessor.extract_latest_value(indicators.get("inflation"))
        summary["gdp"] = DataProcessor.extract_latest_value(indicators.get("gdp"))
        summary["unemployment"] = DataProcessor.extract_latest_value(indicators.get("unemployment"))
        
        summary["population"] = country_data.get("population", "N/A")
        summary["region"] = country_data.get("region", "N/A")
        summary["capital"] = country_data.get("capital", ["N/A"])[0]

        return summary

    @staticmethod
    def extract_latest_value(data):
        if isinstance(data, list):
            valid_entries = [entry for entry in data if entry.get("value") is not None]
            if valid_entries:
                valid_entries.sort(key=lambda x: x.get("date", ""), reverse=True)
                return round(valid_entries[0]["value"], 2)
            return "N/A"
        #Dic con clave Data.
        if isinstance(data, dict) and "data" in data:
            series = data.get("data", {})
            if isinstance(series, dict):
                for year in sorted(series.keys(), reverse=True):
                    value = series.get(year)
                    if isinstance(value, (int, float)):
                        return round(value, 2)
            return "N/A"
        return "N/A"

    @staticmethod
    def extract_indicator_series(indicator_data):
        if not isinstance(indicator_data, list):
            return []
        series = [
            {"year": entry["date"], "value": entry["value"]}
            for entry in indicator_data if entry.get("value") is not None
        ]
        return series[::-1]  # Orden de más antiguo a más reciente
