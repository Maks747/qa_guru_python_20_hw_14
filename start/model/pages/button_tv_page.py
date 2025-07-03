from selene import browser, have


class TVPage:
    def __init__(self):
        self.button_tv = browser.element('[data-testid="tv_button"]')

    def open_main_page(self):
        browser.open('https://start.ru/')

    def click_button_tv(self):
        self.button_tv.click()

    def check_tv_page_title(self):
        (browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should
         (have.text('ТВ Каналы Онлайн и Программа Передач')))