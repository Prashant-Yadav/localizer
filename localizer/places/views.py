
from googleplaces import GooglePlaces, types, lang

from django.shortcuts import render

from .models import Place, Photo


def index(request):
    return render(request, 'places/index.html')


def navbar_info(request):
    return render(request, 'places/navbar.html')


def search(request):
    placename = request.POST['place']

    context = {
        'location': placename,
    }

    return render(request, 'places/search.html', context)


def content(request, type, location):
    key = 'AIzaSyDVa_QhQkZb8eGLwMmDrhvpjB745f5dakM'

    '''try: 
        places=Place.objects.filter(city=location)
        context = {
            'location': location,
            'places': places,
            'type': type,
        }
    except:        '''
    google_places = GooglePlaces(key)

    query_result = google_places.nearby_search(location=location, radius=20000,
                                               types=type)

    for place in query_result.places:
        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.

        place_model = Place(place_name=place.name,
                            geo_location=place.geo_location,
                            place_id=place.place_id,
                            address="",
                            details=place.details,
                            city=location,
                            local_phone_number=str(place.local_phone_number),
                            international_phone_number=str(place.international_phone_number),
                            website=place.website,
                            icon=place.icon
                            )
        place_model.save()

        current_place = Place.objects.get(id=place_model.id)

        for photo in place.photos:
            photo.get(maxheight=500, maxwidth=500)

            photo_model = Photo(photo_name=photo.filename,
                                place=current_place,
                                url=photo.url,
                                mimetype=photo.mimetype
                                )
            photo_model.save()

    context = {
        'location': location,
        'places': query_result.places,
        'type': type,
    }

    return render(request, 'places/content.html', context)

def item(request, place_id):
    
    place = Place.objects.get(place_id=place_id)

    context = {
        'place': place,
    }

    return render(request, 'places/item.html', context)