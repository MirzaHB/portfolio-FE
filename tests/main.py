from cat_toggle_test import cat_toggle_test
from photo_modal_toggle import photo_modal_toggle
from selenium import webdriver

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "normal"

    driver = webdriver.Chrome(options=options)

    try:
        cat_toggle_test(driver)
        photo_modal_toggle(driver)

    finally:
        driver.quit()
