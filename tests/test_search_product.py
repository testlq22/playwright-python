import pytest

from pages.search_product_page import SearchProductPage
from utils.test_data import Data


class TestSearchProduct:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.searchProd = SearchProductPage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.searchProd.check_page_loaded()
        self.searchProd.products_btn_click()
        self.searchProd.verify_products_page()
        self.searchProd.search_product(Data.product)
        self.searchProd.verify_searched_products_txt_visible()
        self.searchProd.verify_searched_products_visible()
