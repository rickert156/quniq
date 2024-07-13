from selenium import webdriver
import time

def start(driver, domain):
	driver.get(domain)
	time.sleep(2)