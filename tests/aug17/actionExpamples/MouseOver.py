from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import ActionChains

# option = webdriver.ChromeOptions()
# option.add_experimental_option("useAutomationExtension", False)
# option.add_experimental_option("excludeSwitches", ["enabled-automation"])
driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.myntra.com/")


action =ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//a[@class='desktop-main'][contains(text(),'Men')]")).move_to_element(driver.find_element_by_link_text("T-Shirts")).click().perform()


