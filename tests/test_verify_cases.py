import pytest

from pages.verify_cases_page import VerifyTestCases


class TestVerifyTestCases:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.ver = VerifyTestCases(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_test_cases(self, test_setup):
        self.ver.check_page_loaded()
        self.ver.test_cases_btn_click()
        self.ver.check_test_cases_page_loaded()
