from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# option = webdriver.ChromeOptions()
# option.add_experimental_option("useAutomationExtension", False)
# option.add_experimental_option("excludeSwitches", ["enabled-automation"])
driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.google.com/")
assert "Google" in driver.title

driver.find_element_by_name("q").click()
driver.find_element_by_xpath("//*[@name='q']").click()
driver.find_element_by_xpath("//*[@name='q']").send_keys("selenium")
driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//a/h3[contains(text(),'Selenium.dev')]").click()



driver.find_elements_by_css_selector("#email").send_keys("")
assert "SeleniumHQ Browser Automation" in driver.title
driver.quit()