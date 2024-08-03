from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dataTest import listEmail, name_project, description
import time

FIELD = 'q-field__native.q-placeholder'
ALTERNATIVE_BUTTON = 'q-btn.q-btn-item.non-selectable.no-outline.q-btn--outline.q-btn--rectangle.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.aux-buttons'
BUTTON_BACK = 'q-btn.q-btn-item.non-selectable.no-outline.q-btn--unelevated.q-btn--rectangle.bg-blue.text-white.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--dense.base-button.base-button--large.q-px-md'

def backButton(driver):
	back_button = driver.find_element(By.CLASS_NAME, BUTTON_BACK)
	back_button.click()
	print('Нажал кнопку "Назад", работает')
	time.sleep(2)

def nextButton(driver):
	BUTTON_NEXT = 'q-icon.notranslate.material-icons.icon-arrow-toright'
	button_next = driver.find_element(By.CLASS_NAME, BUTTON_NEXT)
	button_next.click()
	time.sleep(2)
	backButton(driver)
	button_next.click()
	print('Нажал кнопку "Продолжить", работает')
	time.sleep(2)

def role(driver):
	radio_button = 'q-radio__bg.absolute.non-selectable'
	number_button=0
	for button in driver.find_elements(By.CLASS_NAME,  radio_button):
		number_button+=1
		button.click()
		time.sleep(0.5)
		button = button.text
	print('Выбрал роли, цели, количество сотрудников')
	nextButton(driver)

def invite(driver):
	number_field = 0
	for send_email in driver.find_elements(By.CLASS_NAME, FIELD):
		send_email.send_keys(listEmail[number_field])
		number_field+=1
		time.sleep(1)
	print('Ввел имейлы для приглашения')
	time.sleep(2)
	after_button = driver.find_element(By.CLASS_NAME, ALTERNATIVE_BUTTON)
	after_button.click()
	print('Выбрал "Позже"')
	time.sleep(2)

def projectDescription(driver):
	number_field = 0
	for send_data in driver.find_elements(By.CLASS_NAME, FIELD):
		number_field+=1
		if number_field == 1:send_data.send_keys(name_project)
		if number_field == 2:send_data.send_keys(description)
		time.sleep(2)
	print('Ввели название и описание проекта')
	createProj = driver.find_element(By.CLASS_NAME, 'q-icon.notranslate.material-icons.icon-arrow-toright')
	createProj.click()
	print('Проект Создан')
	time.sleep()

def createNewProject(driver):
	number_button = 0
	print('Кнопки на экране: ')
	for listButton in driver.find_elements(By.CLASS_NAME, 'q-radio__label.q-anchor--skip'):
		number_button+=1
		listButton.click()
		time.sleep(0.5)
		listButton = listButton.text		
		print(f'\t[{number_button}] {listButton}')
	nextButton(driver)
	role(driver)
	invite(driver)
	projectDescription(driver)
	time.sleep(10)



