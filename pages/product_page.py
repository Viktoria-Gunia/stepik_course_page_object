import pytest
import time
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import LoginPageLocators

class ProductPage(BasePage):
    
    def should_be_product_url(self):
        self.should_be_btn_add()
        self.click_btn_add()
        self.should_be_correct_adding_product_price()

    def should_be_product_url1(self):
        self.should_be_btn_add()
        self.click_btn_add_one_solve_quiz_and_get_code()
        self.should_be_correct_adding_product_price()   
        
    def success_message_after_adding_product_to_basket(self):
        self.should_be_btn_add()
        self.click_btn_add()
        self.should_not_be_success_message()

    def see_success_message(self):
        self.should_be_btn_add()
        self.click_btn_add_one_solve_quiz_and_get_code()
        self.should_not_be_success_message()

    def see_success_message1(self):
        self.should_be_btn_add()
        self.should_not_be_success_message()

    def message_disappeared(self):
        self.should_be_btn_add()
        self.click_btn_add_one_solve_quiz_and_get_code()
        time.sleep(1)
        self.is_disappeared1()

    def message_disappeared_promo(self):
        self.should_be_btn_add()
        self.click_btn_add()
        time.sleep(1)
        self.is_disappeared1()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

   
    def is_disappeared1(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should be"  
        
    def go_to_login_page_invalid(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK_INVALID), "LOGIN link is not presented"

   
    @pytest.mark.xfail(reason="fixing this bug right now")
    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(*ProductPageLocators.PRICE_BEFOR)
        in_basket = self.browser.find_elements(*ProductPageLocators.IN_BASKET)
        product_price = in_basket[2]
        assert product_price.text == message_basket_total.text, "Цены не равны" + self.link
        name_book = self.browser.find_element(*ProductPageLocators.NAME_TOVAR)
        name_book_in_basket = in_basket[0]
        print('name_book_in_basket',name_book_in_basket.text)
        assert name_book.text == name_book_in_basket.text, "Названия не одинаковые:" + self.link
        
    def click_btn_add(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()
        self.solve_quiz_and_get_code()

    def click_btn_add_one_solve_quiz_and_get_code(self):
        link = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        link.click()
        

    def should_be_btn_add(self):
       assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'add to basket' displayed is not presented"

    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        link.click()
           
    def should_be_login_url(self):
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "Wrong url:substring 'login' is not present in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN_FORM), "LOGIN_FORM displayed is not presented"
    
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "REGISTER_FORM displayed is not presented"
    