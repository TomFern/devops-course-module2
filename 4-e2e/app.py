from flask import Flask, jsonify, request

app = Flask(__name__)

# the / route shows a "Welcome to the flask app!"
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# the /add route takes a JSON payload in a POST request and returns the sum of the two numbers
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data.get("a", 0) + data.get("b", 0)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
