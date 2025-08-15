import googlemaps

gmaps = googlemaps.Client(key="YOUR_GOOGLE_MAPS_API_KEY")

def get_safe_route(origin, destination):
    directions = gmaps.directions(origin, destination, mode="walking")
    return directions
