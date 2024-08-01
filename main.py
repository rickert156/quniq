from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dataTest import email, domain, user_name, userLastname, user_phone, otp_code
from positive.start import start
from positive.auth import auth, inputDataUser, otpCode, selectCompany
from positive.newProject import newProject, notNewProject
from positive.linkSearch import linkSearch
import time

driver = webdriver.Chrome()
driver.maximize_window()

def createProject(driver):
	create_project = input('\nСоздать новый проект?(y/n) ')
	if create_project == 'y':newProject(driver)
	elif create_project == 'n':notNewProject(driver)
	else:
		print('Некорректный выбор!')
		createProject(driver)


def stepLogin(email):
	start(driver, domain)
	selectTest = input('Test Quinq\nЭтап Аваторизации, нужно будет вводить команды с клавиатуры.\n\nПользователь зарегистирован?(у/n) ')
	
	if selectTest == 'y':
		auth(driver, email)
		otpCode(driver, otp_code)
	elif selectTest == 'n':
		email = input('Введи имейл для теста: ')
		auth(driver, email)
		inputDataUser(driver, user_name, userLastname, user_phone)
		otpCode(driver, otp_code)
	else:
		print('Некорректный выбор!\n')
		stepLogin(email)

	selectCompany(driver)
	createProject(driver)
	linkSearch(driver)


if __name__ == '__main__':
	stepLogin(email)