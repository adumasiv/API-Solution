# This file contains the API logic. The server will be using Flask running on port 5000.

from flask import Flask, request, jsonify #jsonify is used to covert Python dictionaries or objects to JSON objects
from data_objects import data_objects # Import the data_objects list from data_objects.py  
from flask_cors import CORS # Import CORS to allow cross-origin requests 
import uuid # Import uuid to generate unique IDs for data objects       

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['GET', 'POST']) #'DELETE']) # Allow both GET, POST & DELETE requests on the same route

def handle_data(): # This function will handle the request of the user

    global data_objects # Declare data_objects (from 'data_objects.py') as a global variable to modify it in the function

    if request.method == 'POST': # If the request is a POST request, then the user is sending data to the server

        data = request.get_json() # Get the data sent by the user
        data["id"] = str(uuid.uuid4())  # Generate a unique ID for the data object
        data_objects.append(data) # Add the data to the list of data objects 


        return jsonify(data_objects)
        
    
    elif request.method == 'GET': # If the request is a GET request, then the user is asking for data from the server
        return jsonify(results=data_objects) # Return the first 10 data objects
    
    #elif request.method == 'DELETE':

           # data = request.get_json()
            #if "id" in data:
                # data_id = data["id"]
                 # Find and remove the data object with the given ID
                 #data_objects = [ obj for obj in data_objects if obj.get ("id") != data_id]
            #return jsonify(results=data_objects)
    else:
        return jsonify(error= "ID not provided in the request"), 400

if __name__ == '__main__':
        app.run(debug=True) # Run the app in debug mode