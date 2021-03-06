# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 1920)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: rgb(0, 0, 0);\n"
"QLabel\n"
"{\n"
"    font-family: HelveticaNeue;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browserContainer = QtWidgets.QFrame(self.centralwidget)
        self.browserContainer.setEnabled(False)
        self.browserContainer.setGeometry(QtCore.QRect(220, 684, 640, 360))
        self.browserContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.browserContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.browserContainer.setLineWidth(0)
        self.browserContainer.setObjectName("browserContainer")
        self.notificationLabel = QtWidgets.QLabel(self.centralwidget)
        self.notificationLabel.setEnabled(True)
        self.notificationLabel.setGeometry(QtCore.QRect(0, 905, 1080, 130))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.notificationLabel.setFont(font)
        self.notificationLabel.setStyleSheet("opacity: 0;color: #ffffff")
        self.notificationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.notificationLabel.setWordWrap(True)
        self.notificationLabel.setObjectName("notificationLabel")
        self.mainFourFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFourFrame.setGeometry(QtCore.QRect(0, 0, 1080, 1920))
        self.mainFourFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFourFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFourFrame.setObjectName("mainFourFrame")
        self.dateTimeFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.dateTimeFrame.setGeometry(QtCore.QRect(550, 20, 521, 174))
        self.dateTimeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dateTimeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dateTimeFrame.setObjectName("dateTimeFrame")
        self.dateLabel = QtWidgets.QLabel(self.dateTimeFrame)
        self.dateLabel.setGeometry(QtCore.QRect(18, 0, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(30)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dateLabel.setIndent(0)
        self.dateLabel.setObjectName("dateLabel")
        self.timeAmPmLabel = QtWidgets.QLabel(self.dateTimeFrame)
        self.timeAmPmLabel.setGeometry(QtCore.QRect(476, 100, 46, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.timeAmPmLabel.setFont(font)
        self.timeAmPmLabel.setStyleSheet("color: #ffffff")
        self.timeAmPmLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeAmPmLabel.setObjectName("timeAmPmLabel")
        self.timeLabel = QtWidgets.QLabel(self.dateTimeFrame)
        self.timeLabel.setGeometry(QtCore.QRect(250, 60, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(50)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("color: #ffffff")
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.timeSecondsLabel = QtWidgets.QLabel(self.dateTimeFrame)
        self.timeSecondsLabel.setGeometry(QtCore.QRect(476, 64, 46, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.timeSecondsLabel.setFont(font)
        self.timeSecondsLabel.setStyleSheet("color: #ffffff")
        self.timeSecondsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeSecondsLabel.setObjectName("timeSecondsLabel")
        self.quoteFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.quoteFrame.setGeometry(QtCore.QRect(313, 1682, 759, 230))
        self.quoteFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quoteFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quoteFrame.setObjectName("quoteFrame")
        self.quoteLabel = QtWidgets.QLabel(self.quoteFrame)
        self.quoteLabel.setGeometry(QtCore.QRect(8, 8, 743, 177))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.quoteLabel.setFont(font)
        self.quoteLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.quoteLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.quoteLabel.setIndent(0)
        self.quoteLabel.setObjectName("quoteLabel")
        self.authorLabel = QtWidgets.QLabel(self.quoteFrame)
        self.authorLabel.setGeometry(QtCore.QRect(8, 191, 743, 27))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.authorLabel.setFont(font)
        self.authorLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.authorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.authorLabel.setIndent(0)
        self.authorLabel.setObjectName("authorLabel")
        self.currentWXFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.currentWXFrame.setGeometry(QtCore.QRect(20, 20, 521, 174))
        self.currentWXFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currentWXFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentWXFrame.setObjectName("currentWXFrame")
        self.wxTempLabel = QtWidgets.QLabel(self.currentWXFrame)
        self.wxTempLabel.setGeometry(QtCore.QRect(0, 0, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(48)
        self.wxTempLabel.setFont(font)
        self.wxTempLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.wxTempLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wxTempLabel.setIndent(0)
        self.wxTempLabel.setObjectName("wxTempLabel")
        self.wxLabel = QtWidgets.QLabel(self.currentWXFrame)
        self.wxLabel.setGeometry(QtCore.QRect(0, 70, 481, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.wxLabel.setFont(font)
        self.wxLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.wxLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.wxLabel.setIndent(0)
        self.wxLabel.setObjectName("wxLabel")
        self.windLabel = QtWidgets.QLabel(self.currentWXFrame)
        self.windLabel.setGeometry(QtCore.QRect(0, 120, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.windLabel.setFont(font)
        self.windLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.windLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.windLabel.setIndent(0)
        self.windLabel.setObjectName("windLabel")
        self.currentWxImage = QtWidgets.QLabel(self.currentWXFrame)
        self.currentWxImage.setGeometry(QtCore.QRect(260, 3, 80, 55))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.currentWxImage.setFont(font)
        self.currentWxImage.setObjectName("currentWxImage")
        self.trafficFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.trafficFrame.setGeometry(QtCore.QRect(20, 1682, 287, 221))
        self.trafficFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.trafficFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.trafficFrame.setObjectName("trafficFrame")
        self.trafficArrivalTimeLabel = QtWidgets.QLabel(self.trafficFrame)
        self.trafficArrivalTimeLabel.setGeometry(QtCore.QRect(0, 180, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.trafficArrivalTimeLabel.setFont(font)
        self.trafficArrivalTimeLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.trafficArrivalTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.trafficArrivalTimeLabel.setIndent(0)
        self.trafficArrivalTimeLabel.setObjectName("trafficArrivalTimeLabel")
        self.trafficDepartureTimeLabel = QtWidgets.QLabel(self.trafficFrame)
        self.trafficDepartureTimeLabel.setGeometry(QtCore.QRect(0, 140, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.trafficDepartureTimeLabel.setFont(font)
        self.trafficDepartureTimeLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.trafficDepartureTimeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.trafficDepartureTimeLabel.setIndent(1)
        self.trafficDepartureTimeLabel.setObjectName("trafficDepartureTimeLabel")
        self.trafficDestinationLabel = QtWidgets.QLabel(self.trafficFrame)
        self.trafficDestinationLabel.setGeometry(QtCore.QRect(0, 100, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(22)
        self.trafficDestinationLabel.setFont(font)
        self.trafficDestinationLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.trafficDestinationLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.trafficDestinationLabel.setIndent(0)
        self.trafficDestinationLabel.setObjectName("trafficDestinationLabel")
        self.calendarFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.calendarFrame.setGeometry(QtCore.QRect(781, 190, 290, 420))
        self.calendarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calendarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calendarFrame.setObjectName("calendarFrame")
        self.calendarListView = QtWidgets.QListWidget(self.calendarFrame)
        self.calendarListView.setGeometry(QtCore.QRect(8, 43, 274, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarListView.sizePolicy().hasHeightForWidth())
        self.calendarListView.setSizePolicy(sizePolicy)
        self.calendarListView.setMinimumSize(QtCore.QSize(274, 400))
        self.calendarListView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.calendarListView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.calendarListView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.calendarListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.calendarListView.setAutoScroll(False)
        self.calendarListView.setObjectName("calendarListView")
        self.calendarLabel = QtWidgets.QLabel(self.calendarFrame)
        self.calendarLabel.setGeometry(QtCore.QRect(8, 8, 274, 29))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        self.calendarLabel.setFont(font)
        self.calendarLabel.setStyleSheet("color: #ffffffff")
        self.calendarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.calendarLabel.setObjectName("calendarLabel")
        self.wxForecastFrame = QtWidgets.QFrame(self.mainFourFrame)
        self.wxForecastFrame.setGeometry(QtCore.QRect(20, 190, 425, 420))
        self.wxForecastFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wxForecastFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wxForecastFrame.setObjectName("wxForecastFrame")
        self.dayLabel = QtWidgets.QLabel(self.wxForecastFrame)
        self.dayLabel.setGeometry(QtCore.QRect(8, 8, 120, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayLabel.sizePolicy().hasHeightForWidth())
        self.dayLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        self.dayLabel.setFont(font)
        self.dayLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.dayLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dayLabel.setIndent(0)
        self.dayLabel.setObjectName("dayLabel")
        self.lowLabel = QtWidgets.QLabel(self.wxForecastFrame)
        self.lowLabel.setGeometry(QtCore.QRect(327, 8, 74, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lowLabel.sizePolicy().hasHeightForWidth())
        self.lowLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        self.lowLabel.setFont(font)
        self.lowLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.lowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lowLabel.setIndent(0)
        self.lowLabel.setObjectName("lowLabel")
        self.highLabel = QtWidgets.QLabel(self.wxForecastFrame)
        self.highLabel.setGeometry(QtCore.QRect(240, 8, 74, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highLabel.sizePolicy().hasHeightForWidth())
        self.highLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        self.highLabel.setFont(font)
        self.highLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.highLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.highLabel.setIndent(0)
        self.highLabel.setObjectName("highLabel")
        self.skyImageLabel = QtWidgets.QLabel(self.wxForecastFrame)
        self.skyImageLabel.setGeometry(QtCore.QRect(138, 8, 80, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.skyImageLabel.sizePolicy().hasHeightForWidth())
        self.skyImageLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(20)
        self.skyImageLabel.setFont(font)
        self.skyImageLabel.setStyleSheet("font-pixelsize: 30;\n"
"color: #ffffff")
        self.skyImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skyImageLabel.setIndent(0)
        self.skyImageLabel.setObjectName("skyImageLabel")
        self.wxForecastListView = QtWidgets.QListWidget(self.wxForecastFrame)
        self.wxForecastListView.setGeometry(QtCore.QRect(8, 50, 409, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wxForecastListView.sizePolicy().hasHeightForWidth())
        self.wxForecastListView.setSizePolicy(sizePolicy)
        self.wxForecastListView.setMinimumSize(QtCore.QSize(274, 400))
        self.wxForecastListView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wxForecastListView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.wxForecastListView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wxForecastListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wxForecastListView.setAutoScroll(False)
        self.wxForecastListView.setObjectName("wxForecastListView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Py Smart Mirror"))
        self.notificationLabel.setText(_translate("MainWindow", "TextLabel"))
        self.dateLabel.setText(_translate("MainWindow", "August 12 Mon, 2006"))
        self.timeAmPmLabel.setText(_translate("MainWindow", "AM"))
        self.timeLabel.setText(_translate("MainWindow", "99:99"))
        self.timeSecondsLabel.setText(_translate("MainWindow", "00"))
        self.quoteLabel.setText(_translate("MainWindow", "Quote"))
        self.authorLabel.setText(_translate("MainWindow", "Author"))
        self.wxTempLabel.setText(_translate("MainWindow", "67°C"))
        self.wxLabel.setText(_translate("MainWindow", "Windy"))
        self.windLabel.setText(_translate("MainWindow", "Also windy."))
        self.currentWxImage.setText(_translate("MainWindow", "TextLabel"))
        self.trafficArrivalTimeLabel.setText(_translate("MainWindow", "Arrival Time:"))
        self.trafficDepartureTimeLabel.setText(_translate("MainWindow", "Departure Time:"))
        self.trafficDestinationLabel.setText(_translate("MainWindow", "Destination:"))
        self.calendarLabel.setText(_translate("MainWindow", "Calendar"))
        self.dayLabel.setText(_translate("MainWindow", "Day"))
        self.lowLabel.setText(_translate("MainWindow", "Low"))
        self.highLabel.setText(_translate("MainWindow", "High"))
        self.skyImageLabel.setText(_translate("MainWindow", "Sky"))
