from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

def linkSearch(driver):
	current = driver.current_url
	number_links = 0
	for links in driver.find_elements(By.TAG_NAME, 'a'):
		number_links+=1
		links = links.get_attribute('href')
		response = requests.get(links)
		response = response.status_code
		print(f'[{number_links}] Status code: {response} | {links}')

