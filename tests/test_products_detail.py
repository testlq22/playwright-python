import pytest

from pages.verify_products_detail_page import VerifyProductsDetailPage


class TestVerifyTestCases:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.verProdPage = VerifyProductsDetailPage(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.verProdPage.check_page_loaded()
        self.verProdPage.products_btn_click()
        self.verProdPage.verify_all_products_page()
        self.verProdPage.verify_all_products_visible()
        self.verProdPage.first_product_details_click()
        self.verProdPage.check_product_details_page_loaded()
        self.verProdPage.check_products_details_info()
