from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=256)
    preview = models.TextField(max_length=516)
    content = models.TextField(max_length=1024)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.title
