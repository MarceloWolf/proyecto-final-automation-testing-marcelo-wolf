from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # 1. Definimos los localizadores (elementos de la interfaz de saucedemo.com)
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_CONTAINER = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        """Hereda el constructor y el driver de BasePage"""
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def navigate_to(self):
        """Navega directo a la URL de SauceDemo"""
        self.open_url(self.url)

    def login_with_credentials(self, username, password):
        """Realiza el flujo completo de ingresar datos y apretar el botón"""
        self.write_text(self.USERNAME_INPUT, username)
        self.write_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Devuelve el mensaje de error si las credenciales fallan (Escenario Negativo)"""
        return self.get_text(self.ERROR_CONTAINER)