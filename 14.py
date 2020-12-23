from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input")
    fn.send_keys('Alex')
    ln = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input")
    ln.send_keys('B')
    em = browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input")
    em.send_keys('qwerty@gmail.com')
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    welcome_text = browser.find_element_by_tag_name("h1").text

    assert 'Congratulations! You have successfully registered!' == welcome_text

finally:
    time.sleep(10)
    browser.quit()

