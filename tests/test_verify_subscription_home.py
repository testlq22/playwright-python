import pytest

from pages.verify_subscription_home_page import VerifySubscriptionHomePage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestVerifySubscriptionHomePage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.verSubscription = VerifySubscriptionHomePage(self.page)

    def test_verify_subscription_home_page(self, test_setup):
        self.verSubscription.check_page_loaded()
        self.verSubscription.scroll_to_arrow()
        self.verSubscription.verify_subscription_txt_visible()
        self.verSubscription.fill_email(Data.fakeEmail)
        self.verSubscription.click_arrow_btn()
        self.verSubscription.verify_success_alert_visible()
        take_screenshot(self.page, 'verify_subscription_home_page')
