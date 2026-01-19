from typing import final
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

from .constants import FACULTIES_URL
from .utils import removeExtraWhitespaces


@dataclass
class Teacher:
    name: str
    image_url: str


@final
class FacultyScraper:
    # FIX: Name and image URL does not load. Use selenium instead of requests and bs4.
    def __init__(self):
        page = requests.get(FACULTIES_URL)
        self.soup = BeautifulSoup(page.content, "lxml")
        print(self.soup)

    def get_teachers(self) -> list[Teacher]:
        teachers: list[Teacher] = []
        profiles = self.soup.find_all(
            "img", {":src": "profile.PersonalOtherInfo.SecondProfilePhoto"}
        )

        for profile in profiles:
            name = str(profile.get("alt", "Unknown"))
            name = removeExtraWhitespaces(name).title()

            # TODO: Set backup image.
            image_path = str(profile.get("src"))
            image_url = "https://www.aiub.edu" + image_path

            teachers.append(Teacher(name, image_url))

        return teachers
