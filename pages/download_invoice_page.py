from playwright.sync_api import Page, expect


class DownloadInvoice:

    def __init__(self, page: Page):

        self.page = page
        self.__dwnld_invoice = self.page.locator('[class="col-sm-9 col-sm-offset-1"]>[href="/download_invoice/900"]')

    def click_dwnld_invoice_btn(self) -> None:
        self.__dwnld_invoice.click()
