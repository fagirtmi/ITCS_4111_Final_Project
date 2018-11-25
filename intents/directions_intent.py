# /building_image.py
import requests
import json
import imghdr
import geocoder

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

# location_url = 'https://www.google.com/maps/dir/?api=1&destination='
location_url = 'https://www.google.com/maps/embed/v1/directions'
photos_url = "https://maps.googleapis.com/maps/api/place/photo"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

# @app.route("/get_picture", methods=['POST'])
def get_directions(message, os):
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good
	response_data = requests.get('https://www.iplocation.net/go/ipinfo').text
	
	try:
		response_json_data = json.loads(response_data)
		location = response_json_data["loc"].split(",")
		message = message.replace(" ", "+")
		building = message + "+UNCC"
		address = location_url + "?key=" + key + "&origin=" + location[0] + "," + location[1] + "&destination=" + building
	except ValueError:
		print("Exception happened while loading data")
		address = location_url + "?key=" + key + "&origin=your+location" + "&destination=" + building

	print(address)
	return address

	# message = message.replace(" ", "+")

	# building = message + "+UNCC"

	# address = location_url + "?key=" + key + "&origin=your+location" + "&destination=" + building
	
	# building = data['queryResult']['parameters']['Buildings']
	# building = building + " UNCC"

	# search_payload = {"key":key, "query":building}
	# search_req = requests.get(search_url, params=search_payload)
	# search_json = search_req.json()

	# address = search_json["results"][0]['formatted_address']
	# building = json.dumps(building)
	# address = json.dumps(address)

	# address = building + "+" + address 
	# address = address.replace(" ", "+")
	# address = address.replace('"',"")
	
	# address = location_url + address