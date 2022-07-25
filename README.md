# hw05_final - Проект спринта: подписки на авторов, спринт 6 в Яндекс.Практикум

## Спринт 6 - Проект спринта: подписки на авторов

### hw05_final - Проект спринта: подписки на авторов, Яндекс.Практикум.

Покрытие тестами проекта Yatube из спринта 6 Питон-разработчика бекенда Яндекс.Практикум. Все что нужно, это покрыть тестами проект, в учебных целях. Реализована система подписок/отписок на авторов постов.

### **ЗАМЕЧАНИЕ**:
* Не работает статика должным образом, пофиксить, переходом на Django 3 или 4

Стек:

- Python 3.10.5
- Django==2.2.28
- mixer==7.1.2
- Pillow==9.0.1
- pytest==6.2.4
- pytest-django==4.4.0
- pytest-pythonpath==0.7.3
- requests==2.26.0
- six==1.16.0
- sorl-thumbnail==12.7.0
- Pillow==9.0.1
- django-environ==0.8.1

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

При желании делаем коллекцию статики (часть статики уже загружена в репозиторий в виде исключения):

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
=================================================== test session starts ===================================================
platform win32 -- Python 3.10.5, pytest-6.2.4, py-1.11.0, pluggy-0.13.1 -- ...\hw05_final\venv\Scripts\python.exe     
django: settings: yatube.settings (from ini)
rootdir: ...\hw05_final, configfile: pytest.ini, testpaths: tests/
plugins: Faker-6.0.0, django-4.4.0, pythonpath-0.7.3
collected 31 items

tests/test_paginator.py::TestGroupPaginatorView::test_group_paginator_view_get PASSED                                [  3%]
tests/test_paginator.py::TestGroupPaginatorView::test_group_paginator_not_in_context_view PASSED                     [  6%]
tests/test_paginator.py::TestGroupPaginatorView::test_index_paginator_not_in_view_context PASSED                     [  9%]
tests/test_paginator.py::TestGroupPaginatorView::test_index_paginator_view PASSED                                    [ 12%]
tests/test_paginator.py::TestGroupPaginatorView::test_profile_paginator_view PASSED                                  [ 16%]
tests/test_about.py::TestTemplateView::test_about_author_tech PASSED                                                 [ 19%] 
tests/test_auth_urls.py::TestAuthUrls::test_auth_urls PASSED                                                         [ 22%]
tests/test_comment.py::TestComment::test_comment_add_view PASSED                                                     [ 25%]
tests/test_comment.py::TestComment::test_comment_add_auth_view PASSED                                                [ 29%]
tests/test_create.py::TestCreateView::test_create_view_get PASSED                                                    [ 32%]
tests/test_create.py::TestCreateView::test_create_view_post PASSED                                                   [ 35%]
tests/test_follow.py::TestFollow::test_follow_not_auth PASSED                                                        [ 38%]
tests/test_follow.py::TestFollow::test_follow_auth PASSED                                                            [ 41%]
tests/test_homework.py::TestPost::test_post_create PASSED                                                            [ 45%]
tests/test_homework.py::TestGroup::test_group_create PASSED                                                          [ 48%]
tests/test_homework.py::TestGroupView::test_group_view PASSED                                                        [ 51%]
tests/test_homework.py::TestCustomErrorPages::test_custom_404 PASSED                                                 [ 54%]
tests/test_homework.py::TestCustomErrorPages::test_custom_500 PASSED                                                 [ 58%] 
tests/test_homework.py::TestCustomErrorPages::test_custom_403 PASSED                                                 [ 61%]
tests/test_post.py::TestPostView::test_index_post_with_image PASSED                                                  [ 64%]
tests/test_post.py::TestPostView::test_index_post_caching PASSED                                                     [ 67%]
tests/test_post.py::TestPostView::test_post_view_get PASSED                                                          [ 70%]
tests/test_post.py::TestPostEditView::test_post_edit_view_get PASSED                                                 [ 74%]
tests/test_post.py::TestPostEditView::test_post_edit_view_author_get PASSED                                          [ 77%]
tests/test_post.py::TestPostEditView::test_post_edit_view_author_post PASSED                                         [ 80%]
tests/test_profile.py::TestProfileView::test_profile_view_get PASSED                                                 [ 83%]
tests/test_comment.py::TestComment::test_comment_model PASSED                                                        [ 87%]
tests/test_follow.py::TestFollow::test_follow PASSED                                                                 [ 90%] 
tests/test_homework.py::TestPost::test_post_model PASSED                                                             [ 93%] 
tests/test_homework.py::TestPost::test_post_admin PASSED                                                             [ 96%] 
tests/test_homework.py::TestGroup::test_group_model PASSED                                                           [100%] 

============================================== 31 passed in 5.86s ==============================================
```

Запускаем проект:

```bash
python yatube/manage.py runserver localhost:80
```

После чего проект будет доступен по адресу http://localhost/

Заходим в http://localhost/admin и создаем группы и записи.
После чего записи и группы появятся на главной странице.

Автор: [Дмитрий Клепиков](https://github.com/themasterid) :+1:
