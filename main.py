from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from positive.start import start 
from positive.auth import auth, inputDataUser, otpCode, selectCompany
import time

email = 'rickert@testeeeeeer.com'
domain = 'https://hill.test.quniq.net/auth'
user_name = 'Max'
user_phone = '9961112222'
otp_code = '123456'

driver = webdriver.Chrome()
driver.maximize_window()


if __name__ == '__main__':
	start(driver, domain)
	auth(driver, email)
	if inputDataUser(driver, user_name, user_phone):
		print('Заполнили данные пользователя')
	if otpCode(driver, otp_code):
		print('Данный пользователя вводить не нужно')
	selectCompany(driver)

