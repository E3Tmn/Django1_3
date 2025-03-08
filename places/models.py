from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание', blank=True)
    long_description = HTMLField('Описание', blank=True)
    longitude = models.DecimalField('Долгота',
                                    max_digits=17,
                                    decimal_places=14)
    latitude = models.DecimalField('Широта', max_digits=17, decimal_places=14)

    class Meta:
        unique_together = [['title', 'longitude', 'latitude']]


    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              verbose_name='Место',
                              related_name='images')
    image = models.ImageField('Фото')
    order = models.IntegerField('Номер',
                                default=0,
                                db_index=True)

    def __str__(self):
        return f'{self.id} {self.place.title}'
