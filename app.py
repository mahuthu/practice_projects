

from flask import Flask, request, jsonify
app = Flask(__name__)
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]
#This helper function uses a generator expression to select all the country IDs
# and then calls max() on them to get the largest value.
# It increments this value by 1 to get the next ID to use.
def find_next_id():
    return max(country["id"] for country in countries) + 1
@app.route("/countries", methods=["GET"])
#, get_countries() takes countries, which is a Python list, and converts
# it to JSON with jsonify(). This JSON is returned in the response.

def get_countries():
    return jsonify(countries)
# a Flask route decorator, to connect GET requests to a function in the application.
# When you access /countries, Flask calls the decorated function to handle the HTTP request and return
# a response.
@app.route("/countries", methods=["POST"])
#this function handles POST requests to /countries and allows you to add a new country
#to the list. It uses the Flask request object to get information about the current HTTP request:
def add_countries():
    #Using request.is_json to check that the request is JSON
    if request.is_json:
        #Creating a new country instance with request.get_json()
        country = request.get_json()
        #Finding the next id and setting it on the country
        country["id"] = find_next_id()
        #ppending the new country to countries
        countries.append(country)
        return country, 201

    return {"error: request must be json"}, 415
