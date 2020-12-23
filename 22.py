from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('http://suninjuly.github.io/wait1.html')
    browser.find_element_by_id("verify").click()

    assert 'successful' in browser.find_element_by_id("verify_message")

finally:
    time.sleep(10)
    browser.quit()
