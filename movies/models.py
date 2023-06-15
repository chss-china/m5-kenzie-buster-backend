from django.db import models
from users.models import User
class Rating_choices(models.TextChoices):
        G = 'G'
        PG = 'PG',
        PG13 = 'PG-13'
        R = 'R',
        NC17 = 'NC-17'
    
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices=Rating_choices.choices, default=Rating_choices.G,null=True)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    users = models.ManyToManyField(User, through='movies.MovieOrder', related_name='movies2')


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)