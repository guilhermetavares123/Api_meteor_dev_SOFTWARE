import requests

class Previsao:
    def __init__(self, latitude, longitude, timezone="auto"):
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        self.data = None       
        self.daily = None      

    def api_meteor(self):
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={self.latitude}"
            f"&longitude={self.longitude}"
            "&daily=temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,"
            "wind_speed_10m_max,sunrise,sunset,daylight_duration,"
            "sunshine_duration,uv_index_max"
            f"&timezone={self.timezone}"
        )

        response = requests.get(url)
        self.data = response.json()
        self.daily = self.data["daily"]

    def get_day(self, index):
        return {
            "dia": self.daily["time"][index],
            "temp_max": self.daily["temperature_2m_max"][index],
            "temp_min": self.daily["temperature_2m_min"][index],
            "sens_max": self.daily["apparent_temperature_max"][index],
            "sens_min": self.daily["apparent_temperature_min"][index],
            "vento_max": self.daily["wind_speed_10m_max"][index],
            "nascer": self.daily["sunrise"][index],
            "por_sol": self.daily["sunset"][index],
            "uv_max": self.daily["uv_index_max"][index],
        }

    def list_days(self):
        dias = []
        for i in range(len(self.daily["time"])):
            dias.append(self.get_day(i))
        return dias

    def imprimir_dias(self):
        
        for d in self.list_days():
            print(f" Dia: {d['dia']}")
            print(f"Máx: {d['temp_max']}°C | Mín: {d['temp_min']}°C")
            print(f"Sens. Máx: {d['sens_max']}°C")
            print(f"Vento Máx: {d['vento_max']} km/h")
            print(f"Nascer: {d['nascer']}")
            print(f"Pôr do Sol: {d['por_sol']}")
            print(f"UV Máx: {d['uv_max']}")
            print("-" * 40)


Local = Previsao(latitude=-16.49, longitude=-49.16)
Local.api_meteor()
Local.imprimir_dias()
