from typing import final
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


@final
class FacultyWriterApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        _ = self.exec()
