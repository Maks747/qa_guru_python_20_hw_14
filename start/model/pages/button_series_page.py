from selene import browser, have


class SeriesPage:
    def __init__(self):
        self.button_series = browser.element('[data-testid="series_button"]')

    def open_main_page(self):
        browser.open("")

    def click_button_series(self):
        self.button_series.click()

    def check_series_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(have.text('Сериалы - смотреть онлайн'))