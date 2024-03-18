from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    page = models.IntegerField()

    def __str__(self) -> str:
        return self.title
