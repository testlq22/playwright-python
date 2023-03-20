import pytest

from pages.pl_ord_reg_while_check_page import PlaceOrderRegWhileCheckout
from pages.register_page import Register
from utils.test_data import Data


class TestVerifyTestCases:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.regWhileCheckout = PlaceOrderRegWhileCheckout(self.page)
        self.reg = Register(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.regWhileCheckout.check_page_loaded()
        self.regWhileCheckout.hover_product_1()
        self.regWhileCheckout.add_first_product()
        self.regWhileCheckout.click_continue_shopping()
        self.regWhileCheckout.hover_product_2()
        self.regWhileCheckout.add_second_product()
        self.regWhileCheckout.click_continue_shopping()
        self.regWhileCheckout.click_header_cart_btn()
        self.regWhileCheckout.check_cart_displayed()
        self.regWhileCheckout.click_proceed_btn()
        self.regWhileCheckout.click_register_login_btn()
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
        # cart
        self.regWhileCheckout.click_header_cart_btn()
        self.regWhileCheckout.click_proceed_btn()
        self.regWhileCheckout.check_delivery_address(Data.firstName, Data.lastName, Data.company, Data.address1, Data.address2, Data.country, Data.state, Data.city, Data.zipCode, Data.mobileNumber)
        self.regWhileCheckout.verify_product_1_visible()
        self.regWhileCheckout.verify_product_2_visible()
        self.regWhileCheckout.check_product_1_details_info(Data.product1Char[0], Data.product1Char[1], Data.product1Char[2], Data.product1Char[3])
        self.regWhileCheckout.check_product_2_details_info(Data.product2Char[0], Data.product2Char[1], Data.product2Char[2], Data.product2Char[3])
        self.regWhileCheckout.add_comment(Data.message)
        self.regWhileCheckout.click_place_order_btn()
        self.regWhileCheckout.fill_name_on_card(Data.firstName, Data.lastName)
        self.regWhileCheckout.fill_card_number(Data.cardNumb)
        self.regWhileCheckout.fill_cvc(Data.cvc)
        self.regWhileCheckout.fill_exp_month(Data.monthBirth)
        self.regWhileCheckout.fill_exp_year(Data.yearExpCard)
        self.regWhileCheckout.click_pay_btn()
        """self.regWhileCheckout.success_msg_visible()""" # doesnt work from 17.03.23
        self.page.wait_for_timeout(2000)
        self.regWhileCheckout.success_msg2_visible()
        self.reg.click_delete_account_btn()
        self.page.wait_for_timeout(2000)
        self.reg.account_deleted_visible()
        self.reg.click_continue_btn()
