from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time
group = 'ЭКН211-1'

url = 'https://schedule.mi.university/ruz/'
driver = webdriver.Chrome(executable_path='/Users/work/bot2(schedule mmu)/chrome/chromedriver')
