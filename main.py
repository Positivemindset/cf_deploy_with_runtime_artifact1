import json
import requests
from flask import jsonify

def fetch_data_option3_cf(request):
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code
