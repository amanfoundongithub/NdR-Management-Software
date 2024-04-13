import sys
sys.path.append('../../Booking-Service')

from flask import Flask, jsonify, request
from Service import BookingService
import requests

app = Flask(__name__)

@app.route('/venues', methods=['POST'])
def create_venue():
    venue_data = request.get_json()
    name = venue_data['name']
    capacity = venue_data['capacity']
    location = venue_data['location']
    latitude = venue_data['latitude']
    longitude = venue_data['longitude']
    venue = BookingService.BookingService.create_venue(name, capacity, location, latitude, longitude)
    if venue:
        return jsonify({'id':venue.id}), 201
    else:
        return jsonify({'error': 'Venue already exists'}), 400

@app.route('/venues/<id>', methods=['GET'])
def get_venue(id):
    venue = BookingService.BookingService.get_venue(id)
    if venue:
        return jsonify({'name' : venue.name, 'capacity' : venue.capacity, 'location' : venue.location})
    else:
        return jsonify({'error': 'Venue not found'}), 404

@app.route('/venues', methods = ['GET'])
def get_all_venues() : 
    venues_list = BookingService.BookingService.get_all_venues()
    res = []
    for venues in venues_list:
        venuesj =  {
            'id' : venues.id,
            'name' : venues.name , 
            'capacity' : venues.capacity,
            'location' : venues.location,
            'latitude' : venues.latitude,
            'longitude' : venues.longitude
        }
        res.append(venuesj)
    return jsonify({'data':res})

@app.route('/events', methods=['POST'])
def create_event():
    event_data = request.get_json()
    name = event_data['name']
    event_type = event_data['type']
    venue_name = event_data['venue']
    start_time = event_data['start_time']
    end_time = event_data['end_time']
    event = BookingService.BookingService.create_event(name, event_type, venue_name, start_time, end_time)
    if event :
        return jsonify(event.id), 201
    else : 
        return jsonify({'error': 'Venue not found'}), 404

@app.route('/events', methods=['GET'])
def get_all_events():
    events_list = BookingService.BookingService.get_all_events()
    print(events_list)
    res = []
    for event in events_list : 
        eventj = {
            'id' : event.id,
            'name': event.name,
            'type': event.event_type,
            'venue': event.venue_id,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'booked_seats': event.booked_seats
        }
        res.append(eventj)
    return jsonify({'data':res})

@app.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = BookingService.BookingService.get_event(id)
    if event :
        return jsonify(event)
    else:
        return jsonify({'error': 'Event not found'}), 404

@app.route('/bookings', methods=['POST'])
def book_ticket():
    booking_data = request.get_json()
    user_id = booking_data['user_id']
    event_id = booking_data['event_id']
    num_tickets = booking_data['num_tickets']
    ftickets = BookingService.BookingService.get_free_tickets(event_id)
    if ftickets and ftickets >= num_tickets:
        booking = BookingService.BookingService.create_booking(user_id, event_id, num_tickets)
        return jsonify({
            'user_id': booking.user_id,
            'event_id': booking.event_id,
            'num_tickets': booking.num_tickets
        }), 201
    else : 
        return jsonify({'error': 'Not enough tickets available'}), 400

@app.route('/bookings', methods=['GET'])
def get_all_bookings():
    return BookingService.BookingService.get_all_bookings()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)