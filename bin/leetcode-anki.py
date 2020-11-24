#!/usr/bin/env python3

import os
import logging
import genanki  # type: ignore

from typing import List, Set


LEETCODE_DIR = "../l33tcode"
LEETCODE_PROBLEMS_URL = "https://leetcode.com/problems"
GITHUB_SOLUTIONS_URL = "https://github.com/prius/learning/blob/master/l33tcode"
LEETCODE_ANKI_MODEL_ID = 4567610856
LEETCODE_ANKI_DECK_ID = 8589798175
OUTPUT_FILE = "/tmp/leetcode.apkg"
ALLOWED_EXTENSIONS = {".py", ".go"}


logging.getLogger().setLevel(logging.INFO)


class LeetcodeNote(genanki.Note):
    @property
    def guid(self):
        # Hash by leetcode task handle
        return genanki.guid_for(self.fields[2])


def get_leetcode_files() -> List[str]:
    return os.listdir(LEETCODE_DIR)


def get_leetcode_task_handles() -> Set[str]:
    return {
        name
        for name, ext in map(
            lambda f: os.path.splitext(os.path.basename(f)), get_leetcode_files()
        )
        if ext in ALLOWED_EXTENSIONS
    }


def get_leetcode_task_url(task_handle: str) -> str:
    return f"{LEETCODE_PROBLEMS_URL}/{task_handle}/"


def get_github_solution_url_python(task_handle: str) -> str:
    return f"{GITHUB_SOLUTIONS_URL}/{task_handle}.py"


def get_github_solution_url_go(task_handle: str) -> str:
    return f"{GITHUB_SOLUTIONS_URL}/{task_handle}.go"


def generate() -> None:
    leetcode_model = genanki.Model(
        LEETCODE_ANKI_MODEL_ID,
        "Leetcode model",
        fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "LeetcodeHandle"}],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
    )
    leetcode_deck = genanki.Deck(LEETCODE_ANKI_DECK_ID, "leetcode")
    for leetcode_task_handle in get_leetcode_task_handles():
        logging.info(f"Adding {leetcode_task_handle}")
        leetcode_task_url = get_leetcode_task_url(leetcode_task_handle)
        github_solution_url_python = get_github_solution_url_python(
            leetcode_task_handle
        )
        github_solution_url_go = get_github_solution_url_go(leetcode_task_handle)
        leetcode_note = LeetcodeNote(
            model=leetcode_model,
            fields=[
                f"<a href='{leetcode_task_url}'>{leetcode_task_handle}</a>",
                f"""
                <a href='{github_solution_url_python}'>python</a>
                <a href='{github_solution_url_go}'>go</a>
                """,
                leetcode_task_handle,
            ],
        )
        leetcode_deck.add_note(leetcode_note)

    genanki.Package(leetcode_deck).write_to_file(OUTPUT_FILE)


if __name__ == "__main__":
    generate()
