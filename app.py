import flask
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

images={}

@app.route('/', methods=['GET'])
def home():
	response = requests.get('http://www.picsum.photos/200')
	out = "<img src='"+str(response.url)+"'/>"
	return out

@app.route('/<int:id>', methods=['GET'])
def req(id):
	if(id in images.keys()):
		out = "<img src='"+str(images[id])+"'/>"
	else:
		response = requests.get('http://www.picsum.photos/200')
		out = "<img src='"+str(response.url)+"'/>"
		images[id] = response.url
	return out

@app.route('/images', methods=['GET'])
def display_all():
	return json.dumps(images)

app.run()