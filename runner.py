import requests
import random
import time

USER_SERVICE_URL = 'http://127.0.0.1:5000'
BOOKING_SERVICE_URL = 'http://127.0.0.1:5002'
RECOMMENDATION_SERVICE_URL = 'http://127.0.0.1:5003'
IOT_SEVICE_URL = 'http://127.0.0.1:5004'

def test_create_parking_lot():
    parking_lot_datas = [{
        'name': 'Parking Lot A',
        'location': 'Location A',
        'capacity': 100,
        'parked': 20,  # Initial parked cars
        'iot_device_id': 123,
        'latitude': 50.456,
        'longitude': 60.789
    },{
        'name': 'Parking Lot B',
        'location': 'Location B',
        'capacity': 100,
        'parked': 100,  # Initial parked cars
        'iot_device_id': 124,
        'latitude': 14.456,
        'longitude': 18.789
    }]
    for parking_lot_data in parking_lot_datas:
        ##wait for response
        response = requests.post(f'{IOT_SEVICE_URL}/parking_lots', json=parking_lot_data)
        time.sleep(1)
        print("Parking Lot Created " ,response.json())

def test_get_all_parking_lots():
    response = requests.get(f'{IOT_SEVICE_URL}/parking_lots')
    print("Parking Lot Lists " , response.json())

def test_get_available_parking_lots():
    response = requests.get(f'{IOT_SEVICE_URL}/parking_lots/available')
    print("Parking Lots Available ",response.json())


EVENT_TYPES = ["science", "comedy", "game", "art", "health"]


def create_temporary_events_and_venues():
    venues = [
        {"name": "Venue A", "capacity": 100, "location": "Location A", "latitude": 12.456, "longitude": 14.012},
        {"name": "Venue B", "capacity": 150, "location": "Location B", "latitude": 22.789, "longitude": 24.654},
        {"name": "Venue C", "capacity": 200, "location": "Location C", "latitude": 42.123, "longitude": 44.321}
    ]
    
    for venue in venues:
        response = requests.post(f'{BOOKING_SERVICE_URL}/venues', json=venue)
        if response.status_code == 201:
            print(f"Venue '{venue['name']}' created successfully")
        else:
            print(f"Failed to create venue '{venue['name']}'")

    for i in range(10):
        event = {
            "name": f"Event {i+1}",
            "type": random.choice(EVENT_TYPES),
            "venue": random.randint(1, len(venues)),
            "start_time": "2024-04-10 08:00:00",
            "end_time": "2024-04-10 12:00:00",
            "booked_seats": random.randint(0, 50)
        }
        response = requests.post(f'{BOOKING_SERVICE_URL}/events', json=event)
        if response.status_code == 201:
            print(f"Event '{event['name']}' created successfully")
        else:
            print(f"Failed to create event '{event['name']}'")

def test_booking_tickets():
    # Book tickets for some events
    response = requests.get(f'{BOOKING_SERVICE_URL}/venues')
    venues = response.json()['data']

    response = requests.get(f'{BOOKING_SERVICE_URL}/events')
    events = response.json()['data']
    for _ in range(3):
        event_id = random.randint(1,len(events))  # There are 10 events created
        num_tickets = random.randint(1, 3)
        booking_data = {"user_id":1,"event_id": event_id, "num_tickets": num_tickets}
        response = requests.post(f'{BOOKING_SERVICE_URL}/bookings', json=booking_data)
        if response.status_code == 201:
            print(f"Successfully booked {num_tickets} tickets for Event ID {event_id}")
        else:
            print(f"Failed to book tickets for Event ID {event_id}")

    # Try to book tickets for events exceeding venue capacity
    for _ in range(5):
        event = random.choice(events)
        event_id = event['id']
        venue_id = event['venue']
        venue_capacity = 0
        for venue in venues:
            if venue['id'] == venue_id:
                venue_capacity = venue['capacity']
                break
        num_tickets = random.randint(venue_capacity + 1, venue_capacity + 20)  # Try to book more tickets than venue capacity
        booking_data = {"user_id":1,"event_id": event_id, "num_tickets": num_tickets}
        response = requests.post(f'{BOOKING_SERVICE_URL}/bookings', json=booking_data)
        if response.status_code == 400:
            print(f"Failed to book {num_tickets} tickets for Event ID {event_id} as venue capacity exceeded")
        else:
            print(f"Unexpected success in booking {num_tickets} tickets for Event ID {event_id}")

def test_recommend_venues(num_tickets):
    response = requests.get(f'{RECOMMENDATION_SERVICE_URL}/recommend_venues/{num_tickets}')
    print("Recommended Venues: ", response.json())

def test_recommend_parkinglots(location):
    response = requests.post(f'{RECOMMENDATION_SERVICE_URL}/recommend_parkinglots', json=location)
    print("Recommended Parking Lots: ", response.json())

def test_recommend_events(topics):
    event_data = {'topics': topics}
    response = requests.post(f'{RECOMMENDATION_SERVICE_URL}/recommend_events', json=event_data)

    print("Recommended Events With given topics : ", response.json())

def main():
    test_create_parking_lot()
    test_get_all_parking_lots()
    test_get_available_parking_lots()

    create_temporary_events_and_venues()

    test_booking_tickets()

    for num_tickets in [20,50,100,1000] :
        test_recommend_venues(num_tickets)  #Get Recommendation for num_tickets 
    test_recommend_parkinglots({'location':{'latitude':12.5,'longitude':13.5}})  
    test_recommend_events(['science', 'art'])  # Example: Get recommendations for events related to science and art
    
if __name__ == "__main__":
    test_recommend_parkinglots({'location':{'latitude':12.5,'longitude':13.5}})  
    # main()