from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Juhi\\PycharmProjects\\Selenium_Turorial\\drivers\\chromedriver.exe")
driver.maximize_window()
location = "file:///C:/Users/Juhi/PycharmProjects/Selenium_Turorial/PAGES/confirmation_alert.html"
driver.get(location)

#Click on the "Alert" button to generate the Simple Alert
button = driver.find_element_by_name('alert')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
obj.accept()

print(" Clicked on the OK Button in the Alert Window")

driver.close