from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    number1 = data.get('number1')
    number2 = data.get('number2')

    if not operation or not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        return jsonify({"error": "Invalid input"}), 400

    if operation == "add":
        result = number1 + number2
    elif operation == "subtract":
        result = number1 - number2
    elif operation == "multiply":
        result = number1 * number2
    elif operation == "divide":
        if number2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = number1 / number2
    else:
        return jsonify({"error": "Unsupported operation"}), 400

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)