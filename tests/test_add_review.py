import pytest

from pages.add_review_page import ReviewProducts
from utils.test_data import Data
from utils.tools import take_screenshot


class TestAddReview:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.revProducts = ReviewProducts(self.page)

    def test_add_review(self, test_setup):
        self.revProducts.check_page_loaded()
        self.revProducts.products_btn_click()
        self.revProducts.first_product_det_click()
        self.revProducts.fill_name(Data.firstName)
        self.revProducts.fill_email(Data.fakeEmail)
        self.revProducts.fill_review(Data.review)
        self.revProducts.click_submit_btn()
        self.revProducts.verify_thankyou_msg_visible(Data.thankMsg)
        take_screenshot(self.page, 'add_review')
