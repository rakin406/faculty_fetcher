from loguru import logger

from writer.gui import FacultyWriterApp


def main():
    _ = logger.add("faculty_fetcher.log")
    app = FacultyWriterApp()
    app.run()


if __name__ == "__main__":
    main()
