from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/Juhi/PycharmProjects/Selenium_Turorial/drivers/chromedriver.exe")
driver.maximize_window()
location = "file:///C:/Users/Juhi/PycharmProjects/Selenium_Turorial/PAGES/confirmation_alert.html"
driver.get(location)

#Click on the "employeeLogin" button to generate the Prompt Alert
button = driver.find_element_by_name('continue')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert


time.sleep(2)

#Enter text into the Alert using send_keys()
obj.send_keys('Meenakshi')

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

#Retrieve the message on the Alert window
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

obj.accept()

#get the text returned when OK Button is clicked.
txt = driver.find_element_by_id('msg')
print(txt.text)

driver.close