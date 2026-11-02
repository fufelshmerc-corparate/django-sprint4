# Блогикум

Учебный блог на Django: публикации, категории, комментарии, регистрация и страницы профиля.

Проект рассчитан на Python 3.12 и Django 5.1.

## Запуск

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py loaddata ../db.json
python manage.py runserver
```

Главная страница: http://127.0.0.1:8000/

Демо-пользователи из `db.json` (пароль в учебном дампе не опубликован, его можно задать через `createsuperuser` или админку):

- `admin` — администратор
- `leo`, `anton`, `alex` — авторы публикаций

## Проверки

Из корня репозитория, с активированным виртуальным окружением:

```bash
pytest
flake8
```

Письма (сброс пароля) сохраняются в `blogicum/sent_emails/`. Каталоги `venv/`, `media/`, `sent_emails/` и файл `db.sqlite3` не коммитятся.
