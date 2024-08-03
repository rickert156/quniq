from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def createNewProject(driver):
	for listButton in driver.find_elements(By.CLASS_NAME, 'q-radio__label.q-anchor--skip'):
		listButton = listButton.text
		print(listButton)