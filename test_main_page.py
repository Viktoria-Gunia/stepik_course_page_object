import pytest
from .pages.product_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.smoke
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage(browser, link)   
    page.open()                     
    page.should_be_login_url()        

@pytest.mark.smoke    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)   
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_text_basket()
# pytest -v --tb=line --language=en  -m smoke test_main_page.py

                      