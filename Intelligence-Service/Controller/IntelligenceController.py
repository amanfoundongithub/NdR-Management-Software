from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

##PUT IT IN .ENV
BOOKING_SERVICE_URL = 'http://127.0.0.1:5002'

@app.route('/recommend_venues/<num_tickets>', methods=['GET'])
def recommend_venue(num_tickets) :
    num_tickets = int(num_tickets)
    response  = requests.get(f'{BOOKING_SERVICE_URL}/events')
    if response.status_code == 404 : 
        return jsonify({'error': 'Error Fetching Events'}), 404
    event_data = (response.json())['data']
    response = requests.get(f'{BOOKING_SERVICE_URL}/venues')
    if response.status_code == 404 : 
        return jsonify({'error': 'Error Fetching Venues'}), 404
    venues_data = (response.json())['data']
    capacity = {}
    for venue in venues_data : 
        capacity[venue['id']] = venue['capacity']
    rec_list = []
    for event in event_data : 
        print(event['venue'])
        print(capacity[event['venue']])
        print(event['booked_seats'])
        print()
        if capacity[event['venue']]-event['booked_seats']  >= num_tickets : 
            rec_list.append(event)
    return jsonify({'data':rec_list}), 200

@app.route('/dummy',methods=['GET'])
def dummy():
    return jsonify({'data':'dummy'}),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)