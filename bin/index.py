#!/usr/bin/env python3
import logging
import os
import time
from functools import lru_cache
from typing import List, Set

# https://github.com/prius/python-leetcode
import leetcode  # type: ignore

# Example:
# cookies = {
#     "csrftoken": "xxx",
#     "LEETCODE_SESSION": "yyy",
# }
from cookies import cookies

LEETCODE_DIR = "../l33tcode"
LEETCODE_PROBLEMS_URL = "https://leetcode.com/problems"
GITHUB_SOLUTIONS_URL = "https://github.com/prius/learning/blob/master/l33tcode"
ALLOWED_EXTENSIONS = {".py", ".go"}


logging.getLogger().setLevel(logging.INFO)


@lru_cache(None)
def get_leetcode_api_client() -> leetcode.DefaultApi:
    configuration = leetcode.Configuration()

    configuration.api_key["x-csrftoken"] = cookies["csrftoken"]
    configuration.api_key["csrftoken"] = cookies["csrftoken"]
    configuration.api_key["LEETCODE_SESSION"] = cookies["LEETCODE_SESSION"]
    configuration.api_key["Referer"] = "https://leetcode.com"
    configuration.debug = False
    api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

    return api_instance


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


def get_title(task_handle: str) -> str:
    api_instance = get_leetcode_api_client()

    graphql_request = leetcode.GraphqlQuery(
        query="""
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                  title
              }
            }
        """,
        variables=leetcode.GraphqlQueryVariables(title_slug=task_handle),
        operation_name="getQuestionDetail",
    )

    title = api_instance.graphql_post(body=graphql_request).data["question"]["title"]

    return title


def generate() -> None:
    for leetcode_task_handle in get_leetcode_task_handles():
        time.sleep(1)  # Leetcode API has a rate-limiter

        leetcode_task_url = get_leetcode_task_url(leetcode_task_handle)
        github_solution_url_python = get_github_solution_url_python(
            leetcode_task_handle
        )
        github_solution_url_go = get_github_solution_url_go(leetcode_task_handle)

        try:
            title = get_title(leetcode_task_handle)
        except Exception:
            logging.exception(f"Failed to add {leetcode_task_handle}")
            continue

        content = f"[{title}]({leetcode_task_url}) | "

        if os.path.exists(LEETCODE_DIR + "/" + leetcode_task_handle + ".py"):
            content += f"[Python]({github_solution_url_python}) "

        if os.path.exists(LEETCODE_DIR + "/" + leetcode_task_handle + ".go"):
            content += f"[Golang]({github_solution_url_go}) "

        print(content)


if __name__ == "__main__":
    generate()
