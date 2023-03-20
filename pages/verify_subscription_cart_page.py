from playwright.sync_api import Page, expect


class VerifySubscriptionCartPage:

    def __init__(self, page: Page):

        self.page = page
        self.__cart_btn_header = self.page.locator('li>[href="/view_cart"]')
        self.__arrow_btn = self.page.locator('button[id="subscribe"]')
        self.__subscription_txt = self.page.locator('[class="single-widget"]')
        self.__email_field = self.page.locator('[id="susbscribe_email"]')
        self.__success_alert = self.page.locator('[class="alert-success alert"]')

        self.__search_btn = self.page.locator('button[id="submit_search"]')

    def check_page_loaded(self) -> None:
        expect(self.page).to_have_url('https://automationexercise.com/')

    def click_cart_btn_header(self) -> None:
        self.__cart_btn_header.click()

    def scroll_to_arrow(self) -> None:
        self.__arrow_btn.scroll_into_view_if_needed()

    def verify_subscription_txt_visible(self) -> None:
        expect(self.__subscription_txt).to_contain_text('Subscription')
        expect(self.__subscription_txt).to_be_visible()

    def fill_email(self, email) -> None:
        self.__email_field.fill(email)

    def click_arrow_btn(self) -> None:
        self.__arrow_btn.click()

    def verify_success_alert_visible(self) -> None:
        expect(self.__success_alert).to_contain_text('You have been successfully subscribed!')
        expect(self.__success_alert).to_be_visible()
