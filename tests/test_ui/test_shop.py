import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_navegacion_y_filtrado(driver):
    """Caso de Prueba 3: Verificar que se puede ingresar y visualizar la tienda."""
    login_page = LoginPage(driver)
    login_page.navigate_to()
    login_page.login_with_credentials("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    # Validamos que el contenedor de ordenamiento/filtrado esté visible en pantalla
    assert inventory_page.find_element(inventory_page.PRODUCT_SORT_CONTAINER).is_displayed(), \
        "El contenedor de productos no se desplegó correctamente."

def test_agregar_producto_al_carrito(driver):
    """Caso de Prueba 4: Agregar un artículo y validar el contador del carrito."""
    login_page = LoginPage(driver)
    login_page.navigate_to()
    login_page.login_with_credentials("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    # Agregamos la mochila al carrito
    inventory_page.add_first_product_to_cart()
    
    # Validamos que el número del ícono del carrito pase a ser "1"
    assert inventory_page.get_cart_badge_count() == "1", "El contador del carrito no se actualizó."

def test_flujo_checkout_completo(driver):
    """Caso de Prueba 5: Flujo de punta a punta hasta la pantalla de Checkout."""
    login_page = LoginPage(driver)
    login_page.navigate_to()
    login_page.login_with_credentials("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    inventory_page.add_first_product_to_cart()
    inventory_page.go_to_cart()
    
    # Avanzamos al checkout (interacciones rápidas directas sobre el carrito)
    driver.find_element(By.ID, "checkout").click()
    
    # Completamos el formulario de envío
    driver.find_element(By.ID, "first-name").send_keys("Marcelo")
    driver.find_element(By.ID, "last-name").send_keys("Wolf")
    driver.find_element(By.ID, "postal-code").send_keys("1828")
    driver.find_element(By.ID, "continue").click()
    
    # Validamos que llegamos a la página de revisión final antes de comprar
    assert "checkout-step-two.html" in driver.current_url, "No se completó el flujo hacia el checkout."