from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)


try:
    print("something")

except Exception:
    print(Exception)
