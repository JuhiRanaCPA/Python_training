import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains

# option = webdriver.ChromeOptions()
# option.add_experimental_option("useAutomationExtension", False)
# option.add_experimental_option("excludeSwitches", ["enabled-automation"])
driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Static.html")


actions = ActionChains(driver)
sourceElement = driver.find_element_by_xpath("//img[@id='angular']")
destinationElement = driver.find_element_by_xpath("//div[@id='droparea']")
time.sleep(4)
actions.drag_and_drop(sourceElement,destinationElement).perform()