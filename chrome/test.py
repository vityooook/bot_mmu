# from selenium import webdriver   # задача №1
# from selenium.webdriver.common.by import By
# import time
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/1/1.html')
#     input_form = driver.find_elements(By.CLASS_NAME, 'form')
#     for i in range(6):
#         input_form[i].send_keys(i)
#     time.sleep(2)
#     button = driver.find_element(By.ID, 'btn').click()
#     time.sleep(10)

# from selenium import webdriver   # задача №2
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/2/2.html')
#     find = driver.find_element(By.LINK_TEXT, '16243162441624').click()
#     find_2 = driver.find_element(By.ID, 'result')
#     time.sleep(5)
#     print(find_2.text)

# from selenium import webdriver   # задача №3
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/3/3.html')
#
#     result = [int(i.text) for i in driver.find_elements(By.XPATH, "//div[@class='text']/p")] #version 1
#     print(sum(result))
#     find = driver.find_elements(By.XPATH, "//div[@class='text']/p") #version 2
#     for i in find:
#         result += int(i.text)
#     print(result)


# from selenium import webdriver   # задача №4
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/3/3.html')
#
#     result = [int(i.text) for i in driver.find_elements(By.XPATH, "//div[@class='text']/p[2]")]
#     print(sum(result))



# from selenium import webdriver   # задача №5
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/4/4.html')
#     check = driver.find_elements(By.CLASS_NAME, 'check')
#     for i in check:
#         i.click()
#     time.sleep(5)
#     botton = driver.find_element(By.CLASS_NAME, 'btn').click()
#     time.sleep(3)



# from selenium import webdriver   # задача №6
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/5/5.html')
#     num = [1, 2, 3, 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 22, 23, 28, 29,
#                33, 34, 38,
#                39, 43, 44, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 63, 64, 68,
#                69, 73,
#                74, 78, 79, 83, 84, 88, 89, 91, 92, 97, 98, 101, 104, 108, 109, 113, 114,
#                149, 153,
#                184, 185,
#                119, 123, 124, 128, 129, 131, 132, 137, 138, 140, 141, 144, 145, 148,
#                154, 158, 159, 163, 164, 165, 168, 169, 171, 172, 177, 178, 180, 181,
#
#                187, 188, 189, 190, 192, 193, 194, 195, 197, 198, 199, 200, 204, 205,
#                206, 207,
#                254, 255,
#                208, 209, 211, 212, 217, 218, 220, 221, 224, 225, 227, 228, 229, 230,
#                232, 233,
#                234, 235, 237, 238, 239, 240, 245, 246, 247, 248, 249, 251, 252, 253,
#
#                256, 257, 258, 260, 261, 264, 265, 268, 269, 273, 274, 278, 279, 288,
#                289, 291,
#
#                348, 349,
#                292, 293, 294, 295, 296, 297, 300, 301, 302, 303, 304, 305, 308, 309,
#                313, 314,
#                318, 319, 328, 329, 331, 332, 339, 340, 341, 342, 343, 344, 345, 346,
#
#                353, 354, 358, 359, 368, 369, 371, 372, 379, 380, 385, 386, 408, 409,
#                411, 412,
#                478, 479,
#                419, 420, 425, 426, 428, 429, 433, 434, 438, 439, 444, 445, 446, 447,
#                448, 451,
#                452, 459, 460, 465, 466, 467, 468, 469, 470, 472, 473, 474, 475, 477,
#
#                480, 485, 486, 487, 488, 491, 492, 499, 500, 505, 506, 508, 509, 513,
#                514, 518, 519]
#     # my_num = []
#     # check = driver.find_elements(By.CLASS_NAME, 'check')
#     # for i in check:
#     #     my_num.append(i.get_attribute('value')
#     # [x.click() for n, x in enumerate(driver.find_elements(By.CLASS_NAME, 'check'),
#     #                                  start=1) for y in num if y == n] #cersion 1
#     bebe = enumerate(driver.find_elements(By.CLASS_NAME, 'check'), start=1) #version 2
#     for n, x in bebe:
#         for y in num:
#             if y == n:
#                 x.click()

# from selenium import webdriver  # задача №7
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/7/7.html')
#     num = []
#     # find_1 = driver.find_elements(By.TAG_NAME, 'option') # version 1
#     # for i in find_1:
#     #     num.append(int(i.text))
#     # print(sum(num))
#     result = [int(i.text) for i in driver.find_elements(By.TAG_NAME, 'option')] # version 2
#     print(sum(result))


# from selenium import webdriver  # задача №8
# from selenium.webdriver.common.by import By
# import time
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/selenium/6/6.html')
#     a = ((12434107696 * 3) * 2) + 1
#     find = driver.find_elements(By.TAG_NAME, 'option')
#     for i in find:
#         if int(i.text) == a:
#             i.click()
#     time.sleep(1)
#     driver.find_element(By.CLASS_NAME, 'btn').click()
#     time.sleep(4)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless')
#
# with webdriver.Chrome(options = options_chrome) as driver:
#     driver.get('https://yandex.ru/')
#     find = driver.find_element(By.TAG_NAME, 'a')
#     print(find.get_attribute('href'))

# from pprint import pprint
# from selenium import webdriver
#
# with webdriver.Chrome() as driver:
#
#     driver.get('https://yandex.ru/')
#     cookies = driver.get_cookies()
#     pprint(cookies)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/methods/1/index.html')
#     while True:
#         num = driver.find_element(By.ID, 'result').text
#         driver.refresh()
#         if num.isdigit():
#             print(num)
#             break


# from selenium import webdriver
# num = []
# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/methods/3/index.html')
#     cookies = driver.get_cookies()
#     for cookie in cookies:
#         num.append(int(cookie['value']))
#     print(sum(num))

from selenium import webdriver
import re
# num = []

# with webdriver.Chrome() as driver:
#     driver.get('https://parsinger.ru/methods/3/index.html')
#     cookies = driver.get_cookies()
#     for cookie in cookies:
#         clear = cookie['name']
#         digit = int(re.sub(r'secret_cookie_', r'', clear))
#         if digit % 2 == 0:
#             num.append(digit)
#
#     print(sum(num))


from selenium import webdriver
from selenium.webdriver.common.by import By

