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

        date = []
        dotw = []
        time = []
        subjects = []
        type_of_subject = []
        cabinet = []
        teacher = []
        for lesson in lessons:
            date_raw = lesson.find('div', class_='d-lg-none date clearfix').find_next("span")
            date.append(date_raw.text)
            dotw_row = lesson.find('div', class_='d-lg-none date clearfix').find_next("span").find_next("span")
            dotw.append(dotw_row.text)
            time_raw = lesson.find('div', class_='d-lg-none date clearfix').find_next("span").find_next(
                "span").find_next("span")
            time.append(time_raw.text)

            subject_raw = lesson.find('div', class_='title').find_next("span")
            subjects.append(subject_raw.text)
            type_of_subject_raw = lesson.find("div", "text-muted kind ng-star-inserted")
            type_of_subject.append(type_of_subject_raw.text)

            cabinet_raw = lesson.find('table', class_='info').find_next("tr")
            cabinet.append(cabinet_raw.text)
            teacher_raw = lesson.find('table', class_='info').find_next("tr").find_next("tr").find_next("tr")
            teacher.append(teacher_raw.text)

        print(tabulate({"date": date,
                        "dotw": dotw,
                        "time": time,
                        "subject": subjects,
                        "type_of_subject": type_of_subject,
                        "cabinet": cabinet,
                        "teacher": teacher}, headers="keys"))



def main():
    # get_source_html('экн211-1','26.09.2023')
    get_lessons(file_path='/Users/work/bot_mmu/bot_mmu/chrome/lessons.html')


if __name__ == "__main__":
    main()
