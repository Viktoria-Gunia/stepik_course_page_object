import pytest
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.need_review
class TestNeedReview():
    def test_user_can_add_product_to_basket(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = LoginPage(browser, self.link) 
        page.open()
        page.register_new_user()
        page  = BasePage(browser, self.link)
        page.should_be_authorized_user()
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.should_be_product_url1() 

    def test_guest_can_add_product_to_basket(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.should_be_product_url1() 

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, self.link)   
        page.open()
        page.go_to_basket_page()
        page.should_be_empty_basket()
        page.should_be_empty_text_basket() 

    def test_guest_can_go_to_login_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, self.link)  
        page.open()                      
        page.should_be_login_url()      
# pytest -v --tb=line --language=en -m need_review  test_product_page.py

@pytest.mark.tests_for_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = LoginPage(browser, self.link) 
        page.open()
        page.register_new_user()
        page  = BasePage(browser, self.link)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.see_success_message1()
        
    def test_user_can_add_product_to_basket(self,browser):
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.should_be_product_url1()     
# pytest -v --tb=line --language=en -m tests_for_user  test_product_page.py

@pytest.mark.tests_for_guest
class TestGuest():
    def test_guest_should_see_login_link_on_product_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, self.link)
        page.open()
        page.should_be_login_url()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, self.link)   
        page.open()
        page.go_to_basket_page()
        page.should_be_empty_basket()
        page.should_be_empty_text_basket()

    def test_guest_cant_see_success_message(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.see_success_message()  

    def test_message_disappeared_after_adding_product_to_basket(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.message_disappeared() 

    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_url() 
#pytest -v --tb=line --language=en -m tests_for_guest  test_product_page.py

@pytest.mark.tests_promo
class TestMainPage1():
    
    @pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
    def test_guest_can_add_product_to_basket(self,browser,promo_offer):
        self.link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.should_be_product_url() 

    @pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser,promo_offer):
        self.link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.success_message_after_adding_product_to_basket() 

    @pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
    def test_guest_cant_see_success_message(self,browser,promo_offer):
        self.link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.see_success_message()

    
    @pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
    def test_message_disappeared_with_promo(self,browser,promo_offer):
        self.link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, self.link) 
        page.open()                     
        page.message_disappeared_promo()   
#pytest -rx -v --tb=line --language=en -m tests_promo test_product_page.py

   
