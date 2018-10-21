from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

#windows chrome driver, change accordingly , download correct driver
driver = webdriver.Chrome('./chromedriver')

#Opening whatsapp web, need to scan QR code after this one
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = '"Pranav CH1 126"' #can be any contact name

#searching for contact, entering the chat
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

def push_whatsapp(string):
	message.send_keys(string)
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()
	