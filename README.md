# hw05_final - Проект спринта: подписки на авторов, спринт 6 в Яндекс.Практикум

## Спринт 6 - Проект спринта: подписки на авторов

### hw05_final - Проект спринта: подписки на авторов, Яндекс.Практикум.

TODO

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/themasterid/hw05_final.git
```

или

```bash
git clone git@github.com:themasterid/hw05_final.git
```

Переходим в папку с проектом:

```bash
cd hw05_final
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube/manage.py createsuperuser
```

При желании делаем коллекцию статики:

```bash
python yatube/manage.py collectstatic
```

Предварительно сняв комментарий с:
```bash
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

И закомментировав: 
```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

Иначе получим ошибку: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Для запуска тестов выполним:

```bash
pytest
```

Получим:

```bash

pytest
ОТРЕДАКТИРОВАТЬ ПОСЛЕ УСТРАНЕНИЯ
FAILED tests/test_create.py::TestCreateView::test_create_view_get - AssertionError: Проверьте, чт...
FAILED tests/test_homework.py::TestGroupView::test_group_view - AssertionError: Отредактируйте HT...
FAILED tests/test_post.py::TestPostEditView::test_post_edit_view_author_get - AssertionError: Про...
============================ 3 failed, 17 passed, 33 warnings in 2.98s ============================ 
```

Запускаем проект:

```bash
python yatube/manage.py runserver localhost:80
```

После чего проект будет доступен по адресу http://localhost/

Заходим в http://localhost/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Автор: [Дмитрий Клепиков](https://github.com/themasterid) :+1:
