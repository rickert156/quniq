from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dataTest import email, domain, user_name, user_phone, otp_code
from positive.start import start 
from positive.auth import auth, inputDataUser, otpCode, selectCompany
import time

driver = webdriver.Chrome()
driver.maximize_window()

def stepLogin(email):
	start(driver, domain)
	selectTest = input('Test Quinq\nПользователь зарегистирован?(у/n) ')
	
	if selectTest == 'y':
		auth(driver, email)
		otpCode(driver, otp_code)
	elif selectTest == 'n':
		email = input('Введи имейл для теста: ')
		auth(driver, email)
		inputDataUser(driver, user_name, user_phone)
		otpCode(driver, otp_code)
	else:
		print('Некорректный выбор!')
		breake

	selectCompany(driver)

if __name__ == '__main__':
	stepLogin(email)