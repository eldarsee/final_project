from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from time import sleep


class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*ProductPageLocators.CART).click()
        # self.solve_quiz_and_get_code()
        # self.cart_price_should_be_equal_to_product_price()
        # self.product_names_should_be_the_same()
        self.should_not_be_success_message()

    def cart_price_should_be_equal_to_product_price(self):   
        assert self.browser.find_element(*ProductPageLocators.PRICE_FIELD_START).text in \
        self.browser.find_element(*ProductPageLocators.PRICE_FIELD).text, \
        'prices are different'
        
    def product_names_should_be_the_same(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_FIELD_START).text == \
        self.browser.find_element(*ProductPageLocators.PRODUCT_FIELD).text, \
        'product names are different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        self.browser.find_element(*ProductPageLocators.CART).click()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message isn't disappeared, but should be"
