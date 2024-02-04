#!/usr/bin/python3
import requests

# Set the base URL for the Flask application
base_url = 'http://83.136.254.199:32748'

# Make a POST request to the root route '/' with our custom ingredients
data = {'ingredient': 'custom_ingredient', 'measurements': '1000 + 337'}
response = requests.post(base_url + '/', data=data)
print("POST /:", response.text)
