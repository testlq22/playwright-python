import pytest

from pages.add_recomended_items_page import AddRecommendedItems
from utils.test_data import Data


class TestAddRecommendedItems:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.recItems = AddRecommendedItems(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.recItems.check_page_loaded()
        self.recItems.scroll_to_recommended()
        self.recItems.verify_recommended_visible(Data.recommendedItms)
        self.recItems.product2_btn_click()
        self.recItems.view_cart_btn_click()
        self.recItems.verify_product6_visible()
