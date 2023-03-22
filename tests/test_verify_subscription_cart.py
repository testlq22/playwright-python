import pytest

from pages.verify_subscription_cart_page import VerifySubscriptionCartPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestVerifySubscriptionCartPage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.verSubscriptionCart = VerifySubscriptionCartPage(self.page)

    def test_verify_subscription_cart_page(self, test_setup):
        self.verSubscriptionCart.check_page_loaded()
        self.verSubscriptionCart.click_cart_btn_header()
        self.verSubscriptionCart.scroll_to_arrow()
        self.page.wait_for_timeout(5000)
        self.verSubscriptionCart.verify_subscription_txt_visible()
        self.verSubscriptionCart.fill_email(Data.fakeEmail)
        self.verSubscriptionCart.click_arrow_btn()
        self.verSubscriptionCart.verify_success_alert_visible()
        take_screenshot(self.page, 'verify_subscription_cart_page')
