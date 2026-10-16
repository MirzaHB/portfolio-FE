from conftest import BASE_URL, make_driver
from test_cat_toggle import test_cat_toggle
from test_photo_modal import test_photo_modal

if __name__ == "__main__":
    driver = make_driver()

    try:
        test_cat_toggle(driver, BASE_URL)
        test_photo_modal(driver, BASE_URL)
        print("All tests passed")

    finally:
        driver.quit()
