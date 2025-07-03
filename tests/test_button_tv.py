from start.model.pages.button_tv_page import TVPage
import allure


@allure.title("Проверка кнопки ТВ")
def test_button_tv(browser_settings):
    browser = browser_settings

    with allure.step('Открыть главную страницу'):
        tv_page = TVPage()
        tv_page.open_main_page()

    with allure.step('Нажать на кнопку ТВ'):
        tv_page.click_button_tv()

    with allure.step('Проверить заголовок'):
        tv_page.check_tv_page_title()