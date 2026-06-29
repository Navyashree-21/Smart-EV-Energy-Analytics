from flask import Flask, render_template, request
import joblib
import os
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/linear_regression_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    # When the page is opened for the first time
    if request.method == "GET":
        return render_template("index.html")

    # Read user inputs
    speed = float(request.form["speed"])
    battery = float(request.form["battery"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    distance = float(request.form["distance"])

    # Create DataFrame (same feature names used during training)
    input_data = pd.DataFrame({
        "Speed_kmh": [speed],
        "Battery_State_%": [battery],
        "Temperature_C": [temperature],
        "Humidity_%": [humidity],
        "Distance_Travelled_km": [distance]
    })

    # Prediction
    prediction = model.predict(input_data)
    prediction = round(prediction[0], 2)
    percentage = round((prediction / 20) * 100, 1)

    new_data = pd.DataFrame({
    "Speed":[speed],
    "Battery":[battery],
    "Temperature":[temperature],
    "Humidity":[humidity],
    "Distance":[distance],
    "Prediction":[prediction]
})

    # Save prediction history
    # Save prediction history
    new_data.to_csv(
        "history.csv",
        mode="a",
        header=False,
        index=False
    )

    # Battery Status
    if battery >= 80:
        battery_status = "<span style='color:green;'>🟢 Excellent</span>"
    elif battery >= 50:
        battery_status = "<span style='color:orange;'>🟡 Moderate</span>"
    else:
        battery_status = "<span style='color:red;'>🔴 Low</span>"

    # Energy Consumption Level
    if prediction < 6:
        energy_level = "🟢 Low"
    elif prediction < 10:
        energy_level = "🟡 Medium"
    else:
        energy_level = "🔴 High"

    # Print in terminal (for debugging)
    print("Speed:", speed)
    print("Battery:", battery)
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Distance:", distance)
    print("Prediction:", prediction)
    print("Battery Status:", battery_status)
    print("Energy Level:", energy_level)

    history = pd.read_csv("history.csv")

    history = history.tail(10)

    # Send data to HTML
    return render_template(
        "index.html",
        prediction=prediction,
        percentage=percentage,
        speed=speed,
        battery=battery,
        temperature=temperature,
        humidity=humidity,
        distance=distance,
        battery_status=battery_status,
        energy_level=energy_level,
        history=history.to_dict(orient="records")
    )


if __name__ == "__main__":
    app.run(debug=True)