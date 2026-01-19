from writer.faculty_scraper import FacultyScraper


def main():
    scraper = FacultyScraper()
    teachers = scraper.get_teachers()
    print(teachers)


if __name__ == "__main__":
    main()
