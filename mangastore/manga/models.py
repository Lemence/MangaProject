from django.db import models



class Manga(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название манги')
    translated_name = models.CharField(max_length=256, verbose_name='Перевод названия', default=name)
    author_name = models.CharField(max_length=256, verbose_name='Автор манги')
    release_date = models.DateField(verbose_name='Дата выхода', default=None)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'

    def __str__(self):
        return self.name

