import os
from time import sleep

import pytest
from selenium import webdriver

BASE_URL = os.environ.get("BASE_URL", "https://hassanbaig.ca").rstrip("/")
PAUSE = float(os.environ.get("PAUSE", "0.5"))


def pause() -> None:
    sleep(PAUSE)


def make_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "1") != "0":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    return webdriver.Chrome(options=options)


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def driver():
    driver = make_driver()
    yield driver
    driver.quit()
