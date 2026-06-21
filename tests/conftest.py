import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """
    Fixture que inicializa el WebDriver de Chrome antes de cada test
    y se asegura de cerrarlo al finalizar.
    """
    # Configuramos opciones del navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Abre la ventana maximizada
    options.add_argument("--incognito")        # Modo incógnito para limpiar cookies
    
    # Inicializamos el navegador Chrome (Selenium 4 ya lo descarga solo si hace falta)
    driver = webdriver.Chrome(options=options)
    
    # Espera implícita de 10 segundos por si algún elemento tarda en cargar
    driver.implicitly_wait(10)
    
    # 'yield' le pasa el navegador al test que lo necesite
    yield driver
    
    # Una vez que el test termina (pase o falle), se ejecuta esto y cierra el navegador
    driver.quit()