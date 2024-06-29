import os
import colorama
import json as json_module


def directory(path: str) -> None:
    if not os.path.isdir(path):
        os.makedirs(path)
        print(colorama.Fore.YELLOW + f"Automatically created directory: {path}")


def file(cls, path: str, default_content: str = "") -> None:
    if not os.path.isfile(path):
        file_directory = os.path.dirname(path)
        if directory != "":
            cls.directory(file_directory)
        with open(path, "w+") as outfile:
            outfile.write(default_content)
            print(colorama.Fore.YELLOW + f"Automatically created file: {path}")


def json(path: str, default_content, indent: int = 2):
    file(path, json_module.dumps(default_content, indent=indent))