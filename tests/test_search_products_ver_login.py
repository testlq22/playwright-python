import pytest

from pages.search_products_ver_login_page import SearchProductsVerifyAfterLogin
from pages.register_page import Register
from pages.login_valid_page import LoginValidCred
from utils.test_data import Data
from utils.tools import take_screenshot


class TestSearchProductsVerifyAfterLogin:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.searchVerifyAfterLogin = SearchProductsVerifyAfterLogin(self.page)
        self.reg = Register(self.page)
        self.log = LoginValidCred(self.page)

        self.reg.submit_login_btn_click()
        self.reg.set_username(Data.fakeUser)
        self.reg.set_email(Data.fakeEmail)
        self.reg.signup_btn_click()
        self.reg.select_mr()
        self.reg.set_password(Data.fakePassword)
        self.reg.select_day(Data.dayBirth)
        self.reg.select_month(Data.monthBirth)
        self.reg.select_year(Data.yearBirth)
        self.reg.select_newsletter_checkbox()
        self.reg.select_special_offers_checkbox()
        self.reg.set_first_name(Data.firstName)
        self.reg.set_last_name(Data.lastName)
        self.reg.set_company(Data.company)
        self.reg.set_address_1(Data.address1)
        self.reg.set_address_2(Data.address2)
        self.reg.select_country(Data.country)
        self.reg.set_state(Data.state)
        self.reg.set_city(Data.city)
        self.reg.set_zip_code(Data.zipCode)
        self.reg.set_mobile_number(Data.mobileNumber)
        self.reg.click_create_account_btn()
        self.reg.click_continue_btn()
        self.reg.click_logout_btn()
        self.reg.click_logo()
        yield
        self.log.click_delete_account_btn()

    def test_search_products_ver_after_login(self, test_setup):
        self.searchVerifyAfterLogin.check_page_loaded()
        self.searchVerifyAfterLogin.products_btn_click()
        self.searchVerifyAfterLogin.verify_products_page()
        self.searchVerifyAfterLogin.verify_products_txt_visible(Data.allProd)
        self.searchVerifyAfterLogin.search_product(Data.someProduct)
        self.searchVerifyAfterLogin.verify_searched_products_visible()
        self.searchVerifyAfterLogin.hover_product_1()
        self.searchVerifyAfterLogin.add_first_product()
        self.searchVerifyAfterLogin.click_continue_shopping()
        self.searchVerifyAfterLogin.hover_product_2()
        self.searchVerifyAfterLogin.add_second_product()
        self.searchVerifyAfterLogin.click_continue_shopping()
        self.searchVerifyAfterLogin.hover_product_3()
        self.searchVerifyAfterLogin.add_third_product()
        self.searchVerifyAfterLogin.click_continue_shopping()
        self.searchVerifyAfterLogin.click_cart_button()
        self.searchVerifyAfterLogin.verify_product_1_visible()
        self.searchVerifyAfterLogin.verify_product_2_visible()
        self.searchVerifyAfterLogin.verify_product_3_visible()
        self.searchVerifyAfterLogin.login_submit_btn_click()
        self.log.set_email(Data.fakeEmail)
        self.log.set_password(Data.fakePassword)
        self.log.login_btn_click()
        self.searchVerifyAfterLogin.click_cart_button()
        self.searchVerifyAfterLogin.verify_product_1_visible()
        self.searchVerifyAfterLogin.verify_product_2_visible()
        self.searchVerifyAfterLogin.verify_product_3_visible()
        take_screenshot(self.page, 'add_products')
