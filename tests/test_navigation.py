from conftest import pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_navigation(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(base_url)
    pause()

    # Click each nav link and check we land on that page
    for page in ["photos", "blog"]:
        link = (By.CSS_SELECTOR, f'a.nav-link[href="/{page}"]')
        wait.until(EC.element_to_be_clickable(link)).click()
        wait.until(EC.url_contains(f"/{page}"))
        wait.until(EC.text_to_be_present_in_element_attribute(link, "class", "active"))
        pause()
