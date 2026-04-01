from pages.main_page import MainPage
from pages.base_page import BasePage
from selenium import webdriver
from data.parametrize_data import FAQ_ANSWERS
from data.urls import BASE_URL
import pytest
import allure


@allure.feature("Логотипы")
class TestLogos:
    @pytest.fixture(autouse=True)
    def setup(self, driver_firefox):
        # Инициализируем страницу и открываем её через метод класса
        self.main_page = MainPage(driver_firefox)
        self.main_page.open_page(BASE_URL)

    @allure.title("Проверка перехода на Дзен через логотип Яндекса")
    def test_yandex_logo_click_success(self):
        self.main_page.click_yandex_logo()
        self.main_page.switch_to_new_window()
        self.main_page.wait_dzen_loaded()
        assert "dzen.ru" in self.main_page.get_url()

    @allure.title("Проверка возврата на главную через логотип Самоката")
    def test_samokat_logo_click_success(self):
        self.main_page.click_lower_order_button() 
        self.main_page.click_samokat_logo()
        self.main_page.wait_main_page_loaded()
        assert self.main_page.get_url() == BASE_URL


@allure.feature("Кнопки оформления заказа")
class TestOrderButtons:
    @pytest.fixture(autouse=True)
    def setup(self, driver_firefox):
        self.main_page = MainPage(driver_firefox)
        self.main_page.open_page(BASE_URL)

    @allure.title("Проверка верхней кнопки 'Заказать'")
    def test_upper_order_button_click_success(self):
        self.main_page.click_upper_order_button()
        assert "/order" in self.main_page.get_url()

    @allure.title("Проверка нижней кнопки 'Заказать'")
    def test_lower_order_button_click_success(self):
        self.main_page.click_lower_order_button()
        assert "/order" in self.main_page.get_url()


@allure.feature("FAQ (Вопросы и ответы)")
class TestMainPageFAQ:
    @allure.title("Проверка текста ответа в FAQ")
    @pytest.mark.parametrize("index, expected_answer", FAQ_ANSWERS)
    def test_faq_answer(self, driver_firefox, index, expected_answer):
        main_page = MainPage(driver_firefox)
        main_page.open_page(BASE_URL)
        main_page.click_faq_question(index)
        answer_text = main_page.get_faq_answer_text(index)
        assert answer_text == expected_answer