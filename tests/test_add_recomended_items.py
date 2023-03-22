import pytest

from pages.add_recomended_items_page import AddRecommendedItems
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAddRecommendedItems:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.recItems = AddRecommendedItems(self.page)

    def test_add_recommended_items(self, test_setup):
        self.recItems.check_page_loaded()
        self.recItems.scroll_to_recommended()
        self.recItems.verify_recommended_visible(Data.recommendedItms)
        self.recItems.product2_btn_click()
        self.recItems.view_cart_btn_click()
        self.recItems.verify_product6_visible()
        take_screenshot(self.page, 'add_recommended')
