import argparse # Used to parse command line arguments
import requests
from pprint import pprint #more readable json in the console

API_URL = 'http://127.0.0.1:5000/api/data'

# HANDLE 'GET' REQUESTS ---------------------------------------------------------------------------

def get_data():
    response = requests.get(API_URL)
    data_objects = response.json()["results"]  # Get the data objects from the response

    # Sort the data_objects by date in descending order
    sorted_objects = sorted(data_objects, key=lambda x: x["date"], reverse=True)
    pprint(sorted_objects)

    return response.json()

# HANDLE 'POST' REQUESTS ---------------------------------------------------------------------------

def post_data(new_data):
    response = requests.post(API_URL, json=new_data)  # Send a POST request with the new data
    return response.json()

# HANDLE DELETE REQUESTS ---------------------------------------------------------------------------

#def delete_data():
    #response = requests.delete('API_URL/{data_id}')
    r#eturn response.json()

# HANDLE COMMAND LINE ARGUMENTS ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Interact with the API')
    parser.add_argument('--get', action='store_true', help='Invoke GET request')
    parser.add_argument('--post', action='store_true', help='Invoke POST request')
    #parser.add_argument('--delete', type=str, help='Delete data from the API by ID')

    args = parser.parse_args()

    if args.get:
        get_data()
    elif args.post:
        # Get user input for each attribute
        name = input("Enter name: ")
        type = input("Enter type: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")
        # create a dictionary (DTO) with the new data
        new_data = {
            "name": name,
            "type": type,
            "description": description,
            "date": date
        }

        post_data(new_data)

    #creates a delete function that will delete data from the API by ID
    #elif args.delete:

        #delete_data(args.delete)
        
        

    else:
        print("Please provide a valid command. Use --get to invoke GET, --post to invoke POST or --delete to invoke DELETE.")

if __name__ == '__main__':
    main()

    