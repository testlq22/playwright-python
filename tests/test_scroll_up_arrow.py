import pytest

from pages.scroll_up_arrow_page import ScrollUpArrow
from utils.test_data import Data
from utils.tools import take_screenshot


class TestScrollUpArrow:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.scrlUpArrow = ScrollUpArrow(self.page)

    def test_scroll_up_arrow(self, test_setup):
        self.scrlUpArrow.check_page_loaded()
        self.scrlUpArrow.scroll_to_footer()
        self.scrlUpArrow.verify_subscription_visible(Data.subscription)
        self.scrlUpArrow.arrow_up_btn_click()
        self.scrlUpArrow.verify_header_txt_visible(Data.headerText)
        take_screenshot(self.page, 'scroll_up_arrow')


