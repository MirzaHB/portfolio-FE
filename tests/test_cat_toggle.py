from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TOGGLE = (By.CSS_SELECTOR, "button.cat-toggle")
CAT = (By.ID, "oneko")


def test_cat_toggle_removes_and_restores_cat(driver, base_url):
    wait = WebDriverWait(driver, 15)
    driver.get(base_url)

    toggle = wait.until(EC.element_to_be_clickable(TOGGLE))
    wait.until(EC.presence_of_element_located(CAT))
    assert toggle.get_attribute("aria-pressed") == "true"

    # The cat runs off-screen before it removes itself
    toggle.click()
    wait.until(EC.invisibility_of_element_located(CAT))
    wait.until(EC.text_to_be_present_in_element_attribute(TOGGLE, "aria-pressed", "false"))

    toggle.click()
    wait.until(EC.presence_of_element_located(CAT))
    wait.until(EC.text_to_be_present_in_element_attribute(TOGGLE, "aria-pressed", "true"))
