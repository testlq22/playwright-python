import pytest

from pages.verify_subscription_cart_page import VerifySubscriptionCartPage
from utils.test_data import Data


class TestSearchProduct:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.verSubscriptionCart = VerifySubscriptionCartPage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.verSubscriptionCart.check_page_loaded()
        self.verSubscriptionCart.click_cart_btn_header()
        self.verSubscriptionCart.scroll_to_arrow()
        self.page.wait_for_timeout(5000)
        self.verSubscriptionCart.verify_subscription_txt_visible()
        self.verSubscriptionCart.fill_email(Data.fakeEmail)
        self.verSubscriptionCart.click_arrow_btn()
        self.verSubscriptionCart.verify_success_alert_visible()
