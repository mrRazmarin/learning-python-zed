import json

import allure
import pytest
from faker import Faker

from dto.response.create_post_response import CreatePostResponseDto
from dto.response.single_post_response import SinglePostResponseDto


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

    with allure.step("Прикрепление отчета"):
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
    Кейс 2 (Легкий): Создание поста
    1. Отправить POST запрос на /posts с тестовыми данными.
    2. Проверить, что статус код вернулся 201.
    3. Проверить, что данные сохранены корректно.
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

    with allure.step("Прикрепление отчета"):
        pretty_json = json.dumps(response_json, indent=4, ensure_ascii=False)
        allure.attach(
            pretty_json,
            name="Ответ при создании поста",
            attachment_type=allure.attachment_type.JSON
        )

@allure.epic("API Тестирование")
@allure.feature("Ресурс Posts")
@allure.story("Получение поста по id")
@allure.title("Успешное получение поста")
@allure.tag("smoke", "api", "regress")
@pytest.mark.api
def test_get_post_by_id(posts_client):
    """
    Кейс 3 (Легкий): Получение поста по переданному id
    1. Отправить GET запрос на /posts/{id}.
    2. Проверить, что статус код вернулся 200.
    3. Проверить, что в полученных полях не пустые значения.
    """
    faker = Faker()
    query_parameter_id = faker.random_int(min=1, max=100)

    with allure.step(f"Отправка GET запроса на /posts/{query_parameter_id}"):
        response = posts_client.get_post_by_id(query_parameter_id)
        response_json = response.json()
        get_data = SinglePostResponseDto(**response_json)

    with allure.step("Проверка статус кода"):
        assert response.status_code == 200, f"Ожидался статус код = 200, но пришел '{response.status_code}'"

    with allure.step("Проверка полученных полей"):
        assert get_data.id == query_parameter_id, f"Ожидался id-поста = '{query_parameter_id}', но вернулся = '{get_data.id}'"
        assert get_data.title != "", f"Ожидалось, что title будет не пустым, но title вернулось пустое"
        assert get_data.body != "", f"Ожидалось, что body будет не пустым, но body вернулось пустое"
        assert  get_data.user_id is not None, f"Ожидалось, что userId будет не пустым, но userId вернулось пустое"

    with allure.step("Прикрепление отчета"):
        pretty_json = json.dumps(response_json, indent=4, ensure_ascii=False)
        allure.attach(
            pretty_json,
            name="Полученный пост",
            attachment_type=allure.attachment_type.JSON
        )