# 🚗 Smart EV Energy Analytics Dashboard

A Machine Learning-powered web application that predicts Electric Vehicle (EV) energy consumption using real-time user inputs. The project combines **Machine Learning**, **Flask**, **HTML/CSS**, and **Chart.js** to provide an interactive dashboard for estimating EV energy usage and visualizing prediction results.

---

# 📌 Project Overview

As Electric Vehicles become increasingly popular, efficient energy estimation plays a vital role in improving route planning and battery management.

This project predicts the expected **energy consumption (kWh)** of an Electric Vehicle based on driving and environmental conditions entered by the user.

The prediction is generated using a trained **Linear Regression Machine Learning model** and displayed through a modern web dashboard.

---

# ✨ Key Features

* 🚗 Predict EV Energy Consumption using Machine Learning
* ⚡ Interactive Flask Web Application
* 📊 Real-time Energy Visualization using Chart.js
* 📋 Displays complete input summary
* 🔋 Battery Status Indicator (Excellent / Moderate / Low)
* ⚠ Energy Level Classification (Low / Medium / High)
* 📈 Prediction History stored automatically in CSV
* ✅ Input validation for realistic EV operating ranges
* 🎨 Responsive and clean dashboard interface

---

# 🚀 Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Linear Regression

### Backend

* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Data Processing

* Pandas
* NumPy

### Model Serialization

* Joblib

### Visualization

* Chart.js

---

# 📂 Project Structure

```
Smart-EV-Energy-Analytics/
│
├── app.py
├── requirements.txt
├── history.csv
├── .gitignore
│
├── dataset/
│
├── models/
│   └── linear_regression_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ⚙ Machine Learning Workflow

1. Load EV dataset.
2. Perform data preprocessing.
3. Train a Linear Regression model.
4. Save the trained model using Joblib.
5. Load the model in Flask.
6. Accept user inputs.
7. Predict energy consumption.
8. Display prediction and analytics dashboard.
9. Store prediction history in CSV.

---

# 📊 Dashboard Features

The dashboard provides:

* Predicted Energy Consumption
* Energy Consumption Doughnut Chart
* Battery Status
* Energy Level Indicator
* Input Summary
* Prediction History Table

---

# 🔍 Input Parameters

| Parameter          | Unit |
| ------------------ | ---- |
| Speed              | km/h |
| Battery State      | %    |
| Temperature        | °C   |
| Humidity           | %    |
| Distance Travelled | km   |

---

# 📈 Output

The application predicts:

* Energy Consumption (kWh)
* Battery Status
* Energy Level
* Prediction History

---

# 💡 What Makes This Project Different?

Unlike many basic EV prediction projects that simply display a machine learning output, this project focuses on providing an **interactive analytics dashboard**.

### Unique Features

* Integrates a trained Machine Learning model with a Flask web application.
* Provides a user-friendly dashboard instead of command-line predictions.
* Automatically stores every prediction for future analysis.
* Displays prediction history within the application.
* Uses Chart.js for interactive visualization.
* Includes battery health classification and energy level categorization.
* Performs client-side validation for realistic EV operating values.
* Designed as a complete end-to-end Machine Learning deployment project rather than only model training.

---

# ▶ Installation

Clone the repository:

```bash
git clone https://github.com/Navyashree-21/Smart-EV-Energy-Analytics.git
```

Move into the project directory:

```bash
cd Smart-EV-Energy-Analytics
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Add screenshots of:

* Dashboard
* Prediction Result
* Prediction History
* Energy Visualization

---

# 🔮 Future Enhancements

* Support multiple Machine Learning models
* Battery State of Charge prediction
* Battery Health prediction
* Route-based energy estimation
* Weather API integration
* Google Maps integration
* User login and prediction history database
* Cloud deployment
* Deep Learning based prediction model

---

# 🎯 Learning Outcomes

Through this project I learned:

* Machine Learning model development
* Model serialization using Joblib
* Flask web development
* HTML/CSS frontend integration
* JavaScript data visualization using Chart.js
* Data preprocessing using Pandas
* End-to-end Machine Learning deployment
* Git and GitHub project management

---

