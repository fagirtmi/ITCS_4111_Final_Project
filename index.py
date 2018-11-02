# /index.py
import os
import dialogflow
import requests
import json
import pusher
import imghdr

from flask import Flask, request, jsonify, render_template, send_from_directory
app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
photos_url = "https://maps.googleapis.com/maps/api/place/photo"

@app.route('/')
def index():
	return render_template('index.html')

def detect_intent_texts(project_id, session_id, text, language_code):
	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(project_id, session_id)
	
	if text:
		text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
		query_input = dialogflow.types.QueryInput(text=text_input)
		response = session_client.detect_intent(session=session, query_input=query_input)
													
		return response.query_result.fulfillment_text

@app.route('/send_message', methods=['POST'])
def send_message():
	message = request.form['message']
	project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
	fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
	response_text = { "message":  fulfillment_text }
	# print(fulfillment_text)	# Print response text
	return jsonify(response_text)

# function 
@app.route("/get_building_image", methods=['POST'])
def results():
	data = request.get_json(silent=True)
	building = data['queryResult']['parameters']['Buildings']
	building = building + " UNCC"
	key = os.getenv('GOOGLE_MAPS_API_KEY') # key is good

	search_payload = {"key":key, "query":building}
	search_req = requests.get(search_url, params=search_payload)
	search_json = search_req.json()
	print(search_json) # Gives me the entire payload for a building at UNCC

	photo_id = search_json["results"]
	photo_id = search_json["results"][0]["photos"][0]["photo_reference"]

	photo_payload = {"key" : key, "maxwidth" : 500, "maxwidth" : 500, "photoreference" : photo_id}
	photo_request = requests.get(photos_url, params=photo_payload)
	print(photo_payload)
	print(photo_request)

	photo_type = imghdr.what("", photo_request.content)
	photo_name = "static/" + building + "." + photo_type

	with open(photo_name, "wb") as photo:
		photo.write(photo_request.content)

	print(photo_name)
	return send_from_directory('.', photo_name)
	# return '<img src='+ photo_name + '>'

# @app.route('/get_building_picture', methods=['POST'])
# def get_movie_detail():
# 	data = request.get_json(silent=True)
# 	movie = data['queryResult']['parameters']['movie']
# 	api_key = os.getenv('OMDB_API_KEY')

# 	movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(movie, api_key)).content
# 	movie_detail = json.loads(movie_detail)
# 	response =  """
# 		Title : {0}
# 		Released: {1}
# 		Actors: {2}
# 		Plot: {3}
# 	""".format(movie_detail['Title'], movie_detail['Released'], movie_detail['Actors'], movie_detail['Plot'])

# 	reply = {
# 		"fulfillmentText": response,
# 	}

# 	return jsonify(reply)

# run Flask app
if __name__ == "__main__":
	app.run()
