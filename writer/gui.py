from typing import final
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Faculty Writer")
        self.setFixedSize(QSize(900, 800))

        label = QLabel(self)
        pixmap = QPixmap("/home/rakin/Pictures/rakin.jpeg")
        pixmap = pixmap.scaledToHeight(self.height())
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the central widget of the window
        self.setCentralWidget(label)


@final
class FacultyWriterApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        _ = self.exec()
