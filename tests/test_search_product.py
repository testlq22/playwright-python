import pytest

from pages.search_product_page import SearchProductPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestSearchProduct:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.searchProd = SearchProductPage(self.page)

    def test_search_product_page(self, test_setup):
        self.searchProd.check_page_loaded()
        self.searchProd.products_btn_click()
        self.searchProd.verify_products_page()
        self.searchProd.search_product(Data.product)
        self.searchProd.verify_searched_products_txt_visible()
        self.searchProd.verify_searched_products_visible()
        take_screenshot(self.page, 'search_product_page')
