from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import Place, Image


def show_detail_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    info_place = JsonResponse(
        {
            "title": place.title,
            "imgs": [picture.image.url for picture in place.images.all()],
            "description_short": place.short_description,
            "description_long": place.long_description,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude
            }
        }, json_dumps_params={'ensure_ascii': False}
    )
    return info_place


def show_startpage(request):
    db_places = Place.objects.all()
    geojson_places = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse(
                show_detail_place,
                kwargs={'place_id': place.id}
            )
          }
        } for place in db_places
      ]
    }
    data = {'places': geojson_places}
    return render(request, 'index.html', context=data)
