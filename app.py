from flask import Flask, send_file, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("ev_data.csv")

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/style.css")
def css():
    return send_file("style.css")

@app.route("/data")
def data():
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)