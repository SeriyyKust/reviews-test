# Review-Logs
Сервис в реальном времени собирает отзывы пользователей и определяет статус отзыва: *положительный*, *отрицательный*, *нейтральный*.


## Установка зависимостей и запуск приложения

**Для локальной установки зависимостей используется *poetry***
```bash
git clone https://github.com/SeriyyKust/reviews-test.git
cd reviews-test
poetry install
poetry shell
cd src
uvicorn main:app --reload
```

На данный момент переменные окружения не используются - их настраивать не нужно


## Документация API

Документация доступна по адресу:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


## Основные эндпоинты

- `GET /reviews?sentiment` — получить отзывов определённого sentiment
- `POST /reviews` — создать новый отзыв

Пример запроса создания позитивного отзыва:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Данный сервис работает отлично и хорошо"
}'
```

Пример запрос получения отрицательных отзывов
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/reviews/?sentiment=negative' \
  -H 'accept: application/json'
```


## Тестирование

Запуск тестов происходи из основной директории reviews:
```bash
pytest tests/
```