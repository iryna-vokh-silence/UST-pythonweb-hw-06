# UST-pythonweb-hw-06
# Домашнє завдання №6: SQLAlchemy, Alembic та PostgreSQL

Цей проєкт реалізує реляційну базу даних для навчального закладу з використанням **SQLAlchemy ORM**. Система дозволяє керувати даними про студентів, викладачів, групи, предмети та оцінки.

## Технологічний стек
* **Python 3.9+**
* **SQLAlchemy** (ORM для роботи з БД)
* **Alembic** (керування міграціями)
* **PostgreSQL** (база даних у Docker-контейнері)
* **Faker** (генерація тестових даних)

## Структура бази даних
Схема містить 5 таблиць:
1. `groups` — навчальні групи.
2. `students` — студенти, пов'язані з групами.
3. `teachers` — викладачі.
4. `subjects` — предмети із вказівкою викладача.
5. `grades` — оцінки студентів з предмета із датою отримання.

[Image of relational database schema for university management system]

## Як запустити проєкт

### 1. Запуск бази даних
Для роботи проєкту необхідно запустити контейнер PostgreSQL:
```bash
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres