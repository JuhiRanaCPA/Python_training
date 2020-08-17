import time

from selenium.webdriver import Chrome
from selenium import webdriver


# option = webdriver.ChromeOptions()
# option.add_experimental_option("useAutomationExtension", False)
# option.add_experimental_option("excludeSwitches", ["enabled-automation"])
driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")

currentWindowHandle = driver.current_window_handle
print(currentWindowHandle)

driver.find_element_by_xpath("//div[@id='Tabbed']/a/button").click()

windowHandles = driver.window_handles
print(windowHandles)

for windowhandle in windowHandles:
    driver.switch_to.window(windowhandle)
    print(driver.current_window_handle)
    print(driver.title)



driver.close()
driver.switch_to.window(currentWindowHandle)
print(driver.current_window_handle)





