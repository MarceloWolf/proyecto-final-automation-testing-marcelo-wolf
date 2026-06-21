@'
# Framework de Automatización de Pruebas - Trabajo Final Integrador

Este proyecto consiste en un framework de pruebas automatizadas desarrollado en **Python**, estructurado bajo el patrón de diseño **Page Object Model (POM)**. Incluye suites de prueba tanto para la interfaz de usuario (UI) como para servicios de API, generación de reportes dinámicos en HTML y captura automatizada de evidencia ante fallas.

##  Tecnologías Utilizadas

* **Lenguaje:** Python 3.13+
* **Framework de Testing:** Pytest (v8.2.1)
* **Automatización UI:** Selenium WebDriver (v4.21.0)
* **Pruebas de API & Simulación:** Requests & Responses (Mocking local)
* **Reportes:** Pytest-HTML

##  Estructura del Proyecto

```text
├── config/             # Configuraciones globales
├── data/               # Fuentes de datos externas
├── pages/              # Clases de Page Object Model (POM)
│   ├── base_page.py        # Métodos genéricos de Selenium
│   ├── login_page.py       # Selectores y flujos del Login
│   └── inventory_page.py   # Selectores y flujos de la Tienda
├── tests/              # Suites de prueba
│   ├── conftest.py         # Configuración del WebDriver y Hooks de captura
│   ├── test_api/           # Pruebas de Backend (GET, POST, DELETE)
│   └── test_ui/            # Pruebas de Frontend (SauceDemo)
├── pytest.ini          # Configuraciones de entorno y rutas de Pytest
└── requirements.txt    # Dependencias del proyecto
