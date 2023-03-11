from pages.main_page import MainPage

class TestMainPage:

    def test_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()

        assert main_page.check_order_url()

    def test_faq_1(self, driver):
        self.check_faq(MainPage(driver), 1)

    def test_faq_2(self, driver):
        self.check_faq(MainPage(driver), 2)

    def test_faq_3(self, driver):
        self.check_faq(MainPage(driver), 3)

    def test_faq_4(self, driver):
        self.check_faq(MainPage(driver), 4)

    def test_faq_5(self, driver):
        self.check_faq(MainPage(driver), 5)

    def test_faq_6(self, driver):
        self.check_faq(MainPage(driver), 6)

    def test_faq_7(self, driver):
        self.check_faq(MainPage(driver), 7)

    def test_faq_8(self, driver):
        self.check_faq(MainPage(driver), 8)

    def check_faq(self, main_page: MainPage, number):
        main_page.open_question(number)

        assert main_page.check_answer(number), (
            f'For question "{main_page.get_question_text(number)}" expected answer "{main_page.get_answer_text(number)}".'
        )
