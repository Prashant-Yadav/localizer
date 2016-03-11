
from googleplaces import GooglePlaces, types, lang

from django.shortcuts import render


def index(request):
    return render(request, 'places/index.html')


def navbar_info(request):
    return render(request, 'places/navbar.html')


def search(request):
    placename = request.POST['place']
    '''
    key = ' AIzaSyC02yzQWsAxkdaWn8p9ALV7nTthZvjannw'

    google_places = GooglePlaces(key)

    TYPES = [
        types.TYPE_FOOD,
        types.TYPE_GYM,
        types.TYPE_HINDU_TEMPLE,
        types.TYPE_HOSPITAL
    ]

    query_result = google_places.nearby_search(location=placename, radius=20000,
                                               types=TYPES)

    for place in query_result.places:
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.

        for photo in place.photos:
            photo.get(maxheight=500, maxwidth=500)
    '''
    context = {
        'location': placename,
        #'places': query_result.places,
        #'types' : TYPES,
    }

    return render(request, 'places/search.html', context)

def content(request, type, location):
    key = ' AIzaSyC02yzQWsAxkdaWn8p9ALV7nTthZvjannw'

    google_places = GooglePlaces(key)

    query_result = google_places.nearby_search(location=location, radius=20000,
                                               types=type)

    for place in query_result.places:
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.

        for photo in place.photos:
            photo.get(maxheight=500, maxwidth=500)

    context = {
        'location': location,
        'places': query_result.places,
        'type' : type,
    }

    return render(request, 'places/content.html', context)