from playwright.sync_api import Page, expect


class VerifyProductQuantity:

    def __init__(self, page: Page):

        self.page = page
        self.__third_product_details_page = self.page.locator('[href="/product_details/3"]')
        self.__quantity_input = self.page.locator('[id="quantity"]')
        self.__add_to_cart = self.page.locator('[class="btn btn-default cart"]')
        self.__view_cart = self.page.locator('[class="text-center"]>[href="/view_cart"]')
        self.__product_in_cart_3 = self.page.locator('[id="product-3"]')
        self.__quantity_in_cart = self.page.locator('[class="cart_quantity"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def third_product_details_click(self) -> None:
        self.__third_product_details_page.click()

    def check_product_details_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/product_details/3')

    def set_quantity(self, quantity) -> None:
        self.__quantity_input.click()
        self.__quantity_input.clear()
        self.__quantity_input.fill(quantity)

    def add_to_cart_click(self) -> None:
        self.__add_to_cart.click()

    def click_view_cart(self) -> None:
        self.__view_cart.click()

    def check_product_3_quantity_info(self, quantity) -> None:
        expect(self.__product_in_cart_3).to_be_visible()
        expect(self.__quantity_in_cart).to_have_text(quantity)
