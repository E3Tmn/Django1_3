from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    short_description = models.TextField('Краткое описание')
    long_description = models.TextField('Описание')
    longitude = models.DecimalField('Долгота', max_digits=17, decimal_places=14)
    latitude = models.DecimalField('Широта', max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title
    

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField('Фото')

    def __str__(self):
        return f'{self.id} {self.place.title}'
