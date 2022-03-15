from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.GUEST_CLICK_BASKET)
        link.click()

    def should_be_empty_basket(self):
       assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY) == False, "Basket is not empty"

    def should_be_empty_text_basket(self):
       assert self.is_element_present(*BasePageLocators.BASKET_IS_TEXT_EMPTY) == True, "Basket is empty, but text:'Your basket is empty.' not found"      