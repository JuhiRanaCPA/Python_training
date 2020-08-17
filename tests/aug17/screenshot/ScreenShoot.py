import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.google.com/")
assert "Google" in driver.title

driver.get_screenshot_as_file("C:/Users/Juhi/PycharmProjects/Selenium_Turorial/Screenshot/screenshoot.png")
driver.quit()








