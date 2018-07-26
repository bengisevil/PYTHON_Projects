#!/usr/bin/env python3
import sys
import os
import bs4 as bs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

webdriver.chrome.driver = '/usr/local/lib/python3.5/dist-packages/selenium/webdriver/chrome/chromedriver'
#https://stackoverflow.com/questions/49071664/chromium-chromedriver-missing-library-libgfx-on-raspberry-pi/50159947#50159947

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(webdriver.chrome.driver, chrome_options = options)
driver.implicitly_wait(30)

##TODO: NEED TO RECEIVE class and major (in the exact format given below) 

# Navigate to the application home page
driver.get("https://ece.vt.edu/undergrad/curriculum")

majors = ["Electrical Engineering", "Computer Engineering"]
year = ["2017", "2018", "2019"]

##TODO: LOOP HERE 

#Select major and year 
driver.find_element_by_xpath('//*[@id="selectProgram"]/option[text()="%s"]' %majors[0]).click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="selectYear"]/option[text()="%s"]' %year[1]).click()
time.sleep(2)

#Freshman
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(1) > li:nth-child(1)').click()
classes = driver.find_element_by_xpath('//*[@id="freshmanClasses"]/div[1]').text
freshman_fall = classes.split('\n')
classes = driver.find_element_by_xpath('//*[@id="freshmanClasses"]/div[2]').text
freshman_spring = classes.split('\n')
time.sleep(1)
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(1) > li:nth-child(1)').click()
time.sleep(1)

#Sophomore
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(2) > li:nth-child(1)').click()
classes = driver.find_element_by_xpath('//*[@id="sophomoreClasses"]/div[1]').text
soph_fall = classes.split('\n')
classes = driver.find_element_by_xpath('//*[@id="sophomoreClasses"]/div[2]').text
soph_spring = classes.split('\n')
time.sleep(2)
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(2) > li:nth-child(1)').click()
time.sleep(1)

#Junior
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(1) > li:nth-child(3)').click()
classes = driver.find_element_by_xpath('//*[@id="juniorClasses"]/div[1]').text
junior_fall = classes.split('\n')
classes = driver.find_element_by_xpath('//*[@id="juniorClasses"]/div[2]').text
junior_spring = classes.split('\n')
time.sleep(2)
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(1) > li:nth-child(3)').click()
time.sleep(1)

#Senior
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(2) > li:nth-child(3)').click()
classes = driver.find_element_by_xpath('//*[@id="seniorClasses"]/div[1]').text
senior_fall = classes.split('\n')
classes = driver.find_element_by_xpath('//*[@id="seniorClasses"]/div[2]').text
senior_spring = classes.split('\n')
time.sleep(2)
driver.find_element_by_css_selector('#displayCurriculum > div > div > div > ul > div > div:nth-child(2) > li.yearPanel.panel.panel-default.expanding.open').click()
time.sleep(2)
'''
print (freshman_fall)
print (freshman_spring)
print (soph_fall)
print (soph_spring)
print (junior_fall)
print (junior_spring)
print (senior_fall)
print (senior_spring)
'''

##TODO: NEED TO SEND freshman_fall, freshman_spring ... senior_fall, senior_spring back 

# close the browser window
driver.quit() 
