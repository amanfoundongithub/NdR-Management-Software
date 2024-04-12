# NDR Management System

## Code Organization

- **Booking Microservice**: runs on localhost port 5002
- **Recommendation Microservice**: runs on localhost port 5003
- **IoT Microservice**: runs on localhost port 5004

## Steps to Run

1. Run `python3 <microservice>_controller.py` for each microservice.
2. Each microservice is deployed independently.

For example:

```bash
# Start the Booking Microservice
python3 booking_controller.py

# Start the Recommendation Microservice
python3 recommendation_controller.py

# Start the IoT Microservice
python3 iot_controller.py