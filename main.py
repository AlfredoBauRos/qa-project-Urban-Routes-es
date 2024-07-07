from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import data
from helpers import retrieve_phone_code
from Urban_Routes_Page import UrbanRoutesPage


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
        routes_page.click_button_order_taxi()
        routes_page.click_button_comfort()
        assert routes_page.is_comfort_tariff_selected(), "Comfort tariff not selected"

    def test_03_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_phone_number()
        phone_number = data.phone_number
        routes_page.set_phone(phone_number)
        routes_page.click_button_next()
        code = retrieve_phone_code(driver=self.driver)
        assert code
        routes_page.set_code(code)
        routes_page.click_confirm_button()
        # Agregamos un tiempo de espera para asegurarte de que el número de teléfono se confirme
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(routes_page.confirmed_phone_field, phone_number)
        )
        confirmed_phone_number = routes_page.get_confirmed_phone_number()
        assert phone_number in confirmed_phone_number, f"Número de teléfono incorrecto: {confirmed_phone_number}"
        #confirmamos si el numero de telefono que se ingreso, se encuentra ingresado en el campo confirmed_phone_number o localizador np-button arriba de np-text

    def test_04_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method_field()
        routes_page.click_add_credit_card()
        card_number = data.card_number
        card_code = data.card_code
        routes_page.set_card_number(card_number)
        routes_page.set_card_code(card_code)
        routes_page.driver.find_element(*routes_page.card_number_field).send_keys(Keys.TAB)
        routes_page.click_button_add()
        routes_page.click_button_close_card()
        # Al querer hacer un assert en cuestion de los datos en el boton pp-button el boton no guarda estos datos
        # Verificamone que el elemento con texto 'Tarjeta' está presente, asi aseguramos que la prueba paso,
        # que tenemos el metodo de pago con tarjeta y los datos de data se ingresaron correctamente.
        assert routes_page.is_element_present(
            routes_page.pp_value_text_locator), "El texto 'Tarjeta' no está presente en el elemento 'pp-value-text'"

    def test_05_write_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test_06_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_switch_input()
        assert routes_page.get_blanket_value() == 'on', "El valor del switch no es 'on'"
        #aqui comprobamos que el switch este activo si el switch no está activado, la afirmación fallará y se mostrará el mensaje de error.

    def test_07_order_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.double_click_counter_plus_disabled()
        assert routes_page.get_ice_cream_order_count() == 2

    def test_08_modal_appears_to_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_start_trip()
        modal_title_locator = (By.CLASS_NAME, 'order-header-title')
        is_modal_present = routes_page.is_element_present(modal_title_locator)
        assert is_modal_present, "The car search modal is not present."

    def test_09_wait_for_driver_info_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_header_content()
        routes_page.click_car_image_locator()
        assert routes_page.is_car_image_visible(), "Car image should be visible"
        #se agrego el assert que verifica que salga la imagen del carrito una vez que aparecen los datos del conductor
