from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("salary_model.pkl")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():

    name = request.args.get("name")
    age = request.args.get("age")
    education = request.args.get("education")
    experience = request.args.get("experience")

    if experience:

        prediction = model.predict([[int(experience)]])
        salary = prediction[0]

        return render_template(
            "predict.html",
            salary=salary,
            name=name,
            age=age,
            education=education,
            experience=experience
        )

    return render_template(
        "predict.html",
        salary=None,
        name=None,
        age=None,
        education=None,
        experience=None
    )


if __name__ == "__main__":
    app.run(debug=True)