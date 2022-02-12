from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket isn't empty"
        
    def basket_text_should_contain_appropriate_text(self):    
        assert 'empty' in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, \
            "There is no text that basket is empty"
