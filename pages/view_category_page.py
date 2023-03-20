from playwright.sync_api import Page, expect


class ViewCategory:

    def __init__(self, page: Page):

        self.page = page
        self.__left_category_bar = self.page.locator('[class="left-sidebar"]>[class="panel-group category-products"]')
        self.__women_btn = self.page.locator('[href="#Women"]')
        self.__dress_btn = self.page.locator('[href="/category_products/1"]')
        self.__category_text = self.page.locator('[class="title text-center"]')
        self.__men_btn = self.page.locator('[href="#Men"]')
        self.__jeans_btn = self.page.locator('[href="/category_products/6"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def left_category_bar_visible(self) -> None:
        expect(self.__left_category_bar).to_be_visible()

    def women_click(self) -> None:
        self.__women_btn.click()

    def dress_subcategory_click(self) -> None:
        self.__dress_btn.click()

    def check_category_dress_page_loaded(self, categoryurl) -> None:
        expect(self.page).to_have_url(categoryurl)

    def check_category_text_visible(self) -> None:
        expect(self.__category_text).to_have_text('Women - Dress Products')
        expect(self.__category_text).to_be_visible()

    def men_click(self) -> None:
        self.__men_btn.click()

    def jeans_subcategory_click(self) -> None:
        self.__jeans_btn.click()

    def check_category_jeans_page_loaded(self, categoryurl) -> None:
        expect(self.page).to_have_url(categoryurl)
