from flask import Flask, jsonify, request
import random

app = Flask(__name__)

'''store random sets of weather data, this is to simulate weather forecast'''
weather_dummy = [{
    'temperature': 25,
    'humidity': 50,
    'wind_speed': 10,
    'weather': 'sunny'},
    {
    'temperature': 15,
    'humidity': 70,
    'wind_speed': 5,
    'weather': 'rainy'},
    {
    'temperature': 20,
    'humidity': 60,
    'wind_speed': 15,
    'weather': 'cloudy'},
    {
    'temperature': 30,
    'humidity': 40,
    'wind_speed': 20,
    'weather': 'sunny'},
]

@app.route('/predict_weather/<location>', methods=['POST'])
def predict_weather(location):
    return jsonify(random.choice(weather_dummy)), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)