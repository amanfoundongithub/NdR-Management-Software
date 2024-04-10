import requests

from math import radians, sin, cos, sqrt, atan2

class RecommendationService:
    BOOKING_SERVICE_URL = 'http://127.0.0.1:5002'
    IOT_SERVICE_URL = 'http://127.0.0.1:5004'
    @staticmethod
    def get_recommendations(num_tickets):
        response = requests.get(f'{RecommendationService.BOOKING_SERVICE_URL}/events')
        if response.status_code == 404:
            return {'error': 'Error Fetching Events'}
        
        event_data = response.json()['data']
        
        response = requests.get(f'{RecommendationService.BOOKING_SERVICE_URL}/venues')
        if response.status_code == 404:
            return {'error': 'Error Fetching Venues'}
        
        venues_data = response.json()['data']
        capacity = {venue['id']: venue['capacity'] for venue in venues_data}
        
        rec_list = []
        for event in event_data:
            if capacity[event['venue']] - event['booked_seats'] >= num_tickets:
                rec_list.append(event)
        
        return rec_list
    
    @staticmethod
    def get_parking_lots(location):

        requests.get(f'{RecommendationService.IOT_SERVICE_URL}/parking_lots/update')

        lat, lon = location['latitude'],location['longitude']

        response = requests.get(f'{RecommendationService.IOT_SERVICE_URL}/parking_lots/available')
        available_parking_lots = response.json()['data']

        # Calculate distance from the provided location to each parking lot
        nearest_parking_lot = None
        min_distance = float('inf')
        for parking_lot in available_parking_lots:
            # Calculate distance using Haversine formula
            distance = RecommendationService.calculate_distance(lat, lon, parking_lot['latitude'], parking_lot['longitude'])
            if distance < min_distance:
                min_distance = distance
                nearest_parking_lot = parking_lot

        return nearest_parking_lot


    @staticmethod
    def calculate_distance( lat1, lon1, lat2, lon2):

        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula to calculate distance between two points on a sphere
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = 6371 * c  # Radius of the Earth in kilometers
        return distance 
    
    
    @staticmethod
    def get_event_recommendations(topics):
        response = requests.get(f'{RecommendationService.BOOKING_SERVICE_URL}/events')
        if response.status_code == 404:
            return {'error': 'Error Fetching Events'}
        events = response.json()['data']
        rec_list = []
        for event in events:
            if event['type'] in topics:
                rec_list.append(event)
        return rec_list