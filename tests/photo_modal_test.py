from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def photo_modal_toggle(driver: WebDriver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://hassanbaig.ca/photos")

    photo = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'img[alt="Waterton. Taken on an iphone 7."]')
        )
    )
    photo.click()

    # Check that the modal opens
    modal = wait.until(EC.visibility_of_element_located((By.ID, "photo-modal")))
    print(f"Modal is visible: {modal.is_displayed()}")

    # Close the modal
    close_button = wait.until(EC.element_to_be_clickable((By.ID, "photo-modal-close")))
    close_button.click()

    # Check that the modal closes
    wait.until(EC.invisibility_of_element_located((By.ID, "photo-modal")))
    print("Modal is closed")
