import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestSearch(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
    def testLogin(self):
        driver = self.driver
        driver.implicitly_wait(10)                                      #драйвер ожидает загрузки элементов до 10 секунд
        driver.get('http://mail.ru/')                                   #перейти на страницу mail.ru
        input_login = driver.find_element_by_id('mailbox:login')        #найти поле логин

        input_login.send_keys('test_python_malakhova')                  #ввести логин
        mailbox_domain = driver.find_element_by_id('mailbox:domain')    #выбор домена mail.ru из выпадающего списка
        select = Select(mailbox_domain)
        select.select_by_visible_text('@mail.ru')
        input_password = driver.find_element_by_id('mailbox:password')  #найти поле пароль
        input_password.send_keys('test89313672606')                     #ввести пароль
        check_box = driver.find_element_by_id('mailbox:saveauth')       #найти чекбокс запомнить
        if check_box.is_selected():                                     #если чекбокс активен
            check_box.click()                                           #деактивировать
        driver.find_element_by_id('mailbox:submit').click()             #найти кнопку "войти" и нажать ее

        search_box = driver.find_element_by_css_selector('#portal-menu__search__form > span.js-submit.pm-toolbar__search__button.pm-toolbar__search__button_not-expandable.pm-toolbar__search__button_not-adaptive > button')
        #Найти неактивное поле "Поиск"
        search_box.click()                                              #Кликнуть по неактивному полю "Поиск"

        search_box_hilight = driver.find_element_by_id('portal-menu__search')
        #Найти увеличившееся поле "Поиск"
        search_box_hilight.click()                                      #Кликнуть по увеличевшемуся полю "Поиск"
        element = WebDriverWait(driver, 10).until(                      #Ожидание появления нового локатора и его поиск
            EC.visibility_of_element_located((By.NAME, "blank"))
        )
        element.send_keys('супервозможностях')                          #Ввод в поле "Поиск" значения "супервозможностях"

        element.send_keys(Keys.ENTER)                                   #Нажать клавишу Enter

        results = WebDriverWait(driver, 20).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//*[contains(text(), 'супервозможностях')]"))
        )
        #Ожидание появления новых элементов с результатами поиска

        print(results)                                                  #Напечатать результаты поиска
        amount = len(results)                                           #Посчитать количество результатов
        print('Количество упоминаний')                                  #Печать 'Количество упоминаний'
        print(amount)                                                   #Печать количество результатов

        driver.find_element_by_id('PH_logoutLink').click()              #выход из учетной записи

    def tearDown(self):
        self.driver.quit()                                              #выход из браузера

if __name__ == '__main__':
	unittest.main()
