from conftest import BASE_URL, make_driver
from test_cat_toggle import test_cat_toggle
from test_dark_mode import test_dark_mode
from test_navigation import test_navigation
from test_photo_modal import test_photo_modal

if __name__ == "__main__":
    driver = make_driver()

    try:
        test_cat_toggle(driver, BASE_URL)
        test_photo_modal(driver, BASE_URL)
        test_dark_mode(driver, BASE_URL)
        test_navigation(driver, BASE_URL)
        print("All tests passed")

    finally:
        driver.quit()
