from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    CATEGORIES_CHOICES = (('music', 'Muzyka'),('science', 'Nauka'), ('sport', 'Sprzęt'), ('others', 'Inne'))
    categories = models.CharField(max_length=200, default='Inne')
    author_invisible = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
