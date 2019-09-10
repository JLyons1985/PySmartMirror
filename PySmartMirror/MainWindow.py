import sys
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect, QListWidgetItem
from PyQt5.QtCore import QPropertyAnimation, Qt, QTimer
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase
from PySmartMirror.ClockThread import ClockThread
from PySmartMirror.CurrentWeatherThread import CurrentWeatherThread
from PySmartMirror.QuoteThread import QuoteThread
from PySmartMirror.NotificationThread import NotificationThread
from PySmartMirror.TrafficThread import TrafficThread
from PySmartMirror.CalendarItemWidget import CalendarItemWidget
from PySmartMirror.WxForecastItemWidget import WxForecastItemWidget
from PySmartMirror.WxForecastThread import WxForecastThread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('MainWindowUi.ui', self)
        fontID = QFontDatabase.addApplicationFont("HelveticaNeue.ttf")
        self.isMirrorAwake = False
        self.clockThread = ClockThread()
        self.currentWxThread = CurrentWeatherThread()
        self.forecastWxThread = WxForecastThread()
        self.quoteThread = QuoteThread()
        self.trafficThread = TrafficThread()
        self.notificationThread = NotificationThread()
        self.notificationEffect = QGraphicsOpacityEffect()
        self.notificationAnimation = QPropertyAnimation(self.notificationEffect, b"opacity")
        self.mainFourEffect = QGraphicsOpacityEffect()
        self.notificationLabel.setGraphicsEffect(self.notificationEffect)
        self.mainFourFrame.setGraphicsEffect(self.mainFourEffect)
        self.showMainTimer = QTimer()
        self.notificationEffect.setOpacity(0)
        self.mainFourEffect.setOpacity(0)

        self.connectSignals()

    def keyPressEvent(self, event):
        # Did the user press the Escape key?
        if event.key() == Qt.Key_Escape:  # QtCore.Qt.Key_Escape is a value that equates to what the operating system passes to python from the keyboard when the escape key is pressed.
            # Yes: Close the window
            self.close()
        elif event.key() == Qt.Key_F1:
            if self.isMirrorAwake:
                self.shouldMirrorWake(False)
            else:
                self.shouldMirrorWake(True)
        elif event.key() == Qt.Key_F2:
            item = QListWidgetItem(self.calendarListView)
            item_widget = CalendarItemWidget("Test", "Date", "End", "Start")
            item.setSizeHint(item_widget.size())
            self.calendarListView.addItem(item)
            self.calendarListView.setItemWidget(item, item_widget)


    def connectSignals(self):
        # Notifications
        self.notificationThread.sendNotificationTextSignal.connect(self.setNotificationText)
        self.notificationThread.showNotificationPanelSignal.connect(self.hideShowNotificationPanel)

        # Clock
        self.clockThread.sendDateSignal.connect(self.setDateText)
        self.clockThread.sendTimeSignal.connect(self.setTimeText)
        self.clockThread.sendSecondsSignal.connect(self.setSecondsText)
        self.clockThread.sendAmPmSignal.connect(self.setAmPmText)

        # Current Weather
        self.currentWxThread.sendWxTempSignal.connect(self.setCurrentWxTemp)
        self.currentWxThread.sendWxConditionsSignal.connect(self.setCurrentWxConditions)
        self.currentWxThread.sendWxWindsSignal.connect(self.setCurrentWxWinds)
        self.currentWxThread.sendWxGraphicSignal.connect(self.setCurrentWxImage)

        # Forecast Weather
        self.forecastWxThread.sendWxForecastForecast.connect(self.setWxForecastItems)

        # Quote
        self.quoteThread.sendQuoteQuote.connect(self.setQuoteQuote)
        self.quoteThread.sendQuoteAuthor.connect(self.setAuthorLabel)

        # Traffic
        self.trafficThread.sendDestinationTextSignal.connect(self.setDestinationText)
        self.trafficThread.sendDepartureTimeTextSignal.connect(self.setDepartureTimeText)
        self.trafficThread.sendArrivalTimeTextSignal.connect(self.setArrivalTimeText)

    def startThreads(self):
        # Notifications
        self.notificationThread.setRunning(True)
        self.notificationThread.start()

        # Clock
        self.clockThread.setRunning(True)
        self.clockThread.start()

        # Current Weather
        self.currentWxThread.setRunning(True)
        self.currentWxThread.start()

        # Forecast Weather
        self.forecastWxThread.setRunning(True)
        self.forecastWxThread.start()

        # Quote
        self.quoteThread.setRunning(True)
        self.quoteThread.start()

        # Traffic
        self.trafficThread.setRunning(True)
        self.trafficThread.start()

    def stopThreads(self):
        # Notifications
        # self.notificationThread.setRunning(False)
        # self.notificationThread.quit()

        # Clock
        self.clockThread.setRunning(False)
        self.clockThread.quit()

        # Current Weather
        self.currentWxThread.setRunning(False)
        self.currentWxThread.quit()

        # Forecast Weather
        self.forecastWxThread.setRunning(False)
        self.forecastWxThread.quit()

        # Quote
        self.quoteThread.setRunning(False)
        self.quoteThread.quit()

        # Traffic
        self.trafficThread.setRunning(False)
        self.trafficThread.quit()

    # Slot functions used only by this object
    # Notifications
    def setNotificationText(self, notificationText):
        try:
            self.notificationLabel.setText(notificationText)
        except Exception as e:
            print(e)

    def hideShowNotificationPanel(self, showNotificationPanel):
        try:
            if showNotificationPanel:
                startValue = 0
                endValue = 1
            else:
                startValue = 1
                endValue = 0

            self.notificationLabel.setGraphicsEffect(self.notificationEffect)
            self.notificationAnimation.setDuration(2000)
            self.notificationAnimation.setStartValue(startValue)
            self.notificationAnimation.setEndValue(endValue)
            self.notificationAnimation.start()

        except Exception as e:
            print(e)

    # Clock
    def setDateText(self, dateText):
        self.dateLabel.setText(dateText)

    def setTimeText(self, timeText):
        self.timeLabel.setText(timeText)

    def setSecondsText(self, secondsText):
        self.timeSecondsLabel.setText(secondsText)

    def setAmPmText(self, amPmText):
        self.timeAmPmLabel.setText(amPmText)

    # Current Weather
    def setCurrentWxTemp(self, tempText):
        self.wxTempLabel.setText(tempText)

    def setCurrentWxConditions(self, conditionsText):
        self.wxLabel.setText(conditionsText)

    def setCurrentWxWinds(self, windsText):
        self.windLabel.setText(windsText)

    def setCurrentWxImage(self, wxImage):
        self.currentWxImage.setPixmap(wxImage)

    # Forecast Weather
    def setWxForecastItems(self, forecastJsonStr):
        forecasts = json.loads(forecastJsonStr)

        for forecast in forecasts:
            item = QListWidgetItem(self.wxForecastListView)
            item_widget = WxForecastItemWidget(forecast['day'], forecast['icon'], forecast['high'], forecast['low'])
            item.setSizeHint(item_widget.size())
            self.wxForecastListView.addItem(item)
            self.wxForecastListView.setItemWidget(item, item_widget)


        print(forecasts)

    # Quote
    def setQuoteQuote(self, quote):
        self.quoteLabel.setText(quote)

    def setAuthorLabel(self, author):
        self.authorLabel.setText(author)

    # Traffic
    def setDestinationText(self, destination):
        self.trafficDestinationLabel.setText(destination)

    def setDepartureTimeText(self, departureTime):
        self.trafficDepartureTimeLabel.setText(departureTime)

    def setArrivalTimeText(self, arrivalTime):
        self.trafficArrivalTimeLabel.setText(arrivalTime)

    # Mirror Functions

    def shouldMirrorWake(self, shouldWake):
        self.isMirrorAwake = shouldWake
        if shouldWake:
            self.startThreads()
            self.showMirror()
        else:
            self.stopThreads()
            self.hideMirror()

    def showMirror(self):
        self.notificationThread.showNotification("Welcome back, beautiful!", 5)

        self.showMainTimer.timeout.connect(self.showHideMirrorAfterNotification)
        self.showMainTimer.start(5000)

    def hideMirror(self):
        self.notificationThread.showNotification("Goodbye...", 5)

        self.showMainTimer.timeout.connect(self.showHideMirrorAfterNotification)
        self.showMainTimer.start(5000)

    def showHideMirrorAfterNotification(self):
        try:
            self.showMainTimer.stop()
            if self.isMirrorAwake:
                startValue = 0
                endValue = 1
            else:
                startValue = 1
                endValue = 0

            self.mainFourEffect = QGraphicsOpacityEffect()
            self.mainFourFrame.setGraphicsEffect(self.mainFourEffect)
            self.showHideMirrorAnimation = QPropertyAnimation(self.mainFourEffect, b"opacity")
            self.showHideMirrorAnimation.setDuration(2000)
            self.showHideMirrorAnimation.setStartValue(startValue)
            self.showHideMirrorAnimation.setEndValue(endValue)
            self.showHideMirrorAnimation.start()

        except Exception as e:
            print(e)


app = QApplication(sys.argv)
widget = MainWindow()
widget.show()
sys.exit(app.exec_())
