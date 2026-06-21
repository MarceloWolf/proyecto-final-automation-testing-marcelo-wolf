from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Localizadores de los elementos de la tienda
    FIRST_PRODUCT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_SORT_CONTAINER = (By.CSS_SELECTOR, "[data-test='product-sort-container']")

    def __init__(self, driver):
        super().__init__(driver)

    def add_first_product_to_cart(self):
        """Agrega el primer producto (la mochila) al carrito"""
        self.click_element(self.FIRST_PRODUCT_ADD_BUTTON)

    def get_cart_badge_count(self):
        """Devuelve el número de productos que muestra el ícono del carrito"""
        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        """Hace clic en el ícono del carrito para ir a ver la orden"""
        self.click_element(self.CART_LINK)