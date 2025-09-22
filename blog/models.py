from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = 'blog_posts'
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    created_at =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        db_table = 'blog_users'

