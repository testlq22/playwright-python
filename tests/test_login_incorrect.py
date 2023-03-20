import pytest

from pages.login_incorrect_page import LoginIncorrectCred
from utils.test_data import Data


class TestLogin:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.log = LoginIncorrectCred(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_click_login_button(self, test_setup):
        self.log.check_page_loaded()
        self.log.submit_login_btn_click()
        self.log.login_text_visible()
        self.log.set_email(Data.incorrectEmail)
        self.log.set_password(Data.incorrectPassword)
        self.log.login_btn_click()
        self.log.error_msg_visible()
