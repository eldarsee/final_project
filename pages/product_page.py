from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators
from time import sleep


class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*CartPageLocators.CART).click()
        self.solve_quiz_and_get_code()
        self.cart_price_should_be_equal_to_product_price()
        self.product_names_should_be_the_same()

    def cart_price_should_be_equal_to_product_price(self):   
        assert self.browser.find_element(*CartPageLocators.PRICE_FIELD_START).text in \
        self.browser.find_element(*CartPageLocators.PRICE_FIELD).text, \
        'prices are different'
        
    def product_names_should_be_the_same(self):
        assert self.browser.find_element(*CartPageLocators.PRODUCT_FIELD_START).text == \
        self.browser.find_element(*CartPageLocators.PRODUCT_FIELD).text, \
        'product names are different'
