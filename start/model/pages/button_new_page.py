from selene import browser, have


class NewPage:
    def __init__(self):
        self.button_new = browser.element('[data-testid="new_button"]')

    def open_main_page(self):
        browser.open("")

    def click_button_new(self):
        self.button_new.click()

    def check_new_page_title(self):
        (browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should
         (have.text('Новинки фильмов, мультфильмов и сериалов смотреть онлайн')))