from flask import Flask, request, jsonify
import random

app = Flask(__name__)

class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms

class Room:
    def __init__(self, type, amenities):
        self.type = type
        self.amenities = amenities

hotels = [
    Hotel("Luxury Paradise", "Beachfront", [
        Room("2BHK", ["Sea view", "Jacuzzi", "Private balcony"]),
        Room("3BHK", ["Sea view", "Jacuzzi", "Private balcony", "Kitchen"]),
        Room("4BHK", ["Sea view", "Jacuzzi", "Private balcony", "Kitchen", "Private pool"])
    ]),
    Hotel("Mountain Retreat", "Hill station", [
        Room("2BHK", ["Mountain view", "Fireplace", "Balcony"]),
        Room("3BHK", ["Mountain view", "Fireplace", "Balcony", "Kitchen"]),
        Room("4BHK", ["Mountain view", "Fireplace", "Balcony", "Kitchen", "Private garden"])
    ]),
    # Add more hotels with their respective rooms and amenities
]

def find_room(bedrooms, amenities):
    suitable_rooms = []
    for hotel in hotels:
        for room in hotel.rooms:
            if room.type == f"{bedrooms}BHK" and all(amenity in room.amenities for amenity in amenities):
                suitable_rooms.append({"hotel": hotel.name, "location": hotel.location, "room_type": room.type, "amenities": room.amenities})
    return suitable_rooms

def suggest_holiday_plans():
    holiday_plans = [
        "Guided city tour",
        "Adventure sports package",
        "Spa and wellness retreat",
        "Cultural heritage exploration"
    ]
    return random.choice(holiday_plans)

@app.route('/api/room-booking', methods=['POST'])
def room_booking():
    data = request.get_json()
    bedrooms = data.get('bedrooms')
    amenities = data.get('amenities')

    suitable_rooms = find_room(bedrooms, amenities)

    if suitable_rooms:
        suggested_plan = suggest_holiday_plans()
        return jsonify({"rooms": suitable_rooms, "holiday_plan": suggested_plan})
    else:
        return jsonify({"message": "Sorry, no rooms matching your criteria were found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
c:\Users\barat\Downloads\Chatbot_Tutorial\Chatbot_Tutorial\index.html c:\Users\barat\Downloads\Chatbot_Tutorial\Chatbot_Tutorial\script.js c:\Users\barat\Downloads\Chatbot_Tutorial\Chatbot_Tutorial\style.css