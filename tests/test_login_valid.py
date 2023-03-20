import pytest

from pages.login_valid_page import LoginValidCred
from pages.register_page import Register
from utils.test_data import Data


class TestLogin:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.log = LoginValidCred(self.page)
        self.reg = Register(self.page)

        self.page.goto('https://automationexercise.com/')
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
        '''self.page.goto('https://automationexercise.com/')'''

    def test_click_login_button(self, test_setup):
        self.log.check_page_loaded()
        self.log.submit_login_btn_click()
        self.log.login_text_visible()
        self.log.set_email(Data.fakeEmail)
        self.log.set_password(Data.fakePassword)
        self.log.login_btn_click()
        self.log.logged_as_visible(Data.fakeUser)
        self.log.click_delete_account_btn()
        self.log.account_deleted_visible()

