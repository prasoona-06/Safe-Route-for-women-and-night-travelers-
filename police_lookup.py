def find_nearby_police(lat, lon):
    import googlemaps
    gmaps = googlemaps.Client(key="YOUR_GOOGLE_MAPS_API_KEY")
    places = gmaps.places_nearby(location=(lat, lon), radius=3000, type='police')
    return places['results']
