from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    br = webdriver.Chrome()
    br.get(link)

    file = os.path.abspath('empty.txt')

    fn = br.find_element_by_name('firstname')
    ln = br.find_element_by_name('lastname')
    em = br.find_element_by_name('email')
    ch = br.find_element_by_id('file')
    button = br.find_element_by_css_selector('button.btn')

    fn.send_keys('Alex')
    ln.send_keys('B')
    em.send_keys('qwerty@gmail.com')
    ch.send_keys(file)
    button.click()

finally:
    time.sleep(15)
    br.quit()

# print(os.path.abspath('empty.txt'))
# print(os.path.abspath(os.path.dirname(__file__)))