from conftest import pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PHOTO = (By.CSS_SELECTOR, 'img[alt="Waterton. Taken on an iphone 7."]')
MODAL = (By.CSS_SELECTOR, ".photo-modal")
CLOSE = (By.CSS_SELECTOR, ".photo-modal-close")


def test_photo_modal(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(f"{base_url}/photos")

    photo = wait.until(EC.element_to_be_clickable(PHOTO))
    pause()
    photo.click()
    wait.until(EC.visibility_of_element_located(MODAL))
    pause()

    wait.until(EC.element_to_be_clickable(CLOSE)).click()
    wait.until(EC.invisibility_of_element_located(MODAL))
    pause()
