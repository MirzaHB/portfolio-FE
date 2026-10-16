from conftest import pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dark_mode(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(base_url)

    # Note which theme the page starts in
    page = driver.find_element(By.TAG_NAME, "html")
    started_dark = "dark-theme" in page.get_attribute("class")
    pause()

    # Switch the theme and check it changed
    theme_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label*="mode"]')))
    theme_button.click()
    wait.until(lambda _: ("dark-theme" in page.get_attribute("class")) != started_dark)
    pause()

    # Switch it back and check it's the same as the start
    theme_button.click()
    wait.until(lambda _: ("dark-theme" in page.get_attribute("class")) == started_dark)
    pause()
