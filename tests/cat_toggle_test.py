from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def photo_modal_toggle(driver: WebDriver) -> None:
    try:
        driver.get("https://hassanbaig.ca/photos")
        sleep(1)

        photo = driver.find_element(
            By.CSS_SELECTOR,
            'img[alt="Waterton. Taken on an iphone 7."]',
        )

        # Click the photo
        photo.click()
        sleep(1)

        photo_modal = driver.find_element(By.ID, "photo-modal")

        # Check if the modal is visible
        if photo_modal.is_displayed():
            print("Photo modal is visible")
        else:
            print("Photo modal is not visible")

        # Click the close button
        photo_modal_close = driver.find_element(By.ID, "photo-modal-close")
        photo_modal_close.click()
        sleep(1)

        # Check if the modal is closed
        if photo_modal.is_displayed():
            print("Photo modal is still visible after closing")
        else:
            print("Photo modal is closed")

    except Exception as e:
        print(f"Error: {e}")
