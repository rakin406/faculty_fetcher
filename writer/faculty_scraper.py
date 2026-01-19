from typing import final
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

from .constants import FACULTIES_URL


@dataclass
class Teacher:
    name: str
    image_url: str


@final
class FacultyScraper:
    def __init__(self):
        page = requests.get(FACULTIES_URL)
        self.soup = BeautifulSoup(page.content, "lxml")

    def get_teachers(self) -> list[Teacher]:
        teachers: list[Teacher] = []
        return teachers
