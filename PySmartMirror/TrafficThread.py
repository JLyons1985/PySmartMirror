import requests
import time
import PySmartMirror.Config as Config

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread

delay = 1000 * 2 * 60


class TrafficThread(MirrorThread):
    sendDestinationTextSignal = pyqtSignal(str)
    sendDepartureTimeTextSignal = pyqtSignal(str)
    sendArrivalTimeTextSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()

    def run(self):
        try:
            while self.threadRunning:
                self.updateTraffic()
                self.msleep(delay)
        except Exception as e:
            print(e)

    def updateTraffic(self):
        trafficConfig = Config.getTrafficConfigData()
        url = trafficConfig["googleDistanceUrl"]
        epoch_time = int(time.time()) + trafficConfig["departureMinutesFromNow"] * 60
        params = dict()
        params["origins"] = trafficConfig["origins"]
        params["destinations"] = trafficConfig["destinations"]
        params["departure_time"] = epoch_time
        params["key"] = trafficConfig["distanceApiKey"]

        response = requests.get(url, params)
        data = response.json()

        arrivalEpoch = epoch_time + data["rows"][0]["elements"][0]["duration_in_traffic"]["value"]

        self.sendDestinationTextSignal.emit("Destination: Work")
        self.sendDepartureTimeTextSignal.emit("Departure Time: " +
                                              time.strftime('%H:%M', time.localtime(epoch_time)))
        self.sendArrivalTimeTextSignal.emit("Arrival Time: " +
                                            time.strftime('%H:%M', time.localtime(arrivalEpoch)))

