import pytest

from pages.view_brand_page import ViewBrand
from utils.test_data import Data
from utils.tools import take_screenshot


class TestViewBrand:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.viewBrand = ViewBrand(self.page)

    def test_view_brand(self, test_setup):
        self.viewBrand.check_page_loaded()
        self.viewBrand.products_btn_click()
        self.viewBrand.left_brand_bar_visible()
        self.viewBrand.hm_click()
        self.viewBrand.check_brand_page_loaded(Data.brandHM)
        self.viewBrand.check_brand_items_visible()
        self.viewBrand.biba_click()
        self.viewBrand.check_brand_page_loaded(Data.brandBiba)
        self.viewBrand.check_brand_items_visible()
        take_screenshot(self.page, 'view_brand')
