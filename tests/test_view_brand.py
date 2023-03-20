import pytest

from pages.view_brand_page import ViewBrand
from utils.test_data import Data


class TestViewBrand:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.viewBrand = ViewBrand(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.viewBrand.check_page_loaded()
        self.viewBrand.products_btn_click()
        self.viewBrand.left_brand_bar_visible()
        self.viewBrand.hm_click()
        self.viewBrand.check_brand_page_loaded(Data.brandHM)
        self.viewBrand.check_brand_items_visible()
        self.viewBrand.biba_click()
        self.viewBrand.check_brand_page_loaded(Data.brandBiba)
        self.viewBrand.check_brand_items_visible()
