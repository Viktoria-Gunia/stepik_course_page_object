from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()
        
    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
#в should_be_login_url проверяем в assert не равена ли строка self.url через find строке login.  (!= -1)        
        self.go_to_login_page()
        assert "login" in self.browser.current_url, "Wrong url:substring 'login' is not present in the current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
               
        assert self.is_element_present(*LoginPageLocators.LOGIN_LOGIN_FORM), "LOGIN_FORM displayed is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
       assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "REGISTER_FORM displayed is not presented"
        