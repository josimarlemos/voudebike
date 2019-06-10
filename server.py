import os
import json
from flask import Flask, make_response, jsonify


app = Flask(__name__)

@app.route('/api/stations')
def stations():
    filename = os.path.join(app.static_folder, 'stations.json')
    
    with open(filename, 'r') as stations:
        data = json.load(stations)

    return make_response(jsonify(data))