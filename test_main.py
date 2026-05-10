import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import data
from UrbanRoutesPage import UrbanRoutesPage
import helpers as helpers



class TestUrbanRoutes:

    driver = None


    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {
            "browser": "ALL",
            "performance": "ALL"
        })
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.execute_cdp_cmd("Network.enable", {})

    def test_1_set_route(self):
        self.driver.get(data.urban_routes_url)
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.set_from()
        urbanroutepage.set_to()
        assert urbanroutepage.get_from() == data.address_from
        assert urbanroutepage.get_to() == data.address_to


    def test_2_seleccionar_tarifa_comfort(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.click_botton_pedir_un_taxi()
        assert urbanroutepage.is_tariff_selection_screen_displayed(), "No apareció aparecio la pantalla de tarifas despúes de 'Pedir un taxi'"
        urbanroutepage.seleccionar_tarifa_comfort()
        assert urbanroutepage.is_comfort_tariff_selected(),"La tarifa confort no quedo seleccionada despues del click"

    def test_3_fill_in_phone_number(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.click_number_phone()
        assert urbanroutepage.is_number_phone_selected(),"No aparecio la pantalla'Introduce tu número de teléfono'"
        urbanroutepage.introduce_number_phone()
        code = helpers.retrieve_phone_code(self.driver)
        print(code)
        urbanroutepage.introduce_sms_code(code)
        assert urbanroutepage.get_number_phone() == data.phone_number

    def test_4_payment_method(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.click_payment_method()
        assert urbanroutepage.is_payment_method_selected(),"No aparecio la pantalla 'Método de pago'"
        urbanroutepage.add_card()
        #assert urbanroutepage.is_add_card_selected(),"No aparecio la pantalla 'Agregar tarjeta'"
        urbanroutepage.introduce_card_data(data.card_number)
        assert urbanroutepage.get_number_card_data() == data.card_number
        urbanroutepage.introduce_card_code()
        assert urbanroutepage.get_number_card_code() == data.card_code
        urbanroutepage.click_add_button()
        urbanroutepage.click_close_pay_method()



    def test_5_write_a_message_for_the_driver(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.send_a_message_for_the_driver()
        message_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Traiga un aperitivo']")
        actual_message = message_field.get_attribute("value")
        expected_message = data.message_for_driver
        print(f"Mensaje obtenido: '{actual_message}'")
        assert actual_message == expected_message


    def test_6_order_blanket_and_tissues(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.order_requirements()
        assert urbanroutepage.is_order_requirement_selected(),"Manta y pañuelos no se activo"


    def test_7_order_two_ice_cream(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.order_two_ice_cream()
        assert urbanroutepage.is_order_two_ice_cream_selected(),"No se agregaron 2 helados"

    def test_8_the_option_to_search_for_a_taxi_appears(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.modal_to_search_for_a_taxi()
        assert urbanroutepage.is_modal_to_search_for_a_taxi_appears(),"No apareció el modal'Buscar automóvil'"

    def test_9_waiting_for_driver_information(self):
        urbanroutepage = UrbanRoutesPage(self.driver)
        urbanroutepage.wait_for_driver_info()
        assert urbanroutepage.wait_for_driver_info(),"No aparecio la info del conductor en 40 segundos"



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()








