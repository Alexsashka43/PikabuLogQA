from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


url = 'https://pikabu.ru/'
user_nick = 'qwertypitec'
user_password = '89530poneg4,.3'
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(30)


e_mail = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
main_menu = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div[2]/div[1]/div')
button = driver.find_element(By.XPATH, '//*[@id="signin-form"]/div[7]')


"""Позитивный тест"""
def positive_test():
    e_mail.send_keys(user_nick)
    password.send_keys(user_password + Keys.RETURN)
    captcha = driver.find_element(By.ID, 'rc-imageselect')
    try:
        user_nick_in_log = driver.find_element(By.LINK_TEXT, user_nick)
        assert user_nick_in_log.text == user_nick, ''
    except Exception:
        print('Show captcha')
    try:
        captcha = driver.find_element(By.ID, 'rc-imageselect')
        assert captcha
    except Exception:
        print('log in')


"""Негативные тесты"""
def negative_test_wrong_field():
    e_mail.send_keys("wrong_name")
    password.send_keys("wrong_password" + Keys.RETURN)
    assert driver.find_element(By.CLASS_NAME, 'auth__error'), 'Log in'
    main_menu.click()

def negative_test_empty_field():
    button.click()
    assert driver.find_element(By.CLASS_NAME, 'popup__hint')
    main_menu.click()


"""Выход из кабинета"""
def exit_log():
    button_exit_first_step = driver.find_element(By.CLASS_NAME, 'user__info-item user__exit' + Keys.RETURN)
    button_exit_second_step = driver.find_element(By.CLASS_NAME, 'button button_danger' + Keys.RETURN)

# negative_test_wrong_field()
negative_test_empty_field()
# positive_test()
# exit_log()

driver.close()
