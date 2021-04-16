import math
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ThirdTask(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)

        self.polylabel = [(0, 0), (500, 0), (500, 500), (350, 575), (0, 550)]
        self.targetLength = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Third Task')
        p = self.palette()
        self.setPalette(p)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
        qp.setBrush(QBrush(Qt.SolidPattern))

        self.draw_figures(qp)

        qp.end()

    def draw_figures(self, qp: QPainter):
        for i in range(len(self.polylabel) - 1):
            qp.drawLine(self.polylabel[i][0], self.polylabel[i][1], self.polylabel[i + 1][0], self.polylabel[i + 1][1])
        qp.drawLine(self.polylabel[len(self.polylabel) - 1][0], self.polylabel[len(self.polylabel) - 1][1],
                    self.polylabel[0][0], self.polylabel[0][1])

        self.coord = self.completely_fill_in()
        if self.polylabel[1][0] - self.polylabel[0][0] == self.targetLength:
            qp.drawRect(self.polylabel[0][0], self.polylabel[0][1], self.targetLength, self.targetLength)


    def completely_fill_in(self):
        self.targetLength = self.polylabel[1][0] - self.polylabel[0][0]
        for i in range(1, len(self.polylabel)):
            if self.polylabel[i][0] - self.polylabel[i - 1][0] >= self.targetLength:
                self.targetLength = self.polylabel[i][0]
            elif self.polylabel[i][1] - self.polylabel[i - 1][1] >= self.targetLength:
                self.targetLength = self.polylabel[i][0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ThirdTask()
    sys.exit(app.exec_())
