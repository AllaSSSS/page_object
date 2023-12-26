import yaml
from pagetest import OperationsHelper
import logging
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_error_text(browser):
    # Получение ошибки при вводе неверных пользовательских данных
    logging.info("Starting test")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == '401'


def test_login_positive(browser):
    # Вход в систему с правильным логином и паролем
    logging.info('Starting test_login_positive')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.login_success() == f'Hello, {testdata["login"]}'


def test_about_option(browser):
    # Проверка раздела About
    logging.info('Starting test_about_option')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_about_button()
    time.sleep(3)
    assert testpage.check_title_size() == '32px'


# def test_contact_us(browser):
#     logging.info('Test add_post Starting')
#     testpage = OperationsHelper(browser)
#     testpage.go_to_site()
#     testpage.enter_login(testdata['login'])
#     testpage.enter_pass(testdata['password'])
#     testpage.click_login_button()
#     testpage.click_contact_button()
#     testpage.add_name(testdata['u_name'])
#     testpage.add_email(testdata['u_email'])
#     testpage.add_contact_content(testdata['content_field'])
#     testpage.click_contact_us_button()
#     assert testpage.get_alert_message() == 'Form successfully submitted', 'test contact us FAILED!'


