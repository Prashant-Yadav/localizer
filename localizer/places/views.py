
from googleplaces import GooglePlaces, types, lang

from django.shortcuts import render


def index(request):
    return render(request, 'places/index.html')


def search(request):
    placename = request.POST['place']
    key = ' AIzaSyC02yzQWsAxkdaWn8p9ALV7nTthZvjannw'

    google_places = GooglePlaces(key)

    query_result = google_places.nearby_search(location=placename, radius=20000,
                                              types=[
                                                  types.TYPE_FOOD,
                                                  types.TYPE_GYM,
                                                  types.TYPE_HINDU_TEMPLE,
                                                  types.TYPE_HOSPITAL]
                                              )

    for place in query_result.places:
        # The following method has to make a further API call.'''
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.

        for photo in place.photos:
        	photo.get(maxheight=500, maxwidth=500)

    context = {
    	'location' : placename,
    	'places' : query_result.places,
    }

    return render(request, 'places/search.html', context)
