from flask import Flask
import random
import string
# request: To access incoming data (like the long URL).
# redirect: To send the user to another URL.
# jsonify: To create a clean JSON response.

from flask import request, redirect, jsonify


app = Flask(__name__) # creates instance of flask

"""bringing the shortener_logic here"""

url_database = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# --- API ENDPOINT 1: Shorten a URL ---
# We specify methods=['POST'] to say this endpoint only accepts POST requests.
@app.route('/shorten', methods=['POST'])
def shorten_api():

    data = request.get_json() # get data that was posted to us. We expect it to be in json format
    long_url = data.get('url') # get the url from json data -> data['url'], data is a dictionary

    if not long_url :
        return jsonify({"error": "URL is required"}), 400 # Return an error message and a "400 Bad Request" status code.
    
    # generate short code using the shortener logic

    while True:
        short_code = generate_short_code()
        if short_code not in url_database:
            break
    url_database[short_code] = long_url

    short_url = request.host_url + short_code

    return jsonify({"short_url": short_url})


# --- API ENDPOINT 2: Redirect to Long URL --
# The <short_code> part is a variable. Flask will capture whatever is in the URL at that position and pass it as an argument to our function.-

@app.route('/<short_code>')
def redirect_to_url(short_code) :
    long_url = url_database.get(short_code)


    if long_url:
        # If we found it, tell the browser to redirect to it.
        # The '302' is the HTTP status code for a temporary redirect.
        return redirect(long_url, code=302)
    else:
        # If the code is not found, return an error.
        return jsonify({"error": "Short URL not found"}), 404


# --- A simple homepage to explain the service ---   

@app.route('/')
def home():
    return "Welcome to the URL Shortener! Use /shorten to create a URL."

if __name__ == '__main__':
    app.run(debug=True)


"""
Since you can't test a POST request easily in a browser's address bar. We will use cURL.
example to test the shortening end point:
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://en.wikipedia.org/wiki/System_design"}' http://127.0.0.1:5000/shorten


it returns something like this:
{
  "short_url": "http://127.0.0.1:5000/v7ABIY"
}
"""