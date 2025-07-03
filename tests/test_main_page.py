from start.model.pages.main_page import MainPage
from selene import have
import allure

@allure.title('Главный экран')
def test_main_page(browser_settings):
    browser = browser_settings

with allure.step('Открыть главную страницу'):
    main_page = MainPage()
    main_page.open_main_page()

with allure.step('Кино на ТВ - отображается в верхнем меню'):
    main_page.kino_na_TV_should_be_visible()