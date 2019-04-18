from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=2000)
    brief = models.CharField(max_length=2000, default='')
    content = models.TextField(default='')
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
