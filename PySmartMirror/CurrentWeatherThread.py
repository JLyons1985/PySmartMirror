import requests
import PySmartMirror.Config as Config
import PySmartMirror.Utilities as Utilities

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PySmartMirror.MirrorThread import MirrorThread

delay = 3000000


class CurrentWeatherThread(MirrorThread):
    sendWxTempSignal = pyqtSignal(str)
    sendWxConditionsSignal = pyqtSignal(str)
    sendWxWindsSignal = pyqtSignal(str)
    sendWxGraphicSignal = pyqtSignal(QPixmap)

    def __init__(self, parent=None):
        super().__init__()
        self.wxTemp = ""
        self.wxConditions = ""
        self.wxWinds = ""
        self.lastWxTemp = "Ukn"
        self.lastWxConditions = "Ukn"
        self.lastWxWinds = "Ukn"
        self.lastWxGraphicUrl = "Ukn"

    def run(self):
        try:
            while self.threadRunning:
                self.updateCurrentWX()
                self.msleep(delay)
        except Exception as e:
            print(e)

    def updateCurrentWX(self):
        weatherConfig = Config.getWeatherConfigData()
        units = weatherConfig["weatherUnits"]
        url = weatherConfig["currentWeatherUrl"]
        params = dict()
        params["zip"] = weatherConfig["weatherZip"] + "," + weatherConfig["weatherCountry"]
        params["APPID"] = weatherConfig["weatherApiKey"]
        params["units"] = units

        response = requests.get(url, params)
        data = response.json()

        # Temperature
        if units == "imperial":
            tempUnit = "F"
        elif units == "metric":
            tempUnit = "C"
        else:
            tempUnit = "K"

        tempJson = data["main"]
        temp = round(tempJson["temp"])
        self.wxTemp = str(temp) + "°" + tempUnit

        if self.wxTemp != self.lastWxTemp:
            self.lastWxTemp = self.wxTemp
            self.sendWxTempSignal.emit(self.wxTemp)

        # Weather Conditions
        weatherJson = data["weather"][0]
        self.wxConditions = "Weather: " + weatherJson["main"]

        if self.wxConditions != self.lastWxConditions:
            self.lastWxConditions = self.wxConditions
            self.sendWxConditionsSignal.emit(self.wxConditions)

        # Winds
        windJson = data["wind"]
        windSpeed = windJson["speed"]
        windDirection = windJson["deg"]

        if windSpeed > 0:
            self.wxWinds = "Winds: " + str(round(windSpeed)) + " kts" + " from the " + \
                           Utilities.degToCompass(windDirection)
        else:
            self.wxWinds = "Winds: Calm"

        if self.wxWinds != self.lastWxWinds:
            self.lastWxWinds = self.wxWinds
            self.sendWxWindsSignal.emit(self.wxWinds)

        # Wx Graphic
        icon = weatherJson["icon"]
        url = weatherConfig["wxImageUrl"] + icon + "@2x.png"

        if url != self.lastWxGraphicUrl:
            response = requests.get(url)
            imageData = response.content
            wxImage = QPixmap()
            wxImage.loadFromData(imageData)
            self.sendWxGraphicSignal.emit(wxImage)
