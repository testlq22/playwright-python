import pytest

from pages.verify_address_in_check_page import VerifyAddressInCheckout
from pages.register_page import Register
from utils.test_data import Data


class TestVerifyAddressInCheckout:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.verifyAddrInCheckout = VerifyAddressInCheckout(self.page)
        self.reg = Register(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.verifyAddrInCheckout.check_page_loaded()
        self.reg.submit_login_btn_click()
        # register form
        self.reg.set_username(Data.fakeUser)
        self.reg.set_email(Data.fakeEmail)
        self.reg.signup_btn_click()
        # register form full
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
        self.reg.account_confirmation_visible()
        self.reg.click_continue_btn()
        self.reg.logged_as_visible(Data.fakeUser)
        # add to cart
        self.verifyAddrInCheckout.hover_product_1()
        self.verifyAddrInCheckout.add_first_product()
        self.verifyAddrInCheckout.click_continue_shopping()
        self.verifyAddrInCheckout.hover_product_2()
        self.verifyAddrInCheckout.add_second_product()
        self.verifyAddrInCheckout.click_continue_shopping()
        self.verifyAddrInCheckout.click_header_cart_btn()
        self.verifyAddrInCheckout.check_cart_displayed()
        self.verifyAddrInCheckout.click_proceed_btn()
        # cart
        self.verifyAddrInCheckout.check_delivery_address(Data.firstName, Data.lastName, Data.company, Data.address1,
                                                         Data.address2, Data.country, Data.state, Data.city,
                                                         Data.zipCode, Data.mobileNumber)
        self.verifyAddrInCheckout.check_billing_address(Data.firstName, Data.lastName, Data.company, Data.address1,
                                                         Data.address2, Data.country, Data.state, Data.city,
                                                         Data.zipCode, Data.mobileNumber)
        self.reg.click_delete_account_btn()
        self.reg.account_deleted_visible()
        self.reg.click_continue_btn()
