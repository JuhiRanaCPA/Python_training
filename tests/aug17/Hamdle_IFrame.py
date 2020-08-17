from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/Juhi/PycharmProjects/Selenium_Turorial/drivers/chromedriver.exe")
driver.maximize_window()
location = "file:///C:/Users/Juhi/PycharmProjects/Selenium_Turorial/PAGES/Iframe.html"
driver.get(location)

########Section-1

# get the list of iframes present on the web page using tag "iframe"

seq = driver.find_elements_by_tag_name('iframe')

print("No of frames present in the web page are: ", len(seq))

#switching between the iframes based on index

for index in range(len(seq)):

    #switching between the iframes based on index
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(30)

    button = driver.find_element_by_name('alert')
    button.click()

    time.sleep(5)
    obj = driver.switch_to.alert
    msg=obj.text
    print ("Alert shows following message: "+ msg )
    obj.accept()

driver.switch_to.default_content()





##############################Section-2

#switch to a specific iframe (First frame) using Id as locator

iframe = driver.find_element_by_id('FR2')

driver.switch_to.frame(iframe)

#highlight the contents of the selected iframe
button = driver.find_element_by_name('alert')
button.click()

# time.sleep(5)
#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
#use the accept() method to accept the alert
obj.accept()

driver.switch_to.default_content()




##########################Section-3

#switch to a specific iframe (Second frame) using name as locator

iframe = driver.find_element_by_name('frame1')

driver.switch_to.frame(iframe)

#highlight the contents of the selected iframe
button = driver.find_element_by_name('alert')
button.click()

# time.sleep(5)
#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )
#use the accept() method to accept the alert
obj.accept()


driver.switch_to.default_content()

print("Heading of default page is :"+ driver.find_element_by_xpath("//h1").text)
driver.quit()




