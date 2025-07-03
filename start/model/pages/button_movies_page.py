from selene import browser, have


class MoviesPage:
    def __init__(self):
        self.button_movies = browser.element('[data-testid="movies_button"]')

    def open_main_page(self):
        browser.open('https://start.ru/')

    def click_button_movies(self):
        self.button_movies.click()

    def check_movies_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(have.text('Фильмы - смотреть онлайн'))