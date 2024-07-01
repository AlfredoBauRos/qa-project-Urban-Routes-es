from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    import json
    import time
    from selenium.common.exceptions import WebDriverException

    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if
                    log.get("message") and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if code:
            break

    if not code:
        raise Exception("No se encontró el código de confirmación del teléfono.\n"
                        "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
    return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    boton_pedir_un_taxi = (By.CLASS_NAME, "round")
    boton_confort = (By.XPATH, ".//div[@class='tcard-title' and text()='Comfort']")
    boton_confort_activo = (By.XPATH, "//div[contains(@class, 'tcard active') and .//div[text()='Comfort']]")
    botton_number_phone = (By.CLASS_NAME, "np-button")
    tel_field = (By.ID, "phone")
    boton_siguiente = (By.XPATH, "//button[text()='Siguiente']")
    confirm_button = (By.XPATH, "//button[@type='submit' and @class='button full' and text()='Confirmar']")
    metodo_de_pago_field = (By.CLASS_NAME, "pp-text")
    agregar_tarjeta_de_credito = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    numero_de_tarjeta = (By.ID, "number")
    card_code = (By.XPATH, "//input[@placeholder='12']")
    code = (By.ID, 'code')
    boton_agregar = (By.XPATH, "//button[@type='submit' and contains(@class, 'button full') and text()='Agregar']")
    agregar_mensaje_conductor = (By.ID, "comment")
    switch_input = (
        By.XPATH,
        "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following-sibling::div[@class='r-sw']/div/span")
    counter_plus_disabled = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    counter_value = (By.CLASS_NAME, "counter-value")
    boton_iniciar_viaje = (By.CLASS_NAME, "smart-button-main")
    botton_close_card = (By.XPATH, "(//div[@class='section active']//button[@class='close-button section-close'])[2]")
    order_header_content = (By.CLASS_NAME, "order-header-content")
    car_image_locator = (By.XPATH, "//img[contains(@src, '/static/media/kids.075fd8d4.svg') and @alt='Car']")
    modal_title_locator = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def set_from(self, from_address):
        from_field = self.wait.until(EC.visibility_of_element_located(self.from_field))
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        to_field = self.wait.until(EC.visibility_of_element_located(self.to_field))
        to_field.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_boton_pedir_un_taxi(self):
        boton_pedir_un_taxi = self.wait.until(EC.element_to_be_clickable(self.boton_pedir_un_taxi))
        boton_pedir_un_taxi.click()

    def click_boton_confort(self):
        boton_confort = self.wait.until(EC.element_to_be_clickable(self.boton_confort))
        boton_confort.click()

    def is_comfort_tariff_selected(self):
        try:
            self.driver.find_element(*self.boton_confort_activo)
            return True
        except:
            return False

    def click_botton_number_phone(self):
        botton_number_phone = self.wait.until(EC.element_to_be_clickable(self.botton_number_phone))
        botton_number_phone.click()

    def set_tel(self, from_phone):
        tel_field = self.wait.until(EC.visibility_of_element_located(self.tel_field))
        tel_field.send_keys(from_phone)

    def get_tel(self):
        return self.driver.find_element(*self.tel_field).get_property('value')

    def click_boton_siguiente(self):
        boton_siguiente = self.wait.until(EC.element_to_be_clickable(self.boton_siguiente))
        boton_siguiente.click()

    def click_confirm_button(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.confirm_button))
        confirm_button.click()

    def click_metodo_de_pago_field(self):
        metodo_de_pago_field = self.wait.until(EC.element_to_be_clickable(self.metodo_de_pago_field))
        metodo_de_pago_field.click()

    def click_agregar_tarjeta_de_credito(self):
        agregar_tarjeta_de_credito = self.wait.until(EC.element_to_be_clickable(self.agregar_tarjeta_de_credito))
        agregar_tarjeta_de_credito.click()

    def set_numero_de_tarjeta(self, from_card_number):
        numero_de_tarjeta = self.wait.until(EC.visibility_of_element_located(self.numero_de_tarjeta))
        numero_de_tarjeta.send_keys(from_card_number)

    def get_numero_de_tarjeta(self):
        return self.driver.find_element(*self.numero_de_tarjeta).get_property('value')

    def set_card_code(self, from_card_code):
        card_code = self.wait.until(EC.visibility_of_element_located(self.card_code))
        card_code.send_keys(from_card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.card_code).get_property('value')

    def set_code(self, from_code):
        code = self.wait.until(EC.visibility_of_element_located(self.code))
        code.send_keys(from_code)

    def click_boton_agregar(self):
        boton_agregar = self.wait.until(EC.element_to_be_clickable(self.boton_agregar))
        boton_agregar.click()

    def click_botton_close_card(self):
        botton_close_card = self.wait.until(EC.element_to_be_clickable(self.botton_close_card))
        botton_close_card.click()

    def set_agregar_mensaje_conductor(self, from_message_for_driver):
        agregar_mensaje_conductor = self.wait.until(EC.visibility_of_element_located(self.agregar_mensaje_conductor))
        agregar_mensaje_conductor.send_keys(from_message_for_driver)

    def get_agregar_mensaje_conductor(self):
        return self.driver.find_element(*self.agregar_mensaje_conductor).get_property('value')

    def click_switch_input(self):
        switch_input = self.wait.until(EC.element_to_be_clickable(self.switch_input))
        switch_input.click()

    def double_click_counter_plus_disabled(self):
        counter_plus_disabled = self.wait.until(EC.element_to_be_clickable(self.counter_plus_disabled))
        counter_plus_disabled.click()
        counter_plus_disabled.click()

    def get_ice_cream_order_count(self):
        value_element = self.wait.until(EC.visibility_of_element_located(self.counter_value))
        value = value_element.text.strip()
        return int(value) if value else 0

    def click_boton_iniciar_viaje(self):
        boton_iniciar_viaje = self.wait.until(EC.element_to_be_clickable(self.boton_iniciar_viaje))
        boton_iniciar_viaje.click()

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_order_header_content(self):
        order_header_content = self.wait.until(EC.element_to_be_clickable(self.order_header_content))
        order_header_content.click()

    def click_car_image_locator(self):
        car_image_locator = self.wait.until(EC.visibility_of_element_located(self.car_image_locator))
        car_image_locator.click()
