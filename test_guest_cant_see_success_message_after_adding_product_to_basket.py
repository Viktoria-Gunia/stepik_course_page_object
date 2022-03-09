import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(link)
    page = ProductPage(browser, link) 
    page.open()                     
    page.success_message_after_adding_product_to_basket()        

#элемент не появляется на странице в течение заданного времени    
@pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
def test_guest_cant_see_success_message(browser,promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(link)
    page = ProductPage(browser, link) 
    page.open()                     
    page.see_success_message()

# проверить, что какой-то элемент исчезает
@pytest.mark.parametrize('promo_offer', ["0","1", "2","3", "4", "5", "6", "7", "8", "9"])
def message_disappeared(browser,promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(link)
    page = ProductPage(browser, link) 
    page.open()                     
    page.message_disappeared() 

    # pytest -rx -v test_guest_cant_see_success_message_after_adding_product_to_basket.py
      

  
