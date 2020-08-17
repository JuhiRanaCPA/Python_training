import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains

# option = webdriver.ChromeOptions()
# option.add_experimental_option("useAutomationExtension", False)
# option.add_experimental_option("excludeSwitches", ["enabled-automation"])
driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")


actions = ActionChains(driver)
# perform doubleclick
time.sleep(5)
actions.double_click(driver.find_element_by_xpath("//button[contains(text(),'Double-Click Me To See Alert')]")).perform()
obj = driver.switch_to.alert
msg=obj.text
print ("Alert shows following message: "+ msg )
time.sleep(2)
obj.accept()

driver.quit()

