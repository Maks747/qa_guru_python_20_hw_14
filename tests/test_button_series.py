from start.model.pages.button_series_page import SeriesPage
import allure


@allure.title("Проверка кнопки Сериалы")
def test_button_series(browser_settings):
    browser = browser_settings

    with allure.step('Открыть главную страницу'):
        series_page = SeriesPage()
        series_page.open_main_page()

    with allure.step('Нажать на кнопку Сериалы'):
        series_page.click_button_series()

    with allure.step('Проверить заголовок'):
        series_page.check_series_page_title()