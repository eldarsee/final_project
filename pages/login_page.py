from .base_page import BasePage
from .locators import LoginPageLocators, MainPageLocators
from time import sleep


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "it's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
        'there is no login form on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
        'there is no register form on the page'

    def register_new_user(self, email, password):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PSWD1_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PSWD2_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()
        self.should_be_authorized_user()
