from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def backButton(driver):
	BACK_BUTTON = 'q-btn.q-btn-item.non-selectable.no-outline.q-btn--unelevated.q-btn--rectangle.bg-blue.text-white.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--dense.base-button.base-button--large.q-px-md'
	back_button = driver.find_element(By.CLASS_NAME, BACK_BUTTON)
	back_button.click()
	print('Нажал кнопку "Назад"')
	time.sleep(2)

def nextButton(driver):
	BUTTON_NEXT = 'q-btn.q-btn-item.non-selectable.no-outline.q-btn--unelevated.q-btn--rectangle.bg-blue.text-white.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--dense.base-button.base-button--large.q-px-md'
	button_next = driver.find_element(By.CLASS_NAME, BUTTON_NEXT)
	button_next.click()
	time.sleep(2)
	backButton(driver)
	button_next.click()
	time.sleep(2)


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



