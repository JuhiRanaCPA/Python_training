import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.google.com/")
assert "Google" in driver.title

driver.find_element_by_name("q").click()
driver.find_element_by_xpath("//*[@name='q']").click()
driver.find_element_by_xpath("//*[@name='q']").send_keys("selenium")
driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//a/h3[contains(text(),'Selenium.dev')]").click()
assert "SeleniumHQ Browser Automation" in driver.title



# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com")






