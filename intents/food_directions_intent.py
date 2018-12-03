import requests
import json
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

location_url = 'https://www.google.com/maps/embed/v1/directions'
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def get_food_directions(message, os):
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good

	message = message.replace(" ", "+")

	building = message + "+UNCC"

	address = location_url + "?key=" + key + "&origin=your+location" + "&destination=" + building

	return address