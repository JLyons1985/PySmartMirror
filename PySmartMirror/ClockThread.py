import time
import datetime
import sys

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread

delay = 500


class ClockThread(MirrorThread):
    sendTimeSignal = pyqtSignal(str)
    sendDateSignal = pyqtSignal(str)
    sendSecondsSignal = pyqtSignal(str)
    sendAmPmSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()

        self.dateText = ""
        self.timeText = ""
        self.secondsText = ""
        self.amPmText = ""
        self.lastDateText = "Ukn"
        self.lastTimeText = "Ukn"
        self.lastSecondsText = "Ukn"
        self.lastAmPmText = "Ukn"

    def run(self):
        try:
            while self.threadRunning:
                self.updateClock()
                self.msleep(delay)
        except:
            e = sys.exc_info()[0]
            print(e)

    def updateClock(self):
        localTimeTemp = time.localtime(time.time())
        localTime = datetime.datetime(localTimeTemp[0], localTimeTemp[1], localTimeTemp[2], localTimeTemp[3],
                                      localTimeTemp[4],
                                      localTimeTemp[5])

        # Date 'Mon Feb 1, 2019'
        self.dateText = localTime.strftime("%a %b %d, %Y")
        if self.dateText != self.lastDateText:
            self.lastDateText = self.dateText
            self.sendDateSignal.emit(self.dateText)

        # Time
        self.timeText = localTime.strftime("%H:%M")
        if self.timeText != self.lastTimeText:
            self.lastTimeText = self.timeText
            self.sendTimeSignal.emit(self.timeText)

        # Seconds
        self.secondsText = localTime.strftime("%S")
        if self.secondsText != self.lastTimeText:
            self.lastSecondsText = self.secondsText
            self.sendSecondsSignal.emit(self.secondsText)

        # Am Pm
        self.amPmText = localTime.strftime("%p")
        if self.amPmText != self.lastAmPmText:
            self.lastAmPmText = self.amPmText
            self.sendAmPmSignal.emit(self.amPmText)
