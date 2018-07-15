from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)                                      #драйвер ожидает загрузки элементов до 10 секунд
driver.get('http://www.mail.ru')                                #перейти на страницу mail.ru

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

driver.find_element_by_id('mailbox:submit').click()
#найти кнопку "войти" и нажать ее

driver.find_elements_by_xpath("//*[contains(text(), 'test_python_malakhova@mail.ru')]")
#если есть поле с логином - аввторизация прошла успешно

print('Авторизация прошла успешно')

driver.find_element_by_id('PH_logoutLink').click()              #выход из учетной записи

driver.quit()                                                   #выход из браузера