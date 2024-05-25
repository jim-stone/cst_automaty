from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils import AbstractBasePage
from selenium import webdriver
from typing import Type


class LoginPage(AbstractBasePage):
    input_login = (By.CSS_SELECTOR, '#login')
    input_password = (By.CSS_SELECTOR, '#password')
    button_login = (By.CSS_SELECTOR, '[type=submit]')

    def __init__(self, browser: webdriver, url):
        super().__init__(browser)
        self.url = url

    def open(self):
        self.browser.get(self.url)
        return self

    def login(self, login, password):
        self.wait.until(
            EC.all_of(
                EC.visibility_of_element_located(self.input_login),
                EC.visibility_of_element_located(self.input_password),
                EC.visibility_of_element_located(self.button_login),
            )
        )
        self.browser.find_element(*self.input_login).send_keys(login)
        self.browser.find_element(*self.input_password).send_keys(password)
        self.browser.find_element(*self.button_login).click()


class AppsPage(AbstractBasePage):
    list_where_logged_user_is_present = (By.CSS_SELECTOR, 'div.v-list__tile__title[data-v-05eb544e]')
    buttons_apps = (By.CSS_SELECTOR, '.v-sheet--tile')

    def get_user(self):
        self.wait.until(EC.presence_of_all_elements_located(self.list_where_logged_user_is_0))
        elements = self.browser.find_elements(*self.list_where_logged_user_is_present)
        return [e.get_attribute('textContent') for e in elements]

    def login_adm(self):
        self.wait.until(EC.presence_of_all_elements_located(self.buttons_apps))
        elements = self.browser.find_elements(*self.buttons_apps)
        print([e.get_attribute('textContent') for e in elements])