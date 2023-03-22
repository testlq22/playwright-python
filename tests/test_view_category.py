import pytest

from pages.view_category_page import ViewCategory
from utils.test_data import Data
from utils.tools import take_screenshot


class TestViewCategory:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.viewCategory = ViewCategory(self.page)

    def test_view_category(self, test_setup):
        self.viewCategory.check_page_loaded()
        self.viewCategory.left_category_bar_visible()
        self.viewCategory.women_click()
        self.viewCategory.dress_subcategory_click()
        self.viewCategory.check_category_dress_page_loaded(Data.dressCategory)
        self.viewCategory.check_category_text_visible()
        self.viewCategory.men_click()
        self.viewCategory.jeans_subcategory_click()
        self.viewCategory.check_category_jeans_page_loaded(Data.jeansCategory)
        take_screenshot(self.page, 'view_category')
