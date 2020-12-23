from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    br = webdriver.Chrome()
    br.get(link)
    x = br.find_element_by_id('input_value').text
    y = calc(x)
    answer = br.find_element_by_id('answer')
    answer.send_keys(y)
    check = br.find_element_by_id('robotCheckbox')
    check.click()
    br.execute_script('window.scrollBy(0, 100)')
    radio = br.find_element_by_id('robotsRule')
    radio.click()
    button = br.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(15)
    br.quit()
