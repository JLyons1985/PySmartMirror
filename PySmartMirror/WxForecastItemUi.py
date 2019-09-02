# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WxForecastItemUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WxForecastItem(object):
    def setupUi(self, WxForecastItem):
        WxForecastItem.setObjectName("WxForecastItem")
        WxForecastItem.resize(393, 50)
        WxForecastItem.setStyleSheet("background: rgb(0, 0, 0);\n"
"QLabel\n"
"{\n"
"    font-family: HelveticaNeue;\n"
"}")
        self.dayLebl = QtWidgets.QLabel(WxForecastItem)
        self.dayLebl.setGeometry(QtCore.QRect(0, 0, 120, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.dayLebl.setFont(font)
        self.dayLebl.setStyleSheet("color: #ffffffff")
        self.dayLebl.setAlignment(QtCore.Qt.AlignCenter)
        self.dayLebl.setObjectName("dayLebl")
        self.skyImage = QtWidgets.QLabel(WxForecastItem)
        self.skyImage.setGeometry(QtCore.QRect(130, 0, 80, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.skyImage.setFont(font)
        self.skyImage.setStyleSheet("color: #ffffffff")
        self.skyImage.setText("")
        self.skyImage.setAlignment(QtCore.Qt.AlignCenter)
        self.skyImage.setObjectName("skyImage")
        self.highLabel = QtWidgets.QLabel(WxForecastItem)
        self.highLabel.setGeometry(QtCore.QRect(232, 0, 74, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.highLabel.setFont(font)
        self.highLabel.setStyleSheet("color: #ffffffff")
        self.highLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.highLabel.setObjectName("highLabel")
        self.lowLabel = QtWidgets.QLabel(WxForecastItem)
        self.lowLabel.setGeometry(QtCore.QRect(319, 0, 74, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.lowLabel.setFont(font)
        self.lowLabel.setStyleSheet("color: #ffffffff")
        self.lowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lowLabel.setObjectName("lowLabel")

        self.retranslateUi(WxForecastItem)
        QtCore.QMetaObject.connectSlotsByName(WxForecastItem)

    def retranslateUi(self, WxForecastItem):
        _translate = QtCore.QCoreApplication.translate
        WxForecastItem.setWindowTitle(_translate("WxForecastItem", "Form"))
        self.dayLebl.setText(_translate("WxForecastItem", "Item"))
        self.highLabel.setText(_translate("WxForecastItem", "High"))
        self.lowLabel.setText(_translate("WxForecastItem", "Item"))
