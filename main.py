from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Iris Flower Finder 🌸</h1>
    <form action="/predict" method="post">
        Sepal Length: <input type="text" name="sl"><br><br>
        Sepal Width: <input type="text" name="sw"><br><br>
        Petal Length: <input type="text" name="pl"><br><br>
        Petal Width: <input type="text" name="pw"><br><br>
        <input type="submit" value="Predict">
    </form>
    """


@app.route("/predict", methods=["POST"])
def predict():
    sl = float(request.form["sl"])
    sw = float(request.form["sw"])
    pl = float(request.form["pl"])
    pw = float(request.form["pw"])

    # simple logic (replace with your model later)
    if pl < 2:
        result = "Setosa 🌼"
    elif pl < 5:
        result = "Versicolor 🌸"
    else:
        result = "Virginica 🌺"

    return f"<h2>Prediction: {result}</h2><a href='/'>Go Back</a>"


app.run(host="0.0.0.0", port=3000)
