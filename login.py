from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from selenium.webdriver.common.by import By

def test_login_flow():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message
    driver.find_element(By.CSS_SELECTOR, "a.button.secondary").click()

    driver.quit()
