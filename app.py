from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load("model/student_model.pkl")


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():

    gender = request.form["gender"]
    race = request.form["race_ethnicity"]
    parent = request.form["parental_level_of_education"]
    lunch = request.form["lunch"]
    course = request.form["test_preparation_course"]
    reading = float(request.form["reading_score"])
    writing = float(request.form["writing_score"])

    input_df = pd.DataFrame({
        "gender": [gender],
        "race_ethnicity": [race],
        "parental_level_of_education": [parent],
        "lunch": [lunch],
        "test_preparation_course": [course],
        "reading_score": [reading],
        "writting_score":[writing]
    })

    prediction = model.predict(input_df)[0]

    return render_template(
        "result.html",
        prediction=round(prediction, 2)
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)