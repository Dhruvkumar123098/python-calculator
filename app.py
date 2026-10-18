
from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            operation = request.form["operation"]

            result = calculate(a, b, operation)

        except ValueError as error:
            result = str(error)

    return render_template("index.html", result=result)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
