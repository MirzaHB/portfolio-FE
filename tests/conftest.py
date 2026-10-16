import os

import pytest
from selenium import webdriver

BASE_URL = os.environ.get("BASE_URL", "https://hassanbaig.ca").rstrip("/")


@pytest.fixture
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "1") != "0":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
