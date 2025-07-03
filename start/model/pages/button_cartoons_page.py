from selene import browser, have


class CartoonsPage:
    def __init__(self):
        self.button_cartoons = browser.element('[data-testid="animation_button"]')

    def open_main_page(self):
        browser.open('https://start.ru/')

    def click_button_cartoons(self):
        self.button_cartoons.click()

    def check_cartoons_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(have.text('Мультфильмы - смотреть онлайн'))