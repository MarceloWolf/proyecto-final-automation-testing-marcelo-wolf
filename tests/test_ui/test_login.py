import pytest
from pages.login_page import LoginPage

def test_login_exitoso(driver):
    """Caso de Prueba 1: Verificar el login correcto con un usuario estándar."""
    login_page = LoginPage(driver)
    
    # 1. Navegar a la página
    login_page.navigate_to()
    
    # 2. Iniciar sesión con el usuario válido de SauceDemo
    login_page.login_with_credentials("standard_user", "secret_sauce")
    
    # 3. Validación (Assertion): Si entramos bien, la URL debe cambiar a la del inventario
    assert "inventory.html" in driver.current_url, "No se redireccionó a la página de inventario tras el login."

def test_login_credenciales_invalidas(driver):
    """Caso de Prueba 2 (Escenario Negativo): Verificar el manejo de error con credenciales incorrectas."""
    login_page = LoginPage(driver)
    
    # 1. Navegar a la página
    login_page.navigate_to()
    
    # 2. Intentar iniciar sesión con datos inválidos
    login_page.login_with_credentials("usuario_invalido", "clave_falsa")
    
    # 3. Validación (Assertion): Comprobar que aparezca el cartel de error esperado
    mensaje_error = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in mensaje_error, \
        f"El mensaje de error no es el esperado. Se obtuvo: {mensaje_error}"