from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Static user details (replace with actual user details, we could retrieve the data from a database)
USER_ID = "john_doe_17091999"  # This will be used as a unique identifier for the user
EMAIL = "john@xyz.com"  # User's email address
ROLL_NUMBER = "ABCD123"  # User's college roll number

# Route: /bfhl | Method: GET
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    """
    GET method endpoint
    - This route returns a hardcoded JSON response with an operation_code = 1.
    - It does not take any input parameters.
    - The response is returned with an HTTP status code of 200, indicating success.
    """
    return jsonify({"operation_code": 1}), 200

# Route: /bfhl | Method: POST
@app.route('/bfhl', methods=['POST'])
def process_data():
    """
    POST method endpoint
    - This route accepts a JSON request with a 'data' array containing a mix of numbers and alphabets.
    - It processes the array to separate numbers and alphabets and identifies the highest lowercase alphabet.
    - The response includes static user information, the extracted numbers, alphabets, and the highest lowercase alphabet.
    - Error handling is implemented to return a failure status if something goes wrong.
    """
    try:
        # Extract the 'data' array from the JSON request body
        data = request.json.get('data', [])
        
        # Validate that the 'data' is indeed a list
        if not isinstance(data, list):
            raise ValueError("Input data should be a list")

        # Separate numbers from the input data
        numbers = [item for item in data if item.isdigit()]
        
        # Separate alphabets from the input data
        alphabets = [item for item in data if item.isalpha()]

        # Filter out only lowercase alphabets
        lowercase_alphabets = [char for char in alphabets if char.islower()]

        # Find the highest lowercase alphabet in the input, if any
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else ""

        # Prepare the response dictionary with all required information
        response = {
            "is_success": True,  # Operation status: True indicates success
            "user_id": USER_ID,  # Static user ID
            "email": EMAIL,  # Static email
            "roll_number": ROLL_NUMBER,  # Static roll number
            "numbers": numbers,  # List of numbers extracted from the input
            "alphabets": alphabets,  # List of alphabets extracted from the input
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []  # Highest lowercase alphabet
        }

        # Return the prepared response as JSON with an HTTP status code of 200 (OK)
        return jsonify(response), 200

    except Exception as e:
        # If an error occurs, return a failure response with the error message
        return jsonify({"is_success": False, "error": str(e)}), 400

# Entry point of the Flask application
if __name__ == '__main__':
    # Run the Flask app on port 8080 in debug mode
    # Debug mode helps during development by providing detailed error messages and auto-reloading the server on code changes
    app.run(debug=True, port=8080)
