import pytest

from pages.pl_ord_login_before_check_page import PlaceOrderLoginBeforeCheckout
from pages.register_page import Register
from pages.login_valid_page import LoginValidCred
from utils.test_data import Data
from utils.tools import take_screenshot


class TestPlaceOrderLoginBeforeCheckout:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.logBeforeCheckout = PlaceOrderLoginBeforeCheckout(self.page)
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

    def test_place_ord_login_before_check(self, test_setup):
        self.logBeforeCheckout.check_page_loaded()
        self.reg.submit_login_btn_click()
        # login form
        self.log.submit_login_btn_click()
        self.log.login_text_visible()
        self.log.set_email(Data.fakeEmail)
        self.log.set_password(Data.fakePassword)
        self.log.login_btn_click()
        self.log.logged_as_visible(Data.fakeUser)

        # add to cart
        self.logBeforeCheckout.hover_product_1()
        self.logBeforeCheckout.add_first_product()
        self.logBeforeCheckout.click_continue_shopping()
        self.logBeforeCheckout.hover_product_2()
        self.logBeforeCheckout.add_second_product()
        self.logBeforeCheckout.click_continue_shopping()
        self.logBeforeCheckout.click_header_cart_btn()
        self.logBeforeCheckout.check_cart_displayed()
        self.logBeforeCheckout.click_proceed_btn()
        # cart

        self.logBeforeCheckout.check_delivery_address(Data.firstName, Data.lastName, Data.company, Data.address1, Data.address2, Data.country, Data.state, Data.city, Data.zipCode, Data.mobileNumber)
        self.logBeforeCheckout.verify_product_1_visible()
        self.logBeforeCheckout.verify_product_2_visible()
        self.logBeforeCheckout.check_product_1_details_info(Data.product1Char[0], Data.product1Char[1], Data.product1Char[2], Data.product1Char[3])
        self.logBeforeCheckout.check_product_2_details_info(Data.product2Char[0], Data.product2Char[1], Data.product2Char[2], Data.product2Char[3])
        self.logBeforeCheckout.add_comment(Data.message)
        self.logBeforeCheckout.click_place_order_btn()
        self.logBeforeCheckout.fill_name_on_card(Data.firstName, Data.lastName)
        self.logBeforeCheckout.fill_card_number(Data.cardNumb)
        self.logBeforeCheckout.fill_cvc(Data.cvc)
        self.logBeforeCheckout.fill_exp_month(Data.monthBirth)
        self.logBeforeCheckout.fill_exp_year(Data.yearExpCard)
        self.logBeforeCheckout.click_pay_btn()
        """self.logBeforeCheckout.success_msg_visible()""" # doesnt work from 17.03.23
        self.page.wait_for_timeout(2000)
        self.logBeforeCheckout.success_msg2_visible()
        self.reg.click_delete_account_btn()
        self.page.wait_for_timeout(2000)
        self.reg.account_deleted_visible()
        self.reg.click_continue_btn()
        take_screenshot(self.page, 'place_ord_login_before_check')
