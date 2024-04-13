from flask import Flask, jsonify, request
import requests
import sys
sys.path.append('../../IOT-Service')
from Service import IOTService

app = Flask(__name__)

@app.route('/parking_lots', methods=['POST'])
def create_parking_lot():
    parking_lot_data = request.get_json()
    name = parking_lot_data['name']
    location = parking_lot_data['location']
    capacity = parking_lot_data['capacity']
    parked = parking_lot_data['parked']
    iot_device_id = parking_lot_data['iot_device_id']
    latitude = parking_lot_data['latitude']
    longitude = parking_lot_data['longitude']
    parking_lot = IOTService.IOTService.createParkingLot(name, location, capacity, parked, iot_device_id, latitude, longitude)
    parking_lot = {
        'name': parking_lot.name,
        'location': parking_lot.location,
        'capacity': parking_lot.capacity,
        'parked': parking_lot.parked,
        'iot_device_id': parking_lot.iot_device_id,
        'latitude': parking_lot.latitude,
        'longitude': parking_lot.longitude
    }
    return jsonify(parking_lot), 201

@app.route('/parking_lots', methods=['GET'])
def get_all_parking_lots():
    parking_lots = IOTService.IOTService.fetchAllParkingLots()
    res = []
    for parking_lot in parking_lots:
        parking_lotj = {
            'id': parking_lot.id,
            'name': parking_lot.name,
            'location': parking_lot.location,
            'capacity': parking_lot.capacity,
            'parked': parking_lot.parked,
            'iot_device_id': parking_lot.iot_device_id,
            'latitude': parking_lot.latitude,
            'longitude': parking_lot.longitude
        }
        res.append(parking_lotj)
    return jsonify({'data': res})

@app.route('/parking_lots/<id>', methods=['GET'])
def get_parking_lot(id):
    parking_lot = IOTService.fetchParkingLot(id)
    if parking_lot:
        return jsonify({'name': parking_lot.name, 'location': parking_lot.location, 'capacity': parking_lot.capacity, 'parked': parking_lot.parked, 'iot_device_id': parking_lot.iot_device_id, 'latitude': parking_lot.latitude, 'longitude': parking_lot.longitude})
    else:
        return jsonify({'error': 'Parking lot not found'}), 404

@app.route('/parking_lots/update', methods=['GET'])
def update_parking_lots():
    IOTService.IOTService.fetchFromSensor()
    return jsonify({'data': 'Parking lots updated'}), 200

@app.route('/parking_lots/available', methods=['GET'])
def get_available_parking_lots():
    parking_lots = IOTService.IOTService.fetchAvailableParkingLots()
    res = []
    for parking_lot in parking_lots:
        parking_lotj = {
            'id': parking_lot.id,
            'name': parking_lot.name,
            'location': parking_lot.location,
            'capacity': parking_lot.capacity,
            'parked': parking_lot.parked,
            'iot_device_id': parking_lot.iot_device_id,
            'latitude': parking_lot.latitude,
            'longitude': parking_lot.longitude
        }
        res.append(parking_lotj)
    return jsonify({'data': res})

###how to update the parked value
###just update the sensor values before each query
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)