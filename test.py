import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LogInTest(unittest.TestCase):

    
    """Settings buttons and fields"""
    url = 'https://pikabu.ru/'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    user_nick = 'qwertypitec'
    user_password = '89530poneg4,.3'
    e_mail = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')
    main_menu = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div[2]/div[1]/div')
    button_entrance = driver.find_element(By.XPATH, '//*[@id="signin-form"]/div[7]')

    """Positive Test"""
    def test_positive(self):
        self.e_mail.send_keys(self.user_nick)
        self.password.send_keys(self.user_password + Keys.RETURN)
        self.assertEqual(self.driver.find_element(By.CLASS_NAME, 'user__info-item').text, self.user_nick)
        button_exit = self.driver.find_element(By.CLASS_NAME, 'user__info-item user__exit')
        button_exit.click()
        # self.assertIsNotNone(self.driver.find_element(By.ID, 'rc-imageselect'), 'Capcha')

    """Negative Tests"""
    def test_wrong_fields(self):
        self.e_mail.send_keys("wrong_name")
        self.password.send_keys("wrong_password" + Keys.RETURN)
        self.assertIsNotNone(self.driver.find_element(By.CLASS_NAME, 'auth__error'))

    def test_empty_fields(self):
        self.button_entrance.click()
        self.assertIsNotNone(self.driver.find_element(By.CLASS_NAME, 'popup__hint'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()

