import time
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_url(self):
        self.should_be_btn_add()
        self.click_btn_add()
        self.should_be_correct_adding_product_price()

    def should_be_btn_add(self):
       assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'add to basket' displayed is not presented"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(*ProductPageLocators.PRICE_BEFOR)
        in_basket = self.browser.find_elements(*ProductPageLocators.IN_BASKET)
        product_price = in_basket[2]
        assert product_price.text == message_basket_total.text, "Цены не равны"
        name_book = self.browser.find_element(*ProductPageLocators.NAME_TOVAR)
        name_book_in_basket = in_basket[0]
        print('name_book_in_basket',name_book_in_basket.text)
        assert name_book.text == name_book_in_basket.text, "Названия не одинаковые"
        
    def click_btn_add(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()
        
        
        
       
        
       
       
       
    