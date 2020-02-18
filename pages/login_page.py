from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = LoginPage(browser, browser.current_url)
        assert login_url.should_be_login_page(), "Не тот урл"
        # реализуйте проверку на корректный url адрес
        #assert True

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма логина"
        # реализуйте проверку, что есть форма логина
        #assert True

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Отсутствует форма регистрации"
        # реализуйте проверку, что есть форма регистрации на странице
        #assert True