# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarItemUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calendarWidget(object):
    def setupUi(self, calendarWidget):
        calendarWidget.setObjectName("calendarWidget")
        calendarWidget.setWindowModality(QtCore.Qt.NonModal)
        calendarWidget.resize(274, 59)
        calendarWidget.setStyleSheet("background: rgb(0, 0, 0);\n"
"QLabel\n"
"{\n"
"    font-family: HelveticaNeue;\n"
"}")
        self.nameLabel = QtWidgets.QLabel(calendarWidget)
        self.nameLabel.setGeometry(QtCore.QRect(0, 0, 274, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: #ffffffff")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.dateLabel = QtWidgets.QLabel(calendarWidget)
        self.dateLabel.setGeometry(QtCore.QRect(0, 30, 73, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: #ffffffff")
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.startLabel = QtWidgets.QLabel(calendarWidget)
        self.startLabel.setGeometry(QtCore.QRect(121, 30, 53, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.startLabel.setFont(font)
        self.startLabel.setStyleSheet("color: #ffffffff")
        self.startLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startLabel.setObjectName("startLabel")
        self.endLabel = QtWidgets.QLabel(calendarWidget)
        self.endLabel.setGeometry(QtCore.QRect(213, 30, 53, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(16)
        self.endLabel.setFont(font)
        self.endLabel.setStyleSheet("color: #ffffffff")
        self.endLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.endLabel.setObjectName("endLabel")
        self.toLabel = QtWidgets.QLabel(calendarWidget)
        self.toLabel.setGeometry(QtCore.QRect(175, 32, 38, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.toLabel.setFont(font)
        self.toLabel.setStyleSheet("color: #ffffffff")
        self.toLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toLabel.setObjectName("toLabel")
        self.fromLabel = QtWidgets.QLabel(calendarWidget)
        self.fromLabel.setGeometry(QtCore.QRect(70, 32, 44, 20))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        self.fromLabel.setFont(font)
        self.fromLabel.setStyleSheet("color: #ffffffff")
        self.fromLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fromLabel.setObjectName("fromLabel")

        self.retranslateUi(calendarWidget)
        QtCore.QMetaObject.connectSlotsByName(calendarWidget)

    def retranslateUi(self, calendarWidget):
        _translate = QtCore.QCoreApplication.translate
        calendarWidget.setWindowTitle(_translate("calendarWidget", "Calendar Item"))
        self.nameLabel.setText(_translate("calendarWidget", "Item"))
        self.dateLabel.setText(_translate("calendarWidget", "Date"))
        self.startLabel.setText(_translate("calendarWidget", "Date"))
        self.endLabel.setText(_translate("calendarWidget", "Date"))
        self.toLabel.setText(_translate("calendarWidget", "To"))
        self.fromLabel.setText(_translate("calendarWidget", "From"))
