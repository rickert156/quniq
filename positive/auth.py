from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class_button = 'q-btn__content.text-center.col.items-center.q-anchor--skip.justify-center.row'

def inputDataUser(driver, username, userphone):
	input_number = 0
	for userData in driver.find_elements(By.CLASS_NAME, 'q-field__native.q-placeholder'):
		input_number+=1
		if input_number == 1:
			userData.send_keys(username)
		elif input_number == 2:
			userData.send_keys(userphone)
		time.sleep(1)
	button = driver.find_element(By.CLASS_NAME, class_button)
	button.click()
	print('Ввели имя и номер телефона')
	time.sleep(4)

def otpCode(driver, code):
	otp_code = driver.find_element(By.CLASS_NAME, 'q-field__native.q-placeholder')
	otp_code.send_keys(code)
	otp_code.send_keys(Keys.ENTER)
	print('Введен OTP код')
	time.sleep(4)

def selectCompany(driver):
	company = driver.find_element(By.CLASS_NAME, 'q-item__label.q-item__label--caption.text-caption').click()
	button = driver.find_element(By.CLASS_NAME, class_button).click()
	print('Выбрали компанию')
	time.sleep(5)

def auth(driver, email):
	send_email = driver.find_element(By.CLASS_NAME, 'q-field__native.q-placeholder')
	send_email.send_keys(email)
	time.sleep(2)
	if send_email.send_keys(Keys.ENTER):print('Тест пройден, кнопка работает, можно нажать Enter')
	time.sleep(2)
	print('Ввел имейл на стартовой странице')

def login(driver):
	pass