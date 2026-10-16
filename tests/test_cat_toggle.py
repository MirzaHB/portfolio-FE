from conftest import pause
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_cat_toggle(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(base_url)

    # Check the cat is on the page
    cat_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cat-toggle")))
    wait.until(EC.visibility_of_element_located((By.ID, "oneko")))
    pause()

    # Send the cat home and check it's gone
    cat_button.click()
    wait.until(EC.invisibility_of_element_located((By.ID, "oneko")))
    pause()

    # Bring the cat back and check it's visible again
    cat_button.click()
    wait.until(EC.visibility_of_element_located((By.ID, "oneko")))
    pause()
