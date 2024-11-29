import sys

from math import cos, pi, sin
from PyQt6.QtCore import Qt, QPointF, QRectF
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtWidgets import QWidget, QApplication
from random import randint as RI


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()

        self.status = 0
        self.cord = (None, None)
        self.flag = False
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 30, 1000, 1000)
        self.setWindowTitle('Супрематизм')

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()
        self.flag = False

    def drawf(self):
        self.flag = True
        self.update()

    def draw_flag(self, qp):
        A = D = R = RI(20, 100)
        r, g, b = RI(0, 255), RI(0, 255), RI(0, 255)

        # Задаем кисть
        qp.setBrush(QColor(r, g, b))

        if self.status == 1:
            qp.drawEllipse(QPointF(self.cord[0], self.cord[1]), R, R)
        if self.status == 2:
            qp.drawRect(QRectF(self.cord[0] - D / 2, self.cord[1] - D / 2, A, A))
        elif self.status == 3:
            x, y = self.cord

            coords = QPolygonF([QPointF(x, y - A),
                                QPointF(x + cos(7 * pi / 6) * A,
                                        y - sin(7 * pi / 6) * A),
                                QPointF(x + cos(11 * pi / 6) * A,
                                        y - sin(11 * pi / 6) * A)])
            self.qp.drawPolygon(coords)
        self.status = 0

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.status = 3
            self.drawf()

    def mouseMoveEvent(self, event):
        self.cord = event.pos().x(), event.pos().y()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.status = 1
            self.drawf()
        elif event.button() == Qt.MouseButton.RightButton:
            self.status = 2
            self.drawf()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
