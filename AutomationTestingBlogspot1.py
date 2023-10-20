from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
import time

driver_path = r"C:\Drivers\msedgedriver.exe"
edge_options = Options()
edge_options.add_argument("--disable-infobars")
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=edge_options)


driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

##handle textbox
Fillupname = driver.find_element(By.XPATH,'//input[@id="name"]')
Fillupname.send_keys('NAZNAZ')
                     
Fillupemail = driver.find_element(By.ID,'email')
Fillupemail.send_keys('naznaz@gmail.com')

Fillupphone = driver.find_element(By.ID,'phone')
Fillupphone.send_keys('0123456')

Fillupaddress = driver.find_element(By.XPATH,"//textarea[@id='textarea']")
Fillupaddress.send_keys('No6, Lorong KP2, Taman Kota')


##Selecting checkbox for male and print in console that female checkbox is not selected
driver.find_element(By.XPATH,"//input[@id='male']").click()

womanradiobutton = driver.find_element(By.XPATH,"//input[@id='female']")
print("is woman checkbox is selected : " ,womanradiobutton.is_selected())

#handle multiple checkboxes
checkboxes  = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and @class = 'form-check-input']") 
print(len(checkboxes))
for nama in checkboxes:
    print(nama.get_attribute("id"))

#now we want to select 2 weekdays

for check in checkboxes:
    weekday = check.get_attribute("id")
    if weekday == 'saturday' or weekday == 'friday':
        check.click()


#handling dropdown dropdown

dropdowns = driver.find_element(By.XPATH,"//select[@id='country']")
selectingdrowpdown = Select(dropdowns)

selectingdrowpdown.select_by_index('1')


#handling alerts with prompt

alertwithprompt = driver.find_element(By.XPATH,'//button[@onclick="myFunctionPrompt()"]')
alertwithprompt.click()

alertwindown = driver.switch_to.alert
print(alertwindown.text)
alertwindown.send_keys("ABC")
time.sleep(10)


alertwindown.accept()


input("Press Enter to close the browser...")
driver.quit()
