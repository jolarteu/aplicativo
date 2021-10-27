import re

from slugify import slugify


def normalize_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r'\(.*?\)', '', name)
    name = name.strip()

    return slugify(name)
