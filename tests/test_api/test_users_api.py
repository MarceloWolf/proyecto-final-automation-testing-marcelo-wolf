import pytest
import requests
import responses

BASE_URL = "https://reqres.in/api"

@responses.activate
def test_get_users_list():
    """Caso de Prueba API 1: Método GET - Validar listado de usuarios simulando código 200."""
    # Configuramos la respuesta simulada
    responses.add(
        responses.GET,
        f"{BASE_URL}/users?page=2",
        json={"page": 2, "data": [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael"}]},
        status=200
    )
    
    response = requests.get(f"{BASE_URL}/users?page=2")
    
    # 1. Validar código de estado HTTP 200 (OK)
    assert response.status_code == 200, f"Se esperaba 200 pero se obtuvo {response.status_code}"
    
    # 2. Validar estructura del JSON
    json_data = response.json()
    assert "page" in json_data, "Falta el campo 'page' en la respuesta"
    assert "data" in json_data, "Falta el campo 'data' en la respuesta"
    assert len(json_data["data"]) > 0, "La lista de usuarios vino vacía"


@responses.activate
def test_create_user_post():
    """Caso de Prueba API 2: Método POST - Crear un usuario simulando código 201."""
    payload = {
        "name": "Marcelo Wolf",
        "job": "Functional Analyst & QA Automation"
    }
    
    # Configuramos la respuesta simulada del POST
    responses.add(
        responses.POST,
        f"{BASE_URL}/users",
        json={"name": "Marcelo Wolf", "job": "Functional Analyst & QA Automation", "id": "123"},
        status=201
    )
    
    response = requests.post(f"{BASE_URL}/users", json=payload)
    
    # 1. Validar código de estado HTTP 201 (Created)
    assert response.status_code == 201, f"Se esperaba 201 pero se obtuvo {response.status_code}"
    
    # 2. Validar que los datos enviados coincidan con la respuesta
    json_data = response.json()
    assert json_data["name"] == payload["name"], "El nombre en la respuesta no coincide"
    assert json_data["job"] == payload["job"], "El puesto en la respuesta no coincide"
    assert "id" in json_data, "La API no retornó un ID para el usuario creado"


@responses.activate
def test_delete_user():
    """Caso de Prueba API 3: Método DELETE - Eliminar un usuario simulando código 204."""
    # Configuramos la respuesta simulada del DELETE (No devuelve contenido)
    responses.add(
        responses.DELETE,
        f"{BASE_URL}/users/2",
        status=204
    )
    
    response = requests.delete(f"{BASE_URL}/users/2")
    
    # 1. Validar código de estado HTTP 204 (No Content)
    assert response.status_code == 204, f"Se esperaba 204 pero se obtuvo {response.status_code}"