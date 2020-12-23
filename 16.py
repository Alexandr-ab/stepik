from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    br = webdriver.Chrome()
    br.get(link)
    img = br.find_element_by_tag_name('img')
    x = img.get_attribute('valuex')
    y = calc(x)
    answer = br.find_element_by_id('answer')
    answer.send_keys(y)
    check = br.find_element_by_id('robotCheckbox')
    check.click()
    radio = br.find_element_by_id('robotsRule')
    radio.click()
    button = br.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    br.quit()
