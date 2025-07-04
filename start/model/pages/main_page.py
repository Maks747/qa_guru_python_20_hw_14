from selene import browser, have


class MainPage:
    def open_main_page(self):
            browser.open("")

            #browser.driver.execute_script("$('#fixedban').remove()")
            #browser.driver.execute_script("$('footer').remove()")

    def kino_na_TV_should_be_visible(self):
            browser.element('#main_header').should(have.text('Кино на ТВ'))
