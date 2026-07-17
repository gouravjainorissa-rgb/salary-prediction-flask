from flask import Flask, render_template, request, send_file
import joblib

from pdf_generator import generate_pdf

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


@app.route("/download-pdf")
def download_pdf():

    name = request.args.get("name")
    age = request.args.get("age")
    education = request.args.get("education")
    experience = request.args.get("experience")
    salary = float(request.args.get("salary"))

    pdf = generate_pdf(
        name,
        age,
        education,
        experience,
        salary
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Salary_Prediction_Report.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)