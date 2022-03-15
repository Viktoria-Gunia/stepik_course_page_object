import time
from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_url(self):
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "Wrong url:substring 'login' is not present in the current url"

    def should_see_login_url(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN_FORM), "LOGIN_FORM displayed is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "REGISTER_FORM displayed is not presented"

    def register_new_user(self):
        self.go_to_login_page()
        input_email = self.browser.find_element(*LoginPageLocators.USER_REGISTER_EMAIL)
        input_email.send_keys(str(time.time()) + "@fakemail.org")
        input_pass1 = self.browser.find_element(*LoginPageLocators.USER_REGISTER_PASSWORD1)
        my_pass = "fakemail123"
        input_pass1.send_keys(my_pass)
        input_pass2 = self.browser.find_element(*LoginPageLocators.USER_REGISTER_PASSWORD2)
        input_pass2.send_keys(my_pass)
        button = self.browser.find_element(*LoginPageLocators.USER_REGISTER_CLICK)
        button.click()
        

    


        




    