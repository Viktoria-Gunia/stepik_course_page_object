import pytest
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)   
        page.open()                     
        page.should_be_login_url()        


    def test_guest_should_see_login_link(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_see_login_url()  

#pytest -v --tb=line --language=en  -m login_guest test_main_page.py       

                    