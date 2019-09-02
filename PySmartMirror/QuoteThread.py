import requests
import PySmartMirror.Config as Config

from PyQt5.QtCore import pyqtSignal
from PySmartMirror.MirrorThread import MirrorThread

delay = 3000000


class QuoteThread(MirrorThread):
    sendQuoteQuote = pyqtSignal(str)
    sendQuoteAuthor = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()

    def run(self):
        try:
            while self.threadRunning:
                self.updateQuote()
                self.msleep(delay)
        except Exception as e:
            print(e)

    def updateQuote(self):
        quoteConfig = weatherConfig = Config.getQuoteConfigData()
        url = quoteConfig["quoteUrl"]
        postData = {'method': 'getQuote', 'format': 'json', 'lang': 'en'}
        response = requests.post(url, postData)
        data = response.json()
        self.sendQuoteQuote.emit(data["quoteText"])
        self.sendQuoteAuthor.emit("~ " + data["quoteAuthor"])

