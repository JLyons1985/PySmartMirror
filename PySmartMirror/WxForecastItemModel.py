from PyQt5.QtCore import QObject


class WxForecastItemModel(QObject):
    def __init__(self, day, icon, high, low):
        self.day = day
        self.icon = icon
        self.high = high
        self.low = low