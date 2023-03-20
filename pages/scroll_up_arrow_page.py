from playwright.sync_api import Page, expect


class ScrollUpArrow:

    def __init__(self, page: Page):

        self.page = page
        self.__footer = self.page.locator('[id="footer"]')
        self.__subscription = self.page.locator('[class="single-widget"]')
        self.__arrow_up_btn = self.page.locator('[id="scrollUp"]')
        self.__header_txt = self.page.locator('[class="item active"]>[class="col-sm-6"]>h2')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def scroll_to_footer(self) -> None:
        self.__footer.scroll_into_view_if_needed()

    def verify_subscription_visible(self, msg) -> None:
        expect(self.__subscription).to_contain_text(msg)
        expect(self.__subscription).to_be_visible()

    def arrow_up_btn_click(self) -> None:
        self.__arrow_up_btn.click()

    def verify_header_txt_visible(self, msg) -> None:
        expect(self.__header_txt).to_have_text(msg)
        expect(self.__header_txt).to_be_visible()
