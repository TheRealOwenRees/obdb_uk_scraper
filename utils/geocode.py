from time import sleep
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut


def get_brewery_coordinates(name, address, postcode, country):
    def get_coordinates(query):
        try:
            print(query)
            sleep(8)
            geolocator = Nominatim(user_agent="obdb_brewery_finder")
            location = geolocator.geocode(query)
            return [location.latitude, location.longitude]
        except AttributeError:
            return None
        except GeocoderTimedOut:
            print(f"Geocoder timed out with {query} - trying query again.")
            return get_coordinates(query)

    query_string = f"{address.split(',')[0]}, {postcode}, {country}"  # 34B Carrowdore Road, BT22 2LX, Northern Ireland
    coordinates = get_coordinates(query_string)

    if coordinates is None:
        print(f"Coordinates not found, trying again with brewery name.")
        query_string = f"{name}, {postcode}, {country}"  # Brewery Name, BT22 2LX, Northern Ireland
        coordinates = get_coordinates(query_string)

    return coordinates
