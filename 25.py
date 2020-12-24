from selenium import webdriver
import time
import unittest

class TestReg(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys('Alex')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys('B')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys('qwerty@gmail.com')

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(5)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Text should be the same')

    def test_reg2(self):
        browser = self.browser
        browser.get('http://suninjuly.github.io/registration2.html')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group first_class']/input").send_keys('Alex')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group second_class']/input").send_keys('B')
        browser.find_element_by_xpath("//div[@class='first_block']/div[@class='form-group third_class']/input").send_keys('qwerty@gmail.com')

        browser.find_element_by_css_selector("button.btn").click()
        time.sleep(5)
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'Text should be the same')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main


