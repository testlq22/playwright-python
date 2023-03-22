import pytest

from pages.scroll_up_page import ScrollUp
from utils.test_data import Data
from utils.tools import take_screenshot


class TestScrollUp:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.scrlUp = ScrollUp(self.page)

    def test_scroll_up(self, test_setup):
        self.scrlUp.check_page_loaded()
        self.scrlUp.scroll_to_footer()
        self.scrlUp.verify_subscription_visible(Data.subscription)
        self.scrlUp.scroll_to_header()
        self.scrlUp.verify_header_txt_visible(Data.headerText)
        take_screenshot(self.page, 'scroll_up')
