from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PHOTO = (By.CSS_SELECTOR, ".photo-item img")
MODAL = (By.CSS_SELECTOR, ".photo-modal")
CLOSE = (By.CSS_SELECTOR, ".photo-modal-close")


def test_photo_modal_opens_and_closes(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(f"{base_url}/photos")

    wait.until(EC.element_to_be_clickable(PHOTO)).click()
    wait.until(EC.visibility_of_element_located(MODAL))

    wait.until(EC.element_to_be_clickable(CLOSE)).click()
    wait.until(EC.invisibility_of_element_located(MODAL))
