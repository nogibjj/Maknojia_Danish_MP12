from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Basic route
@app.route("/")
def home():
    return render_template("index.html")


# Dynamic route
@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)


# JSON response route
@app.route("/api/info", methods=["GET"])
def api_info():
    data = {
        "app_name": "Cool Flask App",
        "version": "1.0",
        "description": "This is a simple Flask app with dynamic routes and JSON responses.",
    }
    return jsonify(data)


# Query parameters example
@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form.get("num1", 0))
    num2 = float(request.form.get("num2", 0))
    operation = request.form.get("operation", "add")

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
    else:
        result = "Invalid operation"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
