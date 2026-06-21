from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """Constructor de la página base que recibe el driver del navegador."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Espera explícita de hasta 10 segundos

    def open_url(self, url):
        """Abre una URL específica en el navegador."""
        self.driver.get(url)

    def find_element(self, locator):
        """Espera a que un elemento sea visible en la pantalla y lo retorna."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Espera a que un elemento sea cliqueable y hace clic en él."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def write_text(self, locator, text):
        """Busca un campo de texto, lo limpia e ingresa el texto indicado."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Obtiene el texto visible de un elemento en pantalla."""
        return self.find_element(locator).text