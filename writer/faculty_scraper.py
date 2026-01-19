from typing import final
from dataclasses import dataclass

import requests

from .constants import FACULTIES_URL
from .utils import removeExtraWhitespaces


@dataclass
class Teacher:
    name: str
    image_url: str


@final
class FacultyScraper:
    def __init__(self):
        response = requests.get(FACULTIES_URL)
        self.data = response.json()

    def get_teachers(self) -> list[Teacher]:
        teachers: list[Teacher] = []
        profiles = self.data["EmployeeProfileLightList"]

        for profile in profiles:
            name: str = profile["CvPersonal"]["Name"]
            name = removeExtraWhitespaces(name).title()

            image_path: str = profile["PersonalOtherInfo"]["SecondProfilePhoto"]
            image_url = "https://www.aiub.edu" + image_path

            teachers.append(Teacher(name, image_url))

        return teachers
