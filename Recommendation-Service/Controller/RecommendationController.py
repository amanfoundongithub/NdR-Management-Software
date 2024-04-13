
import sys
sys.path.append('../../Recommendation-Service')

from flask import Flask, jsonify, request
from Service import RecommendationService

app = Flask(__name__)

@app.route('/recommend_venues/<num_tickets>', methods=['GET'])
def recommend_venue(num_tickets):
    num_tickets = int(num_tickets)
    rec_list = RecommendationService.RecommendationService.get_recommendations(num_tickets)
    return jsonify({'data': rec_list}), 200

@app.route('/recommend_parkinglots', methods=['POST'])
def recommend_parkinglots():
    location_data = request.get_json()
    location = location_data['location']
    parking_lots = RecommendationService.RecommendationService.get_parking_lots(location)
    return jsonify({'data': parking_lots}), 200

@app.route('/recommend_events', methods=['POST'])
def recommend_events():
    recevent_data = request.get_json()
    topics = recevent_data['topics']
    rec_list = RecommendationService.RecommendationService.get_event_recommendations(topics)
    return jsonify({'data': rec_list}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
