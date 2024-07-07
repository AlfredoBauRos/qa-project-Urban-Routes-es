from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_order_taxi = (By.CLASS_NAME, "round")
    button_comfort = (By.XPATH, ".//div[@class='tcard-title' and text()='Comfort']")
    button_comfort_active = (By.XPATH, "//div[contains(@class, 'tcard active') and .//div[text()='Comfort']]")
    confirmed_phone_field = (By.CLASS_NAME, "np-button")
    button_phone_number = (By.CLASS_NAME, 'np-text')
    phone_field = (By.ID, "phone")
    button_next = (By.XPATH, "//button[text()='Siguiente']")
    confirm_button = (By.XPATH, "//button[@type='submit' and @class='button full' and text()='Confirmar']")
    payment_method_field = (By.CLASS_NAME, "pp-text")
    add_credit_card = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    card_number_field = (By.ID, "number")
    card_code_field = (By.XPATH, "//input[@placeholder='12']")
    code_field = (By.ID, 'code')
    button_add = (By.XPATH, "//button[@type='submit' and contains(@class, 'button full') and text()='Agregar']")
    message_for_driver_field = (By.ID, "comment")
    botton_switch_input = (By.XPATH, "(//span[contains(@class, 'slider') and contains(@class, 'round')])[1]")
    switch_input = (
        By.XPATH,
        "(//input[@type='checkbox' and contains(@class, 'switch-input')])[1]")
    counter_plus_disabled = (By.XPATH, "(//div[@class='counter-plus'])[1]")
    counter_value = (By.CLASS_NAME, "counter-value")
    button_start_trip = (By.CLASS_NAME, "smart-button-main")
    button_close_card = (By.XPATH, "(//div[@class='section active']//button[@class='close-button section-close'])[2]")
    order_header_content = (By.CLASS_NAME, "order-header-content")
    car_image_locator = (By.XPATH, "//img[contains(@src, '/static/media/kids.075fd8d4.svg') and @alt='Car']")
    modal_title_locator = (By.CLASS_NAME, 'order-header-title')
    pp_value_text_locator = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 45)

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

    def click_button_order_taxi(self):
        button_order_taxi = self.wait.until(EC.element_to_be_clickable(self.button_order_taxi))
        button_order_taxi.click()

    def click_button_comfort(self):
        button_comfort = self.wait.until(EC.element_to_be_clickable(self.button_comfort))
        button_comfort.click()

    def is_comfort_tariff_selected(self):
        try:
            self.driver.find_element(*self.button_comfort_active)
            return True
        except:
            return False

    def click_button_phone_number(self):
        self.driver.find_element(*self.button_phone_number).click()

    def set_phone(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def get_confirmed_phone_number(self):
        confirmed_phone_number_element = self.wait.until(EC.visibility_of_element_located(self.confirmed_phone_field))
        return confirmed_phone_number_element.text

    # nueva funcion para comprobar el numero de telefono ingresado, con el numero que se encuentra en el campo
    # "np-button" y se devuelve en texto

    def click_button_next(self):
        button_next = self.wait.until(EC.element_to_be_clickable(self.button_next))
        button_next.click()

    def click_confirm_button(self):
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.confirm_button))
        confirm_button.click()

    def click_payment_method_field(self):
        payment_method_field = self.wait.until(EC.element_to_be_clickable(self.payment_method_field))
        payment_method_field.click()

    def click_add_credit_card(self):
        add_credit_card = self.wait.until(EC.element_to_be_clickable(self.add_credit_card))
        add_credit_card.click()

    def set_card_number(self, card_number):
        card_number_field = self.wait.until(EC.visibility_of_element_located(self.card_number_field))
        card_number_field.clear()
        card_number_field.send_keys(card_number)

    def set_card_code(self, card_code):
        card_code_field = self.wait.until(EC.visibility_of_element_located(self.card_code_field))
        card_code_field.send_keys(card_code)

    def is_element_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        #verifica la presencia de un elemento en la página web utilizando un localizador dado.
        #se ocupo en el test_04 y en el test_08

    def set_code(self, code):
        code_field = self.wait.until(EC.visibility_of_element_located(self.code_field))
        code_field.send_keys(code)

    def click_button_add(self):
        button_add = self.wait.until(EC.element_to_be_clickable(self.button_add))
        button_add.click()

    def click_button_close_card(self):
        button_close_card = self.wait.until(EC.element_to_be_clickable(self.button_close_card))
        button_close_card.click()

    def set_message_for_driver(self, message_for_driver):
        message_for_driver_field = self.wait.until(EC.visibility_of_element_located(self.message_for_driver_field))
        message_for_driver_field.send_keys(message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def click_switch_input(self):
        switch_input = self.wait.until(EC.element_to_be_clickable(self.botton_switch_input))
        switch_input.click()

    def get_blanket_value(self):
        switch_element = self.wait.until(EC.presence_of_element_located(self.switch_input))
        return 'on' if switch_element.is_selected() else 'off'
    # Espera hasta que el elemento del switch esté presente y sea localizado
    # Devuelve 'on' si el switch está seleccionado, de lo contrario devuelve 'off'

    def double_click_counter_plus_disabled(self):
        counter_plus_disabled = self.wait.until(EC.element_to_be_clickable(self.counter_plus_disabled))
        counter_plus_disabled.click()
        counter_plus_disabled.click()

    def get_ice_cream_order_count(self):
        value_element = self.wait.until(EC.visibility_of_element_located(self.counter_value))
        value = value_element.text.strip()
        return int(value) if value else 0

    def click_button_start_trip(self):
        button_start_trip = self.wait.until(EC.element_to_be_clickable(self.button_start_trip))
        button_start_trip.click()

    def click_order_header_content(self):
        order_header_content = self.wait.until(EC.element_to_be_clickable(self.order_header_content))
        order_header_content.click()

    def click_car_image_locator(self):
        # Verifica que la imagen del auto esté presente y visible
        car_image_element = self.wait.until(EC.visibility_of_element_located(self.car_image_locator))
        return car_image_element.is_displayed()

    def is_car_image_visible(self):
        # Verifica que la imagen del auto esté presente y visible
        try:
            car_image_element = self.wait.until(EC.visibility_of_element_located(self.car_image_locator))
            return car_image_element.is_displayed()
        except TimeoutException:
            return False
