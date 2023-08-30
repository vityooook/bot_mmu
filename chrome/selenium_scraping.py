from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time

list_of_data = []

with webdriver.Chrome(executable_path='/Users/work/bot2(schedule mmu)/chrome/chromedriver_new_version') as driver:
    driver.get('https://mmu2021:mmu2021@schedule.mi.university/ruz/')
    time.sleep(4)
    # group of students
    group = driver.find_element(By.ID, 'autocomplete-group')
    group.send_keys('ЭКН211-1')
    time.sleep(1)
    group.send_keys(Keys.ENTER)
    # date calendar
    date = driver.find_element(By.ID, 'start')
    date.send_keys(Keys.COMMAND + 'a')
    date.send_keys(Keys.DELETE)
    date.send_keys('18.09.2023')
    driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-right']").click()
    driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()

    time.sleep(2)
    date_1 = driver.find_element(By.XPATH, "(//span[contains(text(),'Пн')])[1]")
    # date_1 = driver.find_elements(By.CLASS_NAME, 'd-lg-none date clearfix')
#     for x in date_1:
#         list_of_data.append(x.text)
    time.sleep(4)

print(str(date_1.text))
# print(list_of_data)
