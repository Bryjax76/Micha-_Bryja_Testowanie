from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest


class TestWebDriver(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'C:\228413\przypomnienie\Test_Django_3\chromedriver.exe')
        
    def test_todoList(self):
        self.browser.get('http://127.0.0.1:8080/')
        assert 'To-Do Lists' in self.browser.title
        self.header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('LIST', self.header_text)
        
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Gotowanie')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(rows, '1. Gotowanie')
        
    def tearDown(self):
        self.browser.quit()
        
if __name__ == '__main__':
    unittest.main()