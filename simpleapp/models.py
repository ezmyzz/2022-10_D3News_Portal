from django.db import models
from django.core.validators import MinValueValidator


class News(models.Model):
    name = models.CharField(
        max_length=50,
        # """ unique=False,  # названия товаров не должны повторяться """
    )
    description = models.TextField()
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',  # все новости в категории будут доступны через поле news
    )
    some_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()}: {self.description} --------  {self.some_datetime}'


# Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
