from selenium.webdriver.common.by import By

class MainPageLocators():
   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
   GUEST_CLICK_BASKET =(By.XPATH, "//a[@href='/en-gb/basket/']")
   BASKET_IS_EMPTY =(By.CSS_SELECTOR, "h2.col-sm-6.h3")
   BASKET_IS_TEXT_EMPTY = (By.XPATH,"//*[@id='content_inner']//*[contains(text(),'Your basket is empty.')]")

class LoginPageLocators():
   LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
   LOGIN_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
   LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
   LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductPageLocators():
   BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket") 
   PRICE_BEFOR = (By.CSS_SELECTOR, "p.price_color")
   IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
   NAME_TOVAR = (By.XPATH, "//h1")
   SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
   
 