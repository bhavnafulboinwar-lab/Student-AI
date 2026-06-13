from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# model = joblib.load("model/student_model.pkl")

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/result", methods=["POST"])
def result():

    attendance = float(request.form["attendance"])
    study_hours = float(request.form["study_hours"])
    previous_score = float(request.form["previous_score"])

    if attendance >= 80 and study_hours >= 4 and previous_score >= 75:
        prediction = "Excellent"

    elif attendance >= 60 and study_hours >= 2 and previous_score >= 50:
        prediction = "Good"

    elif attendance >= 40 and study_hours >= 1 and previous_score >= 35:
        prediction = "Average"

    else:
        prediction = "Poor"

    return render_template(
        "result.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)