from playwright.sync_api import Page, expect


class ScrollUp:

    def __init__(self, page: Page):

        self.page = page
        self.__footer = self.page.locator('[id="footer"]')
        self.__subscription = self.page.locator('[class="single-widget"]')
        self.__header_txt = self.page.locator('[class="item active"]>[class="col-sm-6"]>h2')
        self.__header = self.page.locator('[id="header"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def scroll_to_footer(self) -> None:
        self.__footer.scroll_into_view_if_needed()

    def verify_subscription_visible(self, msg) -> None:
        expect(self.__subscription).to_contain_text(msg)
        expect(self.__subscription).to_be_visible()

    def scroll_to_header(self) -> None:
        self.__header.scroll_into_view_if_needed()

    def verify_header_txt_visible(self, msg) -> None:
        expect(self.__header_txt).to_have_text(msg)
        expect(self.__header_txt).to_be_visible()
