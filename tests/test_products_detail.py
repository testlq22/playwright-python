import pytest

from pages.verify_products_detail_page import VerifyProductsDetailPage
from utils.tools import take_screenshot


class TestVerifyProductsDetailPage:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.verProdPage = VerifyProductsDetailPage(self.page)

    def test_verify_product_detail_page(self, test_setup):
        self.verProdPage.check_page_loaded()
        self.verProdPage.products_btn_click()
        self.verProdPage.verify_all_products_page()
        self.verProdPage.verify_all_products_visible()
        self.verProdPage.first_product_details_click()
        self.verProdPage.check_product_details_page_loaded()
        self.verProdPage.check_products_details_info()
        take_screenshot(self.page, 'product_detail')
