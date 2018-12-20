from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Calculator(QObject):
    def __init__(self):
        QObject.__init__(self)

    sumResult = pyqtSignal(int, arguments=['sum'])

    subResult = pyqtSignal(int, arguments=['sub'])

    @pyqtSlot(int, int)
    def sum(self, arg1, arg2):
        self.sumResult.emit(arg1 + arg2)

    @pyqtSlot(int, int)
    def sub(self, arg1, arg2):
        self.subResult.emit(arg1 - arg2)


if __name__ == "__main__":
    import sys

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    calculator = Calculator()

    engine.rootContext().setContextProperty("calculator", calculator)

    engine.load("main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
