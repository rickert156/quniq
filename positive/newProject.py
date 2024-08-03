from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from positive.createNewProject import createNewProject
import time

newProj = 'Создания проекта'

def newProject(driver):
	print(f'\nЭтап [{newProj}]')
	create_project = driver.find_element(By.CLASS_NAME, 'q-card__section.q-card__section--vert.text-center')
	create_project.click()
	print('Создаем новый проект...')
	time.sleep(2)
	createNewProject(driver)

def notNewProject(driver):
	not_create_project = driver.find_element(By.CLASS_NAME, 'q-btn.q-btn-item.non-selectable.no-outline.q-btn--outline.q-btn--rectangle.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--dense.aux-buttons')
	not_create_project.click()
	print('Новый проект не создаем...')
	time.sleep(2)