import requests
from tenacity import retry, wait_fixed, stop_after_attempt

class DataFetcher:
    @staticmethod
    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
    def get_country_data_by_code(iso_code):
        url = f"https://restcountries.com/v3.1/alpha/{iso_code}"
        try:
            response = requests.get(url, timeout=10) 
            response.raise_for_status()
            return response.json()[0]
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error al obtener datos del país para {iso_code}: {e}")
            return None

    @staticmethod
    @retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
    def get_world_bank_indicator(iso_code, indicator, years=5):
        url = f"http://api.worldbank.org/v2/country/{iso_code}/indicator/{indicator}?format=json&per_page={years}"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data[1] if len(data) > 1 else []
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error al obtener indicador '{indicator}' para {iso_code}: {e}")
            return []
