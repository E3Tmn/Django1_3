from django.shortcuts import render
from places.models import Place, Image

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
            "detailsUrl": "static/places/moscow_legends.json"
          }
        } for place in db_places
      ] 
    }
    data = {'places':geojson_places}
    return render(request, 'index.html', context=data)