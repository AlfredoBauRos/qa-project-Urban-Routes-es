from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import data
from main import UrbanRoutesPage, retrieve_phone_code


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_01_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_02_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_pedir_un_taxi()
        routes_page.click_boton_confort()
        assert routes_page.is_comfort_tariff_selected(), "not selected"

    def test_03_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_botton_number_phone()
        phone_number = data.phone_number
        routes_page.set_tel(phone_number)
        assert routes_page.get_tel() == phone_number

    def test_04_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_siguiente()
        code = retrieve_phone_code(driver=self.driver)
        routes_page.set_code(code)
        routes_page.click_confirm_button()
        routes_page.click_metodo_de_pago_field()
        routes_page.click_agregar_tarjeta_de_credito()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_numero_de_tarjeta(card_number)
        routes_page.set_card_code(card_code)
        routes_page.driver.find_element(*routes_page.numero_de_tarjeta).send_keys(Keys.TAB)
        routes_page.click_boton_agregar()
        routes_page.click_botton_close_card()
        assert routes_page.get_numero_de_tarjeta() == card_number
        assert routes_page.get_card_code() == card_code

    def test_05_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_agregar_mensaje_conductor(message_for_driver)
        assert routes_page.get_agregar_mensaje_conductor() == message_for_driver

    def test_06_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_switch_input()

    def test_07_order_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.double_click_counter_plus_disabled()
        assert routes_page.get_ice_cream_order_count() == 2

    def test_08_modal_appears_to_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_boton_iniciar_viaje()
        modal_title_locator = (By.CLASS_NAME, 'order-header-title')
        is_modal_present = routes_page.is_element_present(modal_title_locator)
        assert is_modal_present, "El modal de búsqueda de automóvil no está presente."

    def test_09_wait_for_driver_info_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_header_content()
        routes_page.click_car_image_locator()
