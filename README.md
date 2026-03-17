# 🚀 Python API Automation Framework

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Latest-green.svg)
![Allure](https://img.shields.io/badge/Allure-Report-red.svg)

> 🧠 Промышленный фреймворк для автоматизации тестирования API на Python. 
> Проект демонстрирует лучшие практики (Best Practices): чистую архитектуру, 
> паттерн Page Object (в применении к API), использование Pytest с фикстурами и генерацию детальных отчетов в Allure.

> Цель — построить понимание написания фреймворка для автоматизированного тестирования backend'а с нуля.

---

## 📦 Технологический стек
*   **Python 3.13+**: Язык программирования.
*   **Pytest**: Фреймворк для запуска тестов и управления фикстурами.
*   **Requests**: Библиотека для выполнения HTTP-запросов.
*   **Allure Report**: Инструмент для построения красивых и интерактивных отчетов.

---

## 🏗 Архитектура проекта

Проект разделен на логические слои для поддержки масштабируемости и читаемости кода.

```text
my_pet_project/
├── config/                 # Конфигурация
│   └── settings.py         # Базовый URL и переменные окружения
├── src/                    # Исходный код (Business Logic)
│   └── api/                # API клиенты (Обертки над requests)
│       ├── base_client.py  # Базовый класс сессии
│       └── posts.py        # Клиент для ресурса /posts
├── tests/                  # Тесты
│   ├── api/                # Тесты API
│   │   └── test_posts.py   
│   └── conftest.py         # Глобальные фикстуры Pytest
├── allure_results/         # (Генерируется) Сырые данные для отчета
├── pytest.ini              # Настройки Pytest
├── requirements.txt        # Зависимости проекта
└── README.md
```

---

## 🚀 Установка и настройка

### 1. Клонирование репозитория
```bash
git clone <your-repo-url>
cd my_pet_project
```

### 2. Создание виртуального окружения (рекомендуется)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Установка Allure Commandline
Для просмотра отчетов необходима утилита Allure.

*   **macOS:** `brew install allure`
*   **Windows (Chocolatey):** `choco install allure`
*   **Скачивание:** [GitHub Releases](https://github.com/allure-framework/allure2/releases)

---

## 🏃 Как запускать тесты

### Запуск всех тестов
```bash
pytest
```

### Запуск конкретного файла
```bash
pytest tests/api/test_posts.py
```

### Запуск с фильтром по метке
```bash
pytest -m smoke
```

---

## 📊 Просмотр отчета (Allure)

После запуска тестов в папке `allure_results` появятся файлы с данными. Чтобы просмотреть отчет в браузере:

1.  **Режим реального времени (авто-обновление):**
    ```bash
    allure serve allure_results
    ```

2.  **Генерация статического HTML:**
    ```bash
    allure generate allure_results --clean -o allure_report
    allure open allure_report
    ```

---

## ✨ Реализованные функции (MVP)

На текущий момент в фреймворке реализован базовый функционал для работы с API:

- [x] **Базовый API Клиент**: Абстракция над `requests.Session`, автоматическое склеивание URL.
- [x] **Клиент Posts**: Методы для получения всех постов, получения по ID и создания нового.
- [x] **Конфигурация**: Вынесение `BASE_URL` в настройки.
- [x] **Фикстуры**: Подготовка API-клиента через `conftest.py` (Dependency Injection).
- [x] **Allure интеграция**: Декораторы `@allure.epic`, `@allure.step` и аттачменты JSON.
- [x] **Кейсы**:
    - Успешное получение списка постов (200 OK).
    - Проверка структуры данных (валидация типов).

---


## 📝 Пример кода

Пример того, насколько чистым стал тест благодаря архитектуре:

```python
@allure.title("Успешное получение списка всех постов")
def test_get_all_posts(posts_client):
    # Act (Действие)
    with allure.step("Отправка GET запроса"):
        response = posts_client.get_all_posts()

    # Assert (Проверка)
    with allure.step("Проверка статуса и данных"):
        assert response.status_code == 200
        assert len(response.json()) > 0
```

---

## 🔜 Планы развития

*   [ ] Добавить параметризацию тестов.
*   [ ] Реализовать негативные проверки (400, 404, 500).
*   [ ] Добавить валидацию JSON-схем (Pydantic / Jsonschema).
*   [ ] Интеграция с CI/CD (GitHub Actions).
*   [ ] Добавить UI-тесты с Playwright.


---
## 👨‍💻 Автор
Создано в рамках обучения промышленной автоматизации тестирования.