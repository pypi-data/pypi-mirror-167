"""
Scrape all the norwegian Bibles on https://www.bible.com/no/bible/
 and return them in a Logos https://www.logos.com/ compatible format
"""

# bibelen: Scrape norwegian Bibles on Youversion website and generate
# a Logos compatible format
#
# Copyright (C) 2022 Paul Mairo <github@rmpr.xyz>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from bs4 import BeautifulSoup
from tqdm.contrib.concurrent import process_map
from dataclasses import dataclass, field
import re
import requests
import string


@dataclass
class Translation:
    name: str
    code: int
    has_old_testament: bool = True


@dataclass
class _Book:
    name: str
    number_of_chapters: int
    chapters: list[list[str]] = field(default_factory=list)

    def chapter(self, number) -> list[str]:
        if 0 < number <= self.number_of_chapters:
            return self.chapters[number - 1]
        raise RuntimeError(f"Invalid chapter number, {name} only has {no_chapters} chapters")


class Bible:

    def __init__(self, translation: Translation):
        self._base_url = "https://www.bible.com/bible/"
        self._translation = translation
        self.new_testament: list[_Book] = [
            _Book("mat", 28), _Book("MRK", 16), _Book("luk", 24), _Book("JHN", 21),
            _Book("act", 28), _Book("rom", 16), _Book("1co", 16), _Book("2co", 13),
            _Book("gal", 6), _Book("eph", 6), _Book("PHP", 4), _Book("col", 4),
            _Book("1th", 5), _Book("2th", 3), _Book("1ti", 6), _Book("2ti", 4),
            _Book("tit", 3), _Book("phm", 1), _Book("heb", 13), _Book("JAS", 5),
            _Book("1pe", 5), _Book("2pe", 3), _Book("1JN", 5), _Book("2JN", 1),
            _Book("3JN", 1), _Book("jud", 1), _Book("rev", 22),
        ]
        if self._translation.has_old_testament:
            self.old_testament: list[_Book] = [
                _Book("gen", 50), _Book("exo", 40), _Book("lev", 27), _Book("num", 36),
                _Book("deu", 34), _Book("jos", 24), _Book("jdg", 21), _Book("rut", 4),
                _Book("1sa", 31), _Book("2sa", 24), _Book("1ki", 22), _Book("2ki", 25),
                _Book("1ch", 29), _Book("2ch", 36), _Book("ezr", 10), _Book("neh", 13),
                _Book("est", 10), _Book("job", 42), _Book("psa", 150), _Book("pro", 31),
                _Book("ecc", 12), _Book("SNG", 8), _Book("isa", 66), _Book("jer", 52),
                _Book("lam", 5), _Book("EZK", 48), _Book("dan", 12), _Book("hos", 14),
                _Book("JOL", 3), _Book("amo", 9), _Book("oba", 1), _Book("jon", 4),
                _Book("mic", 7), _Book("NAM", 3), _Book("hab", 3), _Book("zep", 3),
                _Book("hag", 2), _Book("zec", 14), _Book("mal", 4),
            ]
        else:
            self.old_testament = []

    @property
    def translation(self) -> int:
        return self._translation

    @translation.setter
    def translation(self, translation: Translation):
        self._translation = translation

    def scrape_book(self, book: _Book) -> tuple[str, list[list[str]]]:
        def _clean_verses(chapter_text: str) -> str:
            cleaned_verses: list = []
            chapter_text_cleaned = chapter_text.replace("\n", "")
            verses = re.split(r"\d+", chapter_text_cleaned)
            for verse in verses:
                clean_verse = verse.strip()
                if clean_verse in f"{string.whitespace}{string.punctuation}":
                    continue
                cleaned_verses.append(clean_verse)
            return cleaned_verses

        chapters: list[list[str]] = []
        for i in range(book.number_of_chapters):
            request = requests.get(
                f"{self._base_url}{self._translation.code}/{book.name}.{i+1}"
            )
            soup = BeautifulSoup(request.text, "html.parser")
            for element in soup.findAll("span", "note"):
                element.decompose()
            chapter_text: str = ""
            for element in soup.findAll("div", "p"):
                chapter_text = f"{chapter_text}{element.get_text()}"
            chapters.append(_clean_verses(chapter_text))
        return chapters

    def scrape_all(self) -> None:
        result = process_map(self.scrape_book, self.new_testament + self.old_testament, desc=f"Fetching {self.translation.name}")
        for i in range(len(self.new_testament)):
            self.new_testament[i].chapters = result[i]
        for i in range(len(self.new_testament), len(result)):
            self.old_testament[i - len(self.new_testament)].chapters = result[i]

    def book(self, number: int) -> _Book:
        if not 0 < number <= 66:
            raise IndexError("Invalid number, remember, the Bible has 66 books")
        if number > 39:
            return self.new_testament[number - 40]
        if number <= 39 and self.translation.has_old_testament:
            return self.old_testament[number - 1]
        raise RuntimeError(f"{self.translation} doesn't have OT")

    def save_to_logos(self) -> None:
        pass
