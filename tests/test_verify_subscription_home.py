import pytest

from pages.verify_subscription_home_page import VerifySubscriptionHomePage
from utils.test_data import Data


class TestSearchProduct:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.verSubscription = VerifySubscriptionHomePage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.verSubscription.check_page_loaded()
        self.verSubscription.scroll_to_arrow()
        self.verSubscription.verify_subscription_txt_visible()
        self.verSubscription.fill_email(Data.fakeEmail)
        self.verSubscription.click_arrow_btn()
        self.verSubscription.verify_success_alert_visible()
