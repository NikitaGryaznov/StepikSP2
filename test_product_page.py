from .pages.product_page import ProductPage
import pytest
import time

#pytest -s -v -k test_guest_can_add_product_to_basket
# pytest -rX -v -k test_guest_can_add_product_to_basket
#1 "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#2 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."


"""
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(1)
"""


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    page.equal_product_name()
    time.sleep(1)
