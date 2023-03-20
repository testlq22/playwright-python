import pytest

from pages.add_review_page import ReviewProducts
from utils.test_data import Data


class TestAddProducts:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.revProducts = ReviewProducts(self.page)

        self.page.goto('https://automationexercise.com/')

    def test_verify_product_detail_page(self, test_setup):
        self.revProducts.check_page_loaded()
        self.revProducts.products_btn_click()
        self.revProducts.first_product_det_click()
        self.revProducts.fill_name(Data.firstName)
        self.revProducts.fill_email(Data.fakeEmail)
        self.revProducts.fill_review(Data.review)
        self.revProducts.click_submit_btn()
        self.revProducts.verify_thankyou_msg_visible(Data.thankMsg)
