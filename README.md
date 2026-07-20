AI Salary Prediction System with PDF Report Generation

Overview

The AI Salary Prediction System is an end-to-end Machine Learning web application that predicts an employee's salary based on years of experience. The application is built using Python, Flask, Scikit-learn, HTML, CSS, and ReportLab.

Users can enter their years of experience, receive an instant salary prediction, and download a professionally formatted PDF report containing the prediction.

---

Live Demo

Live Website:

https://salary-prediction-flask-8a64.onrender.com

---

Features

- Machine Learning salary prediction
- Flask web application
- User-friendly HTML interface
- Real-time prediction
- Downloadable PDF report
- Input validation
- Responsive interface
- Cloud deployment on Render

---

Technologies Used

Programming Language

- Python

Machine Learning

- Scikit-learn
- Joblib

Backend

- Flask

Frontend

- HTML5
- CSS3

PDF Generation

- ReportLab

Deployment

- Render

---

Project Structure

Salary-Prediction/
│
├── app.py
├── train_model.py
├── salary_model.pkl
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── result.html
│   └── report.html
├── static/
│   ├── style.css
│   └── images/
└── README.md

---

Workflow

1. User opens the website.
2. User enters years of experience.
3. Flask receives the input using "request.form".
4. Flask loads the trained Machine Learning model.
5. The model predicts the salary.
6. Flask sends the predicted salary back to the webpage.
7. The user can download a PDF report.
8. ReportLab generates the PDF and sends it to the user.

---

Machine Learning Model

- Algorithm: Linear Regression
- Framework: Scikit-learn
- Model File: "salary_model.pkl"

The model is trained using historical salary data and saved with Joblib for deployment.

---

PDF Report

The generated report includes:

- Project title
- User input (Years of Experience)
- Predicted Salary
- Date and time (if enabled)
- Professional formatting

---

Installation

Clone the repository:

git clone <repository-url>

Move into the project directory:

cd Salary-Prediction

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000

---

Future Improvements

- Support multiple Machine Learning algorithms
- Add Age and Education as additional input features
- Improve prediction accuracy with larger datasets
- User authentication
- Prediction history
- Database integration
- Interactive analytics dashboard
- REST API support

---

Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Model Deployment
- Flask Development
- HTML & CSS
- Joblib Model Serialization
- PDF Report Generation
- Cloud Deployment
- End-to-End ML Pipeline

---

Learning Outcomes

This project demonstrates the complete lifecycle of a Machine Learning application:

- Data → Model Training → Model Saving → Flask Backend → User Input → Prediction → PDF Report → Cloud Deployment

---

Author

Gourav Jain

B.Tech CSE (AI & ML)

NIST University

---

License

This project is created for educational and portfolio purposes.
