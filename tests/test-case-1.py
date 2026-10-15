from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)


try:
    driver.get("https://hassanbaig.ca/")

    cat_icon = driver.find_element(By.ID, "oneko")

    cat_icon.is_displayed()

    cat_toggle_button = driver.find_element(By.CLASS_NAME, "cat-toggle")
    print("something")

except Exception:
    print(Exception)
