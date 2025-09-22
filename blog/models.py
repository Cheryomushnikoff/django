from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, ) # verbose_name=
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog_posts'
