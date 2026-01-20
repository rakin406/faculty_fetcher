from typing import final, override
import sys
from pathlib import Path

from PyQt6.QtCore import QSize, Qt, QObject, QRunnable, QThreadPool, pyqtSignal
from PyQt6.QtGui import QPixmap, QKeyEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from psycopg import sql
import requests
from loguru import logger

# Append the parent directory to sys.path
sys.path.append(str(Path(__file__).parent.parent))

from .faculty_scraper import Teacher, FacultyScraper
from db import get_pool, close_pool


@final
class ImageLoaderSignals(QObject):
    result = pyqtSignal(QPixmap)
    error = pyqtSignal(str)


@final
class ImageLoader(QRunnable):
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

        # Get teacher profiles
        scraper = FacultyScraper()
        self.teachers = scraper.get_teachers()
        self.cur_teacher_idx = 0
        self.tracking_keys = True

        # Connect to database
        self.pool = get_pool()
        self.pool.open()

        # Configure window
        self.setWindowTitle("Faculty Writer")
        self.setFixedSize(QSize(900, 800))

        # Set default label
        self.image_label = QLabel("Loading image...")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.image_label)

        # Create threadpool
        self.threadpool = QThreadPool()

        # Create image loader worker
        self.image_loader = None
        self.load_image()

        # Start threadpool
        self.threadpool.start(self.image_loader)

    def __del__(self):
        close_pool()

    def load_image(self):
        self.image_loader = ImageLoader(self.get_cur_image_url())
        self.image_loader.signals.result.connect(self.display_image)
        self.image_loader.signals.error.connect(self.show_error)

    def keyReleaseEvent(self, event):
        if self.tracking_keys and isinstance(event, QKeyEvent):
            key_text = event.text()

            # Write to database.
            # "m" for male, "f" for female
            if key_text == "m":
                self._save_to_db(self.get_cur_teacher(), "male")
            elif key_text == "f":
                self._save_to_db(self.get_cur_teacher(), "female")

            # Go to next image
            if key_text == "m" or key_text == "f":
                self.cur_teacher_idx += 1

                # No more images to show
                if self.cur_teacher_idx >= len(self.teachers):
                    self.tracking_keys = False
                    self.display_end()
                    return

                self.load_image()
                self.threadpool.start(self.image_loader)

    def get_cur_teacher(self) -> Teacher:
        """Get current teacher"""
        return self.teachers[self.cur_teacher_idx]

    def get_cur_image_url(self) -> str:
        """Get current image URL"""
        return self.teachers[self.cur_teacher_idx].image_url

    def display_image(self, pixmap: QPixmap):
        """Display the loaded image"""
        if not pixmap.isNull():
            # Scale image to fit label while maintaining aspect ratio
            scaled_pixmap = pixmap.scaledToHeight(self.height())
            self.image_label.setPixmap(scaled_pixmap)
        else:
            self.image_label.setText("Failed to load image")

    def display_end(self):
        self.image_label.setText("No more images to show")

    def show_error(self, error_msg: str):
        """Display error message"""
        self.image_label.setText(f"Error loading image:\n{error_msg}")

    def _save_to_db(self, teacher: Teacher, gender: str):
        """Save teacher to database"""
        with self.pool.connection() as conn:
            with conn.cursor() as cur:
                query = sql.SQL("INSERT INTO {table} ({fields}) VALUES (%s, %s, %s)").format(
                    table=sql.Identifier('teachers'),
                    fields=sql.SQL(',').join([
                        sql.Identifier('name'),
                        sql.Identifier('gender'),
                        sql.Identifier('photo_url')
                    ]))

                _ = cur.execute(query, (teacher.name, gender, teacher.image_url))
                logger.info("Saved {name} as {gender} to database", name=teacher.name, gender=gender)


@final
class FacultyWriterApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.window = MainWindow()

    def run(self):
        self.window.show()
        _ = self.exec()
