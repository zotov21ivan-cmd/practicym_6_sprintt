from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium import webdriver
from data.urls import BASE_URL
from data.parametrize_data import DATA_FOR_ORDER
import pytest
import allure

@allure.feature("Оформление заказа")
class TestOrderPage:

    @allure.title("Проверка успешного оформления заказа с различными данными")
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, rental_period, color, order_button", DATA_FOR_ORDER)
    def test_order_success(self, driver_firefox, first_name, last_name, address, metro_station, phone_number, date, rental_period, color, order_button):
        main_page = MainPage(driver_firefox)
        order_page = OrderPage(driver_firefox)
        main_page.open_page(BASE_URL)
        main_page.select_order_button(order_button)
        order_page.fill_first_page(
            first_name, 
            last_name, 
            address, 
            metro_station, 
            phone_number
        )
        order_page.click_next_button()
        order_page.fill_second_page(date, rental_period, color)
        order_page.click_order_button()
        order_page.confirm_order()
        # получаем текст статуса заказа через метод страницы
        actual_message = order_page.get_order_status_text()
        
        assert "Заказ оформлен" in actual_message, \
            f"Ожидали сообщение 'Заказ оформлен', но получили: '{actual_message}'"
        
          