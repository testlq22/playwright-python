import pytest

from pages.register_page import Register
from utils.test_data import Data


class TestRegister:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.reg = Register(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_check_page(self, test_setup):
        self.reg.check_page_loaded()

    def test_click_login_button(self, test_setup):
        self.reg.submit_login_btn_click()
        self.reg.signup_text_visible()
        self.reg.set_username(Data.fakeUser)
        self.reg.set_email(Data.fakeEmail)
        self.reg.signup_btn_click()
        self.reg.first_title_visible()
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
        self.reg.click_delete_account_btn()
        self.reg.account_deleted_visible()
        self.reg.click_continue_btn()
