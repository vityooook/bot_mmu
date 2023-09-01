from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import time


def get_source_html(number_group, data_lessons):
    with webdriver.Chrome(executable_path='/Users/work/bot_mmu/bot_mmu/chrome/chromedriver_new_version') as driver:
        driver.get('https://mmu2021:mmu2021@schedule.mi.university/ruz/')
        time.sleep(4)

        # group of students
        group = driver.find_element(By.ID, 'autocomplete-group')
        group.send_keys(number_group)
        time.sleep(1)
        group.send_keys(Keys.ENTER)

        # date calendar
        date = driver.find_element(By.ID, 'start')
        date.send_keys(Keys.COMMAND + 'a')
        date.send_keys(Keys.DELETE)
        date.send_keys(data_lessons)
        driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-right']").click()
        driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-left']").click()
        time.sleep(2)

        # download this page
        file = open('lessons.html', 'w')
        file.write(driver.page_source)


def get_lessons(file_path):
    with open(file_path) as file:
        scr = file.read()

        soup = BeautifulSoup(scr, 'lxml')
        lessons = soup.find_all('div', class_='media day ng-star-inserted')

        date_and_time = []
        subjects = []
        additional_info = []
        for lesson in lessons:
            lesson_time = lesson.find('div', class_='d-lg-none date clearfix').text
            lesson_time_clean = re.sub(r"\xa0-", '', lesson_time)  # проблема
            date_and_time.append(lesson_time_clean)

            subject = lesson.find('div', class_='title').text
            subjects.append(subject)

            add = lesson.find('table', class_='info').text
            additional_info.append(add)

        print(tabulate({"date": date_and_time,
                        "subjects": subjects,
                        "info": additional_info}, headers="keys"))


def main():
    # get_source_html('экн211-1','26.09.2023')
    get_lessons(file_path='/Users/work/bot_mmu/bot_mmu/chrome/lessons.html')



if __name__ == "__main__":
    main()
