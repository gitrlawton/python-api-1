# jsonify is used to create a json response
from flask import Flask, request, jsonify

# Creat flask application.
app = Flask(__name__)

# Route is an endpoint, a location on our API where we can go to
# get some kind of data. The route is the path that comes after the "/".

# Creating a route. Use the @ sign followed by the name of your
# application (app).
@app.route("/")
def home():
    # Return data we want the user to have access to when they reach 
    # this route.
    return "Home"

# Route designed to retrieve user data based on the provided user_id.
# This route handles GET requests.  Flask assumes that a route is to handle 
# GET requests if no method argument is provided.
@app.route("/get-user/<user_id>")
# v Accept the same parameter(s) as the path parameter(s) in the path. ^
# Notice: the path here doesn't end in a '/'.  Therefore, visiting the path
# with a '/' after the id will result in Not Found error page.  Path must be
# typed as written above.
def get_user(user_id):
    # Dummy data.
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    # Query parameters are variables that follow a '?' in the path
    # example: get-user/1?extra=hello_world"
    # args stores all of the query parameters in a dictionary.
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    # At the beginning of this function, we greate a dictionary called
    # user_data.  Here, we now convert that dictionary to json and send it
    # to the user.
    return jsonify(user_data), 200

# Route for handling POST requests.  At this endpoint, we are receiving
# data from the user.  
# You can set it up to handle multiple types of requests by adding a comma 
# followed by other method types (ie. methods=["POST", "GET", "DELETE"]).
@app.route("/create-user", methods=["POST"])
def create_user():
    # You can create different actions based on what kind of request was 
    # made.  This is only relevant if your route is designed to handle
    # multiple types of requests (ie. both POST and GET).
    if request.method == "POST":
        print("POST request.")
        
    # Receive some data from the request thats in json format.
    # The user is going to send us some data as it pertains to the user
    # they want to create.
    #
    # This is how we get that data.  This gives us all the json data
    # that was passed inside the body of the request.
    data = request.get_json()
    
    # Return this data back to the user along with a success message,
    # indicating it was received successfully.  Note: In most circumstances
    # you'll want to add it to a database, not return it back.
    return jsonify(data), 201

# Run flask application.
if __name__ == "__main__":
    app.run(debug = True)
