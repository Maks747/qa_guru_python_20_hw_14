from start.model.pages.button_movies_page import MoviesPage
import allure


@allure.title("Проверка кнопки Фильмы")
def test_button_movies(browser_settings):
    browser = browser_settings

    with allure.step('Открыть главную страницу'):
        movies_page = MoviesPage()
        movies_page.open_main_page()

    with allure.step('Нажать на кнопку Фильмы'):
        movies_page.click_button_movies()

    with allure.step('Проверить заголовок'):
        movies_page.check_movies_page_title()