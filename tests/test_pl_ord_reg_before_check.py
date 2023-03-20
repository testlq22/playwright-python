import pytest

from pages.pl_ord_reg_before_check_page import PlaceOrderRegBeforeCheckout
from pages.register_page import Register
from utils.test_data import Data


class TestPlaceOrderRegBeforeCheckout:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.regBeforeCheckout = PlaceOrderRegBeforeCheckout(self.page)
        self.reg = Register(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.regBeforeCheckout.check_page_loaded()
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
        self.regBeforeCheckout.hover_product_1()
        self.regBeforeCheckout.add_first_product()
        self.regBeforeCheckout.click_continue_shopping()
        self.regBeforeCheckout.hover_product_2()
        self.regBeforeCheckout.add_second_product()
        self.regBeforeCheckout.click_continue_shopping()
        self.regBeforeCheckout.click_header_cart_btn()
        self.regBeforeCheckout.check_cart_displayed()
        self.regBeforeCheckout.click_proceed_btn()
        # cart
        """self.regBeforeCheckout.click_header_cart_btn()
        self.regBeforeCheckout.click_proceed_btn()"""
        self.regBeforeCheckout.check_delivery_address(Data.firstName, Data.lastName, Data.company, Data.address1, Data.address2, Data.country, Data.state, Data.city, Data.zipCode, Data.mobileNumber)
        self.regBeforeCheckout.verify_product_1_visible()
        self.regBeforeCheckout.verify_product_2_visible()
        self.regBeforeCheckout.check_product_1_details_info(Data.product1Char[0], Data.product1Char[1], Data.product1Char[2], Data.product1Char[3])
        self.regBeforeCheckout.check_product_2_details_info(Data.product2Char[0], Data.product2Char[1], Data.product2Char[2], Data.product2Char[3])
        self.regBeforeCheckout.add_comment(Data.message)
        self.regBeforeCheckout.click_place_order_btn()
        self.regBeforeCheckout.fill_name_on_card(Data.firstName, Data.lastName)
        self.regBeforeCheckout.fill_card_number(Data.cardNumb)
        self.regBeforeCheckout.fill_cvc(Data.cvc)
        self.regBeforeCheckout.fill_exp_month(Data.monthBirth)
        self.regBeforeCheckout.fill_exp_year(Data.yearExpCard)

        self.regBeforeCheckout.click_pay_btn()

        """self.regBeforeCheckout.success_msg_visible()""" # doesnt work from 17.03.23
        self.page.wait_for_timeout(2000)
        self.regBeforeCheckout.success_msg2_visible()
        self.reg.click_delete_account_btn()
        self.reg.account_deleted_visible()
        self.reg.click_continue_btn()
