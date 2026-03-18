import json

import allure
import pytest
from faker import Faker

from dto.response.create_post_response import CreatePostResponseDto


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

    with allure.step("Прикрипление отчета"):
        pretty_json = json.dumps(first_post, indent=4, ensure_ascii=False)
        allure.attach(
            pretty_json,
            name="Пример первого поста",
            attachment_type=allure.attachment_type.JSON
        )

@allure.epic("API Тестирование")
@allure.feature("Ресурс Posts")
@allure.story("Создание поста")
@allure.title("Успешное создание поста")
@allure.tag("smoke", "api", "regress")
@pytest.mark.api
def test_create_post(posts_client):
    """
    Кейс 1 (Легкий): Создание поста
    1. Отправить POST запрос на /posts с тестовыми данными.
    3. Проверить, что статус код вернулся 201.
    4. Проверить, что данные сохранены корректно.
    """

    faker_obj = Faker()

    title = faker_obj.sentence()
    body = faker_obj.sentence()
    user_id = faker_obj.random_int(min=1, max=100)

    with allure.step("Отправка POST запроса на /posts"):
        response = posts_client.create_post(title=title, body=body, user_id=user_id)
        response_json = response.json()
        post_data = CreatePostResponseDto(**response_json)

    with allure.step("Проверка статус кода"):
        assert response.status_code == 201

    with allure.step("Проверка ответа, что пришел не пустой объект"):
        assert post_data.id is not None
        assert post_data.title == title, f"Ожидался title '{title}', но пришел '{post_data.title}'"
        assert post_data.body == body, f"Ожидался body '{body}', но пришел '{post_data.body}'"
        assert post_data.user_id == user_id, f"Ожидался user_id '{user_id}', но пришел '{post_data.user_id}'"

    with allure.step("Прикрипление отчета"):
        pretty_json = json.dumps(response_json, indent=4, ensure_ascii=False)
        allure.attach(
            pretty_json,
            name="Ответ при создании поста",
            attachment_type=allure.attachment_type.JSON
        )