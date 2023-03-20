import pytest

from pages.view_category_page import ViewCategory
from utils.test_data import Data


class TestViewCategory:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.viewCategory = ViewCategory(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.viewCategory.check_page_loaded()
        self.viewCategory.left_category_bar_visible()
        self.viewCategory.women_click()
        self.viewCategory.dress_subcategory_click()
        self.viewCategory.check_category_dress_page_loaded(Data.dressCategory)
        self.viewCategory.check_category_text_visible()
        self.viewCategory.men_click()
        self.viewCategory.jeans_subcategory_click()
        self.viewCategory.check_category_jeans_page_loaded(Data.jeansCategory)
