```markdown
# Альпинистский клуб: Учёт восхождений

Проект представляет собой информационную систему для альпинистского клуба, которая позволяет вести учёт восхождений, управлять данными об альпинистах и горах, а также формировать отчёты и аналитические выборки. Система разработана с использованием Django, PostgreSQL и Docker.

---

## Установка и настройка проекта

### 1. Требования

Для запуска проекта необходимо установить:
- **Docker** ([инструкция по установке](https://docs.docker.com/get-docker/))
- **Docker Compose** ([инструкция по установке](https://docs.docker.com/compose/install/))

---

### 2. Клонирование репозитория

Склонируйте репозиторий с проектом:

```bash
git clone git@github.com:Rijo-ru/alpine_club.git
cd alpine_club
```

---

### 3. Настройка окружения

Создайте файл `.env` в корневой директории проекта и добавьте в него следующие переменные:

```env
POSTGRES_DB=alpineclub
POSTGRES_USER=alpineuser
POSTGRES_PASSWORD=alpinepassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

---

### 4. Запуск проекта

1. Соберите и запустите контейнеры:

   ```bash
   docker compose up --build
   ```

2. После запуска контейнеров выполните миграции:

   ```bash
   docker compose exec web python manage.py migrate
   ```

3. Создайте суперпользователя для доступа к административной панели:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

4. Загрузите тестовые данные в базу данных:

   ```bash
   docker compose exec web python load_data.py
   ```

---

### 5. Доступ к проекту

- **Веб-интерфейс:** Перейдите по адресу `http://localhost:8000/`.
- **Административная панель:** Перейдите по адресу `http://localhost:8000/admin/` и войдите с учётными данными суперпользователя.

---

### 6. Подключение к базе данных через pgAdmin

1. Установите pgAdmin ([официальный сайт](https://www.pgadmin.org/)).
2. Подключитесь к базе данных:
   - **Host:** `localhost`
   - **Port:** `5432`
   - **Database:** `alpineclub`
   - **Username:** `alpineuser`
   - **Password:** `alpinepassword`

---

### 7. Остановка проекта

Чтобы остановить контейнеры, выполните:

```bash
docker compose down
```

---

### 8. Дополнительные команды

- **Пересборка контейнеров:** `docker compose up --build`
- **Просмотр логов:** `docker compose logs -f`
- **Очистка данных:** Удалите том `postgres_data` с помощью команды `docker volume rm alpine_club_postgres_data`.

```