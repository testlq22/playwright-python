from playwright.sync_api import Page, expect


class RemoveProducts:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__first_product = self.page.locator('[src="/get_product_picture/1"]')
        self.__second_product = self.page.locator('[src="/get_product_picture/2"]')
        self.__add_first_product = self.page.locator('[class="overlay-content"]>[data-product-id="1"]')
        self.__continue_shopping = self.page.locator('[class="btn btn-success close-modal btn-block"]')
        self.__add_second_product = self.page.locator('[class="overlay-content"]>[data-product-id="2"]')
        self.__cart_button = self.page.locator('li>[href="/view_cart"]')
        self.__product_in_cart_1 = self.page.locator('[id="product-1"]')
        self.__product_in_cart_2 = self.page.locator('[id="product-2"]')
        self.__del_product_1 = self.page.locator('[id="product-1"]>td>[class="cart_quantity_delete"]')
        self.__del_product_2 = self.page.locator('[id="product-2"]>td>[class="cart_quantity_delete"]')
        self.__cart_body = self.page.locator('tbody')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def hover_product_1(self) -> None:
        self.__first_product.hover()

    def hover_product_2(self) -> None:
        self.__second_product.hover()

    def add_first_product(self) -> None:
        self.__add_first_product.click()

    def click_continue_shopping(self) -> None:
        self.__continue_shopping.click()

    def add_second_product(self) -> None:
        self.__add_second_product.click()

    def click_cart_button(self) -> None:
        self.__cart_button.click()

    def verify_product_1_visible(self) -> None:
        expect(self.__product_in_cart_1).to_be_visible()

    def verify_product_2_visible(self) -> None:
        expect(self.__product_in_cart_2).to_be_visible()

    def check_cart_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/view_cart')

    def del_product_1(self) -> None:
        self.__del_product_1.click()

    def del_product_2(self) -> None:
        self.__del_product_2.click()

    def verify_product_1_not_visible(self, id1) -> None:
        expect(self.__cart_body).not_to_have_id(id1)

    def verify_product_2_not_visible(self, id2) -> None:
        expect(self.__cart_body).not_to_have_id(id2)
