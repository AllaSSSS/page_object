import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                          message=f"Can't find element by locator {locator}")
        except Exception as e:
            logging.exception("Find element exception: {e}")
            element = None
        return element


    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Property {property} not found in element with locator {locator}')
            return None

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while opening site')
            start_browsing = None
        return start_browsing

    def get_alert_txt(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Alert exception')
            return None

        #alert.accept()
        #return msg
