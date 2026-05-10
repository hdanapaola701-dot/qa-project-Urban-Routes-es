import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import data
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    pedir_taxi_button = (By.XPATH ,"//button[@class='button round']")
    comfort_button = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    number_phone =  (By.CLASS_NAME, "np-button")
    fill_phone = (By.XPATH,"//input[@id='phone' and @type='text']")
    sms_code_field = (By.ID, "code")
    confirm_botton =(By.XPATH, "//button[text()='Confirmar']")
    payment_method = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    card = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    number_card = (By.XPATH, "//input[@placeholder='1234 4321 1408']")
    card_code = (By.XPATH,"//input[@placeholder='12']")
    add_card_button = (By.XPATH, "//div[@class='pp-buttons']/button[text()='Agregar']")
    close_card_button = (By.CSS_SELECTOR, "div.payment-picker > div > div > button.close-button.section-close")
    message_for_the_driver = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")
    order = (By.CSS_SELECTOR, ".reqs-head")
    blanket_and_tissues = (By.XPATH, "//div[@class='switch']/span")
    ice_cream_plus_button = (By.XPATH, "//div[text()='Helado']/ancestor::div[@class='r-counter-container']//div[@class='counter-plus']")
    ice_cream_counter = (By.XPATH,"//div[text()='Helado']/ancestor::div[@class='r-counter-container']//div[@class='counter-value']")
    modal_order_taxi = (By.CSS_SELECTOR, ".smart-button-main")
    driver_info = (By.XPATH, "//div[contains(text(), 'El conductor llegará en')]")



    def __init__(self, driver):
        self.driver = driver

    def set_from(self):
        campo_desde = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.from_field))
        campo_desde.send_keys(data.address_from)

    def set_to(self):
       campo_hasta = self.driver.find_element(*self.to_field)
       campo_hasta.send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_botton_pedir_un_taxi(self ):
        botton_pedir_un_taxi = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.pedir_taxi_button))
        botton_pedir_un_taxi.click()

    def is_tariff_selection_screen_displayed(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.pedir_taxi_button)
            )
            return True
        except TimeoutException:
            return False

    def seleccionar_tarifa_comfort(self):
        botton_comfort = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.comfort_button))
        botton_comfort.click()

    def is_comfort_tariff_selected(self):
        try:
            WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(self.comfort_button)
            )
            actived_card = self.driver.find_element(*self.comfort_button)
            return actived_card.text == "Comfort"
        except TimeoutException:
            return False


    def click_number_phone(self):
        botton_number_phone = self.driver.find_element(*self.number_phone)
        botton_number_phone.click()

    def is_number_phone_selected(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.fill_phone)
            )
            return True
        except TimeoutException:
            return False

    def introduce_number_phone(self ):
        type_phone = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.fill_phone))
        type_phone.send_keys(data.phone_number)
        type_phone.send_keys(Keys.RETURN)

    def get_number_phone(self):
        return self.driver.find_element(*self.number_phone).text

    def introduce_sms_code(self, sms_code):
        code_field = self.driver.find_element(By.ID, "code")
        code_field.send_keys(sms_code)
        confirm_button = self.driver.find_element(By.XPATH, "//button[text()='Confirmar']")
        confirm_button.click()
        WebDriverWait(self.driver, 10).until( expected_conditions.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'modal')]")) )



    def click_payment_method(self):
        payment_botton = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.payment_method))
        self.driver.execute_script("arguments[0].click();", payment_botton)

    def is_payment_method_selected(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.card)
                                                )
            return True
        except TimeoutException:
            return False


    def add_card(self):
        credit_card = self.driver.find_element(*self.card)
        credit_card.click()




    def introduce_card_data(self, card_num):
        data_card = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.number_card))
        data_card.send_keys(card_num)
        data_card.send_keys(Keys.RETURN)

    def get_number_card_data(self):
        return self.driver.find_element(*self.number_card).get_attribute("value")

    def introduce_card_code(self):
        data_code = WebDriverWait(self.driver,3).until(expected_conditions.visibility_of_element_located(self.card_code))
        data_code.send_keys(data.card_code)
        data_code.send_keys(Keys.TAB)

    def get_number_card_code(self):
        return self.driver.find_element(*self.card_code).get_attribute("value")


    def click_add_button(self):
        add_button = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.add_card_button) )
        add_button.click()

    def is_card_already_added(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.number_card)
                                                )
            return True
        except TimeoutException:
            return False

    def click_close_pay_method(self):
        close_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_card_button))
        close_button.click()

    def send_a_message_for_the_driver(self):
        type_a_message = WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(self.message_for_the_driver))
        type_a_message.send_keys(data.message_for_driver)


    def order_requirements(self):
        slider_blanket_and_tissues = self.driver.find_element(*self.blanket_and_tissues)
        slider_blanket_and_tissues.click()

    def is_order_requirement_selected(self):
        try:
            checkbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.blanket_and_tissues)
                                                )
            return checkbox.is_selected
        except TimeoutException:
            return False



    def order_two_ice_cream(self):
        plus_button = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.ice_cream_plus_button))
        plus_button.click()
        time.sleep(0.3)
        plus_button.click()

    def is_order_two_ice_cream_selected(self):
        try:
            counter = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ice_cream_counter)
                                                )
            actual_value = counter.text
            print(f"The counter value is: {actual_value}")
            return actual_value == "2"
        except TimeoutException:
            return False



    def modal_to_search_for_a_taxi(self):
        modal_button =WebDriverWait(self.driver,5).until( expected_conditions.element_to_be_clickable(self.modal_order_taxi))
        modal_button.click()

    def is_modal_to_search_for_a_taxi_appears(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal_order_taxi)
                                                )
            return True
        except TimeoutException:
            return False



    def  wait_for_driver_info(self):
     information = WebDriverWait(self.driver, timeout=40).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[contains(text(), 'El conductor llegará en')]")
        )
    )

     return information.is_displayed()














