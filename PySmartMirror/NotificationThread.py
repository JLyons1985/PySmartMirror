import requests
import PySmartMirror.Config as Config

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread

delay = 1000


class NotificationThread(MirrorThread):
    sendNotificationTextSignal = pyqtSignal(str)
    showNotificationPanelSignal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__()
        self.isNotificationPanelVisible = False
        self.secondsSinceNotificationCheck = 0
        self.secondsToDisplayText = 0

    def run(self):
        try:
            while self.threadRunning:
                if self.isNotificationPanelVisible:
                    if self.secondsSinceNotificationCheck >= self.secondsToDisplayText:
                        self.hideNotification()
                    else:
                        self.secondsSinceNotificationCheck += 1
                self.msleep(delay)
        except Exception as e:
            print(e)

    def showNotification(self, notificationText, secondsToDisplayText):
        self.secondsToDisplayText = secondsToDisplayText
        self.secondsSinceNotificationCheck = 0
        self.sendNotificationTextSignal.emit(notificationText)
        self.showNotificationPanelSignal.emit(True)
        self.isNotificationPanelVisible = True

    def hideNotification(self):
        self.secondsSinceNotificationCheck = 0
        self.secondsToDisplayText = 0
        self.showNotificationPanelSignal.emit(False)
        self.isNotificationPanelVisible = False
