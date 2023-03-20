import pytest

from pages.scroll_up_page import ScrollUp
from utils.test_data import Data


class TestScrollUp:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.scrlUp = ScrollUp(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.scrlUp.check_page_loaded()
        self.scrlUp.scroll_to_footer()
        self.scrlUp.verify_subscription_visible(Data.subscription)
        self.scrlUp.scroll_to_header()
        self.scrlUp.verify_header_txt_visible(Data.headerText)
