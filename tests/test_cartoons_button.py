from start.model.pages.button_cartoons_page import CartoonsPage
import allure


@allure.title("Проверка кнопки Детям")
def test_cartoons_button(browser_settings):
    browser = browser_settings

    with allure.step('Открыть главную страницу'):
        cartoons_page = CartoonsPage()
        cartoons_page.open_main_page()

    with allure.step('Нажать на кнопку Детям'):
        cartoons_page.click_button_cartoons()

    with allure.step('Проверить заголовок'):
        cartoons_page.check_cartoons_page_title()