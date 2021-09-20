from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.post = Post.objects.create(
            text='Тестовый текст больше 15 символов для проверки...',
            author=cls.user,
        )

    def test_post_str(self):
        """Проверка __str__ у post."""
        self.assertEqual(self.post.text[:15], str(self.post))

    def test_post_verbose_name(self):
        """Проверка verbose_name у post."""
        field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группа', }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.post._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)

    def test_post_help_text(self):
        """Проверка help_text у post."""
        feild_help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост', }
        for value, expected in feild_help_texts.items():
            with self.subTest(value=value):
                help_text = self.post._meta.get_field(value).help_text
                self.assertEqual(help_text, expected)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )

    def test_group_str(self):
        """Проверка __str__ у group."""
        self.assertEqual(self.group.title, str(self.group))

    def test_group_verbose_name(self):
        """Проверка verbose_name у group."""
        field_verboses = {
            'title': 'Заголовок',
            'slug': 'ЧПУ',
            'description': 'Описание',
        }
        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                verbose_name = self.group._meta.get_field(value).verbose_name
                self.assertEqual(verbose_name, expected)
