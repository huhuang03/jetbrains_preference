#!env python3
import os
from pathlib import Path
import re

home = str(Path.home())
ROOT = f"{home}/Library/Caches/"

PRODUCT_PYCHARM = "PyCharm"


def get_product_root(product: str):
    for f in os.listdir(ROOT):
        match = re.search(f"^{product}[\\d.]*$", f)
        if match:
            print(match.string)


def sync(product: str):
    get_product_root(product)


def main():
    sync(PRODUCT_PYCHARM)


if __name__ == '__main__':
    main()

