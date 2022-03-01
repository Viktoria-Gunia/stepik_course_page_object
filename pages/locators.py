from selenium.webdriver.common.by import By

class MainPageLocators():
   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
   LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
   LOGIN_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
   LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
   BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket") 
   PRICE_BEFOR = (By.CSS_SELECTOR, "p.price_color")
   IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
   NAME_TOVAR = (By.XPATH, "//h1")
   
 