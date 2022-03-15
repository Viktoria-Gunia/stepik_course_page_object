from selenium.webdriver.common.by import By

class BasePageLocators():
   USER_ICON = (By.CSS_SELECTOR, ".icon-user")
   USER_REGISTRATION_EMAIL = (By.XPATH,  "//input[@name='login-email']")
   USER_REGISTRATION_PASSWORD = (By.XPATH,  "//input[@name='registration-password1']")
   USER_EMAIL = (By.XPATH,  "//input[@name='login-username']")
   USER_PASSWORD = (By.XPATH,  "//input[@name='login-password']")
   LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
   GUEST_CLICK_BASKET =(By.XPATH, "//a[@href='/en-gb/basket/']")
   BASKET_IS_EMPTY =(By.CSS_SELECTOR, "h2.col-sm-6.h3")
   BASKET_IS_TEXT_EMPTY = (By.XPATH,"//*[@id='content_inner']//*[contains(text(),'Your basket is empty.')]")
  
class LoginPageLocators():
   LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
   LOGIN_LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
   LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
   USER_REGISTER_EMAIL = (By.CSS_SELECTOR,"#id_registration-email")
   USER_REGISTER_PASSWORD1 = (By.CSS_SELECTOR,"#id_registration-password1")
   USER_REGISTER_PASSWORD2 = (By.CSS_SELECTOR,"#id_registration-password2")
   USER_REGISTER_CLICK = (By.XPATH, "//button[@name='registration_submit']")
   USER_LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
   USER_LOGIN_PASSWORD = (By.CSS_SELECTOR,"#id_login-password")
   USER_LOGIN_CLICK = (By.XPATH, "//button[@name='login_submit']")

   

class ProductPageLocators():
   BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-add-to-basket") 
   PRICE_BEFOR = (By.CSS_SELECTOR, "p.price_color")
   IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
   NAME_TOVAR = (By.XPATH, "//h1")
   SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner p")
   
 