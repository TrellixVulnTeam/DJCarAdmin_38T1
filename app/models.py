from django.db import models


class Car(models.Model):
    db_table = 'app_car'
    brand = models.CharField(max_length=50, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    review_count.short_description = "Количество обзоров"

    class Meta:
        ordering = ["id"]
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


Car.short_description = "Автомобили"


class Review(models.Model):
    db_table = 'app_review'
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    text = models.TextField(null=True)

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        ordering = ["id"]
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
