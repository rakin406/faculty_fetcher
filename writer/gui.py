from typing import final, override
import sys

from PyQt6.QtCore import QSize, Qt, QObject, QRunnable, QThreadPool, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import requests

from .faculty_scraper import FacultyScraper


@final
class ImageLoaderSignals(QObject):
    error = pyqtSignal(str)
    result = pyqtSignal(QPixmap)


@final
class ImageLoader(QRunnable):
    image_loaded = pyqtSignal(QPixmap)
    error_occurred = pyqtSignal(str)

    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.signals = ImageLoaderSignals()

    @override
    def run(self):
        try:
            response = requests.get(self.url)
            pixmap = QPixmap()
            _ = pixmap.loadFromData(response.content)
            self.signals.result.emit(pixmap)
        except Exception as e:
            self.signals.error.emit(str(e))


@final
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        scraper = FacultyScraper()
        teachers = scraper.get_teachers()

        self.setWindowTitle("Faculty Writer")
        self.setFixedSize(QSize(900, 800))

        self.image_label = QLabel("Loading image...")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)

        threadpool = QThreadPool()

        image_loader = ImageLoader(teachers[0].image_url)
        image_loader.signals.error.connect(self.show_error)
        image_loader.signals.result.connect(self.display_image)

        threadpool.start(image_loader)

    def display_image(self, pixmap: QPixmap):
        """Display the loaded image"""
        if not pixmap.isNull():
            # Scale image to fit label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaledToHeight(self.height())
            self.image_label.setPixmap(scaled_pixmap)
        else:
            self.image_label.setText("Failed to load image")

    def show_error(self, error_msg: str):
        """Display error message"""
        self.image_label.setText(f"Error loading image:\n{error_msg}")


@final
class FacultyWriterApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        _ = self.exec()
