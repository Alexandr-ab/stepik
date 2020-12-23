import math
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/find_link_text'
    browser.get(link)
    code = str(math.ceil(math.pow(math.pi, math.e)*10000))
    find = browser.find_element_by_link_text(code)
    find.click()
    fn = browser.find_element_by_name('first_name')
    ln = browser.find_element_by_name('last_name')
    city = browser.find_element_by_name('firstname')
    country = browser.find_element_by_id('country')

    fn.send_keys('Alex')
    ln.send_keys('B')
    city.send_keys('Lisbon')
    country.send_keys('Portugal')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(20)
    browser.quit()
