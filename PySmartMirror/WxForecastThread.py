import json
import requests
from PyQt5.QtGui import QPixmap

import PySmartMirror.Config as Config
import time
import datetime

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread
from PySmartMirror.WxForecastItemModel import WxForecastItemModel

delay = 3000000


class WxForecastThread(MirrorThread):
    sendWxForecastForecast = pyqtSignal(object)

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
            forecastDate = datetime.datetime.fromtimestamp(forecast['dt'])

            icon = forecast['weather'][0]['icon']
            url = weatherConfig["wxImageUrl"] + icon + "@2x.png"
            response = requests.get(url)
            imageData = response.content
            wxImage = QPixmap()
            wxImage.loadFromData(imageData)
            forecastReturn.append(WxForecastItemModel(forecastDate.strftime("%A"),
                                                      wxImage, str(round(forecast['temp']['max'])),
                                                      str(round(forecast['temp']['min']))))

        self.sendWxForecastForecast.emit(forecastReturn)
