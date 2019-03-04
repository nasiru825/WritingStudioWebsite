from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os

binary = FirefoxBinary("C:\Program Files\Mozilla Firefox\firefox.exe")

days=["Monday","Tuesday","Wednesday","Thursday","Friday"]

driver = webdriver.Firefox(executable_path=r'C:\Users\nasir\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe') 
driver.get("http://localhost:51923/Home/Index")

time.sleep(3)
about=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul[1]/li[2]/a")
about.click()
time.sleep(3)
contact=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul[1]/li[3]/a")
contact.click()
time.sleep(3)
register=driver.find_element_by_xpath('//*[@id="registerLink"]')
register.click()
time.sleep(2)
Register_submit=driver.find_element_by_xpath('/html/body/div[2]/form/div[8]/div/input')
Register_submit.click()
time.sleep(1)
register_Username=driver.find_element_by_xpath('//*[@id="UserName"]')
register_Username.click()
register_Username.send_keys("name")
register_email=driver.find_element_by_xpath('//*[@id="Email"]')
register_email.click()
register_email.send_keys("name@yahoo.com")
register_password=driver.find_element_by_xpath('//*[@id="Password"]')
register_password.click()
register_password.send_keys("FullPassword#123")
register_confirmpassword=driver.find_element_by_xpath('//*[@id="ConfirmPassword"]')
register_confirmpassword.click()
register_confirmpassword.send_keys("FullPassword#123")
register_major=driver.find_element_by_xpath('//*[@id="Major"]')
register_major.click()
register_major.send_keys("Art")
register_education=driver.find_element_by_xpath('//*[@id="StudentEducation"]')
register_education.click()
education_option=driver.find_element_by_xpath('//*[@id="StudentEducation"]/option[2]')
time.sleep(1)
education_option.click()
time.sleep(1)
Register_submit.click()

# Schedule Appointents
schedule=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/p[2]/a')
schedule.location_once_scrolled_into_view
time.sleep(2)
schedule.click()
schedule_submit=driver.find_element_by_xpath('/html/body/div[2]/form/div[6]/div/input')
schedule_submit.click()
time.sleep(1)
first=driver.find_element_by_xpath('//*[@id="FirstName"]')
first.click()
first.send_keys("name1")
last=driver.find_element_by_xpath('//*[@id="LastName"]')
last.click()
last.send_keys("name2")
Times=driver.find_element_by_xpath('//*[@id="Time"]')
Times.click()
Times.send_keys("10:00 am")
email=driver.find_element_by_xpath('//*[@id="Email"]')
email.click()
email.send_keys("name@yahoo.com")
time.sleep(2)
schedule_submit.click()
time.sleep(1)
home=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul[1]/li[1]/a')
home.click()
# Tutors Schedule
tutors=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/p[2]/a')
tutors.location_once_scrolled_into_view
time.sleep(2)
tutors.click()
tutors_time=driver.find_element_by_xpath('//*[@id="myInput"]')
tutors_time.click()
for num in range(5):
    tutors_time.send_keys(days[num])
    time.sleep(1)
    tutors_time.clear()
for num2 in range(5):
    tutors_time.send_keys(days[num2].upper())
    time.sleep(1)
    tutors_time.clear()
for num3 in range(5):
    tutors_time.send_keys(days[num3].lower())
    time.sleep(1)
    tutors_time.clear()
for numshort in range(5):
    tutors_time.clear()
    tutors_time.send_keys(days[numshort][0:3])
    time.sleep(1)
for numshort2 in range(5):
    tutors_time.clear()
    tutors_time.send_keys(days[numshort2][0:3].upper())
    time.sleep(1)
for numshort3 in range(5):
    tutors_time.clear()
    tutors_time.send_keys(days[numshort3][0:3].lower())
    time.sleep(1)
home=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul[1]/li[1]/a')
home.click()
FAQ=driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[3]/p[2]/a')
FAQ.location_once_scrolled_into_view
time.sleep(1)
FAQ.click()
Q1=driver.find_element_by_xpath('/html/body/div[2]/dl/dt[1]/button')
Q1.click()
time.sleep(1)
Q2=driver.find_element_by_xpath('/html/body/div[2]/dl/dt[2]/button')
Q2.click()
time.sleep(1)
Q3=driver.find_element_by_xpath('/html/body/div[2]/dl/dt[3]/button')
Q3.click()
time.sleep(1)
Q4=driver.find_element_by_xpath('/html/body/div[2]/dl/dt[4]/button')
Q4.click()
time.sleep(1)
Q1.click()
time.sleep(1)
Q2.click()
time.sleep(1)
Q3.click()
time.sleep(1)
Q4.click()
time.sleep(1)
home=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/ul[1]/li[1]/a')
home.click()
    










