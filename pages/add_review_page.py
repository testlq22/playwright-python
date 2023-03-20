from playwright.sync_api import Page, expect


class ReviewProducts:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__first_product_det = self.page.locator('[href="/product_details/1"]')
        self.__name_field = self.page.locator('[id="name"]')
        self.__email_field = self.page.locator('[id="email"]')
        self.__review_field = self.page.locator('[name="review"]')
        self.__submit_btn = self.page.locator('[id="button-review"]')
        self.__thankyou_msg = self.page.locator('[class="col-md-12 form-group"]>[class="alert-success alert"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def first_product_det_click(self) -> None:
        self.__first_product_det.click()

    def fill_name(self, name) -> None:
        self.__name_field.click()
        self.__name_field.fill(name)

    def fill_email(self, email) -> None:
        self.__email_field.click()
        self.__email_field.fill(email)

    def fill_review(self, review) -> None:
        self.__review_field.click()
        self.__review_field.fill(review)

    def click_submit_btn(self) -> None:
        self.__submit_btn.click()

    def verify_thankyou_msg_visible(self, msg) -> None:
        expect(self.__thankyou_msg).to_have_text(msg)
        expect(self.__thankyou_msg).to_be_visible()
