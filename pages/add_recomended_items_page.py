from playwright.sync_api import Page, expect


class AddRecommendedItems:

    def __init__(self, page: Page):

        self.page = page
        self.__recommended_itms = self.page.locator('[class="recommended_items"]>[class="title text-center"]')
        self.__add_prod2_btn = self.page.locator('#recommended-item-carousel > div > div.item.active > div:nth-child(3) > div > div > div > a')
        self.__view_cart_btn = self.page.locator('[class="text-center"]>[href="/view_cart"]')
        self.__product6_in_cart = self.page.locator('[id="product-6"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def scroll_to_recommended(self) -> None:
        self.__recommended_itms.scroll_into_view_if_needed()

    def verify_recommended_visible(self, msg) -> None:
        expect(self.__recommended_itms).to_have_text(msg)
        expect(self.__recommended_itms).to_be_visible()

    def product2_btn_click(self) -> None:
        self.__add_prod2_btn.click()

    def view_cart_btn_click(self) -> None:
        self.__view_cart_btn.click()

    def verify_product6_visible(self) -> None:
        expect(self.__product6_in_cart).to_be_visible()
