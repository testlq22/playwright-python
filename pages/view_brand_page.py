from playwright.sync_api import Page, expect


class ViewBrand:

    def __init__(self, page: Page):

        self.page = page
        self.__submit_products_btn = self.page.locator('[href="/products"]')
        self.__left_brand_bar = self.page.locator('[class="left-sidebar"]>[class="brands_products"]')
        self.__brand_items = self.page.locator('[class="features_items"]')
        self.__hm_btn = self.page.locator('[href="/brand_products/H&M"]')
        self.__biba_btn = self.page.locator('[href="/brand_products/Biba"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def products_btn_click(self) -> None:
        self.__submit_products_btn.click()

    def left_brand_bar_visible(self) -> None:
        expect(self.__left_brand_bar).to_be_visible()

    def hm_click(self) -> None:
        self.__hm_btn.click()

    def biba_click(self) -> None:
        self.__biba_btn.click()

    def check_brand_page_loaded(self, brandurl) -> None:
        expect(self.page).to_have_url(brandurl)

    def check_brand_items_visible(self) -> None:
        expect(self.__brand_items).to_be_visible()
