import pytest

from pages.login_incorrect_page import LoginIncorrectCred
from utils.test_data import Data
from utils.tools import take_screenshot


class TestLoginIncorrectCred:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.log = LoginIncorrectCred(self.page)

    def test_login_incorrect(self, test_setup):
        self.log.check_page_loaded()
        self.log.submit_login_btn_click()
        self.log.login_text_visible()
        self.log.set_email(Data.incorrectEmail)
        self.log.set_password(Data.incorrectPassword)
        self.log.login_btn_click()
        self.log.error_msg_visible()
        take_screenshot(self.page, 'login_incorrect')
