from PyQt5.QtCore import pyqtSignal, QThread


class MirrorThread(QThread):

    def __init__(self, parent=None):
        QThread.__init__(self)
        self.threadRunning = True

    def __del__(self):
        self.wait()

    def setRunning(self, isRunning):
        self.threadRunning = isRunning
