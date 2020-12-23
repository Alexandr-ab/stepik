from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects2.html'
    br = webdriver.Chrome()
    br.get(link)
    a = br.find_element_by_id('num1').text
    b = br.find_element_by_id('num2').text
    c = int(a) + int(b)
    sel = Select(br.find_element_by_id('dropdown'))
    sel.select_by_value(str(c))
    button = br.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(15)
    br.quit()
