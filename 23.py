from selenium import webdriver as wd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = wd.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    wdw(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    x = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(x))
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()