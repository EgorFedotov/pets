# Запуск проекта:

### Клонируем репозиторий к себе на ПК

```bash
    git git@github.com:EgorFedotov/pets.git
```

### В корне проекта создаем файл .env

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)

### Запускаем докер

```bash
    docker-compose up -d
```

### Выполнеям миграции:

```bash
    docker compose exec web python manage.py makemigrations
    docker compose exec web python manage.py migrate
    
```

# Создаем пользователя 

на эндпоит http://127.0.0.1:8000/api/auth/users/ отправлеям post запрос для регистрации пользователя

пример: 

{
    "username": "egorka",
    "password": "Test125gde",
    "email": "egork@gmail.com"
}

для получения токена отправляем post запрос на http://127.0.0.1:8000/api/auth/jwt/create/ с логином и паролем,
access токен нужно передовать в заголовке каждого запроса в поле Authorization Перед самим токеном должно стоять ключевое слово Bearer и пробел.
