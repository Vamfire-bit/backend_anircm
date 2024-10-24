from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import get_similarity
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define the recommendation endpoint
@app.route('/recommend', methods=['GET'])
def recommend():
    mal_id = request.args.get('mal_id', type=int)
    if mal_id is None:
        return jsonify({"error": "mal_id parameter is required"}), 400
    result = get_similarity(mal_id)
    return jsonify(result)

# The following block is not needed for Gunicorn deployment
if __name__ == '__main__':
    app.run(debug=False)
