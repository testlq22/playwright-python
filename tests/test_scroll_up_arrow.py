import pytest

from pages.scroll_up_arrow_page import ScrollUpArrow
from utils.test_data import Data


class TestScrollUpArrow:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.scrlUpArrow = ScrollUpArrow(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.scrlUpArrow.check_page_loaded()
        self.scrlUpArrow.scroll_to_footer()
        self.scrlUpArrow.verify_subscription_visible(Data.subscription)
        self.scrlUpArrow.arrow_up_btn_click()
        self.scrlUpArrow.verify_header_txt_visible(Data.headerText)


