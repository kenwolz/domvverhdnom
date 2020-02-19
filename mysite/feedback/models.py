from django.db import models
from django.conf import settings

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=35)
    phone = models.CharField('Номер телефона', max_length=30)
    description = models.CharField('Желаемые дата и время посещения', max_length=30, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'


class View(models.Model):
    pass
