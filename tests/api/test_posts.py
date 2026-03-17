import json

import allure
import pytest

@allure.epic("API Тестирование")
@allure.feature("Ресурс Posts")
@allure.story("Получение списка")
@allure.title("Успешное получение списка всех постов")
@allure.tag("smoke", "api", "regress")
@pytest.mark.api
def test_get_all_posts(posts_client):
    """
    Кейс 1 (Легкий): Получение списка ресурсов (GET List)
    1. Отправить GET запрос на /posts.
    2. Проверить, что статус код 200.
    3. Проверить, что ответ это список (массив) и он не пустой.
    """

    with allure.step("Отправка GET запроса на /posts"):
        response = posts_client.get_all_posts()

    with allure.step("Проверка статус кода, ожидаем = 200"):
        assert response.status_code == 200

    with allure.step("Проверка, что ответ это непустой список"):
        response_json = response.json()

        assert isinstance(response_json, list), "Ответ должен быть списком (массивом)"

        assert len(response_json) > 0, "Список постов пришел пустой"

        first_post = response_json[0]

        pretty_json = json.dumps(first_post, indent=4, ensure_ascii=False)
        allure.attach(
            pretty_json,
            name="Пример первого поста",
            attachment_type=allure.attachment_type.JSON
        )