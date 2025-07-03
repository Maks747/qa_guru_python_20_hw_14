from start.model.pages.button_new_page import NewPage
import allure


@allure.title("Проверка кнопки Новинки")
def test_button_new(browser_settings):
    browser = browser_settings

    with allure.step('Открыть главную страницу'):
        new_page = NewPage()
        new_page.open_main_page()

    with allure.step('Нажать на кнопку Новинки'):
        new_page.click_button_new()

    with allure.step('Проверить заголовок'):
        new_page.check_new_page_title()