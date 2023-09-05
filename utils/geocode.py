from time import sleep
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut


def get_brewery_coordinates(address, postcode, country):
    sleep(8)
    query = f"{address.split(',')[0]}, {postcode}, {country}"  # eg. '34B Carrowdore Road, BT22 2LX, United Kingdom'
    print(query)

    try:
        geolocator = Nominatim(user_agent="obdb_brewery_finder")
        location = geolocator.geocode(query)
        coordinates = [location.latitude, location.longitude]
    except AttributeError:
        return None
    except GeocoderTimedOut:
        print(f"Geocoder timed out with {query} - trying query again.")
        return get_brewery_coordinates(address, postcode, country)

    return coordinates
