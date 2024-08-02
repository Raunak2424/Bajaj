from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    response = {
        "is_success": True,
        "user_id": "",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": [],
        "alphabets": [],
        "highest_alphabet": []
    }
    if 'data' in data:
        numbers = [item for item in data['data'] if item.isdigit()]
        alphabets = [item for item in data['data'] if item.isalpha()]
        response["numbers"] = numbers
        response["alphabets"] = alphabets
        if alphabets:
            response["highest_alphabet"] = [max(alphabets, key=lambda x: x.upper())]
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {"operation_code": 1}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
