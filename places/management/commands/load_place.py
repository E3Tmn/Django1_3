from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает информацию о компаниях в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('link', help='Вставьте ссылку на json файл')

    def handle(self, *args, **options):
        response = requests.get(options['link'])
        response.raise_for_status()
        raw_response = response.json()
        place, created = Place.objects.get_or_create(
            title=raw_response['title'],
            longitude=raw_response['coordinates']['lng'],
            latitude=raw_response['coordinates']['lat'],
            defaults={
                'short_description': raw_response['description_short'],
                'long_description':raw_response['description_long']}
        )
        place_images = raw_response['imgs']
        
        for num, image_link in enumerate(place_images):
            try:
                response = requests.get(image_link)
                response.raise_for_status()
                image = Image.objects.get_or_create(place=place, order=num)
                image[0].image.save(
                    f'{num}.jpg',
                    ContentFile(response.content),
                    save=True
                )
            except requests.exceptions.HTTPError as err:
                print(f'HTTP error occurred: {err}')
            except requests.exceptions.ConnectionError as conerr: 
                print("Connection error") 
