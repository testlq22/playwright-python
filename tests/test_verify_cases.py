import pytest

from pages.verify_cases_page import VerifyTestCases
from utils.tools import take_screenshot


class TestVerifyTestCases:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.ver = VerifyTestCases(self.page)

    def test_verify_test_cases(self, test_setup):
        self.ver.check_page_loaded()
        self.ver.test_cases_btn_click()
        self.ver.check_test_cases_page_loaded()
        take_screenshot(self.page, 'verify_test_cases')
