import pytest_html
import os
from datetime import datetime
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    """Fixture que inicializa y cierra el WebDriver de Chrome."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest que intercepta el resultado de cada prueba.
    Si una prueba de UI falla, toma una captura de pantalla y la suma al reporte HTML.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        # Verificamos si el test falló y si tenía el driver de Selenium activo
        if (report.failed and not xfail) or (report.skipped and xfail):
            if "driver" in item.fixturenames:
                driver_fixture = item.funcargs.get("driver")
                if driver_fixture:
                    # Crear carpeta de capturas si no existe
                    os.makedirs("assets", exist_ok=True)
                    
                    # Nombre del archivo con fecha, hora y nombre del test
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    test_name = item.name
                    screenshot_path = f"assets/{test_name}_{timestamp}.png"
                    
                    # Tomar la captura
                    driver_fixture.save_screenshot(screenshot_path)
                    
                    # Incrustar la captura en el reporte HTML de Pytest
                    html = f'<div><img src="{screenshot_path}" alt="screenshot" style="width:304px;height:228px;" ' \
                           f'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))
                    
        report.extra = extra