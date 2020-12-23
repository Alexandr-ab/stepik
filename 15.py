from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/math.html'
try:
    ch = webdriver.Chrome()
    ch.get(link)
    x = ch.find_element_by_id('input_value').text
    y = calc(x)
    answer = ch.find_element_by_id('answer')
    answer.send_keys(y)
    check = ch.find_element_by_id('robotCheckbox')
    check.click()
    radio = ch.find_element_by_id('robotsRule')
    radio.click()
    button = ch.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(15)
    ch.quit()

