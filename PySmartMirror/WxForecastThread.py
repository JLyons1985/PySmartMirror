import json
import requests
import PySmartMirror.Config as Config
import time
import datetime

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread

delay = 3000000


class WxForecastThread(MirrorThread):
    sendWxForecastForecast = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()

    def run(self):
        try:
            while self.threadRunning:
                self.updateWxForecast()
                self.msleep(delay)
        except Exception as e:
            print(e)

    def updateWxForecast(self):
        weatherConfig = Config.getWeatherConfigData()
        units = weatherConfig["weatherUnits"]
        url = weatherConfig["forecastWeatherUrl"]
        params = dict()
        params["zip"] = weatherConfig["weatherZip"] + "," + weatherConfig["weatherCountry"]
        params["APPID"] = weatherConfig["weatherApiKey"]
        params["units"] = units

        response = requests.get(url, params)
        data = response.json()

        forecasts = data['list']

        forecastReturn = []

        for forecast in forecasts:
            tmpForecast = {}
            forecastDate = datetime.datetime.fromtimestamp(forecast['dt'])
            tmpForecast['day'] = forecastDate.strftime("%A")

            icon = forecast['weather'][0]['icon']
            url = weatherConfig["wxImageUrl"] + icon + "@2x.png"
            tmpForecast['icon'] = url

            tmpForecast['low'] = str(round(forecast['temp']['min']))
            tmpForecast['high'] = str(round(forecast['temp']['max']))
            forecastReturn.append(tmpForecast)

        self.sendWxForecastForecast.emit(json.dumps(forecastReturn))
