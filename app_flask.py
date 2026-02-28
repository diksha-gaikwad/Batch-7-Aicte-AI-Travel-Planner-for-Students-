from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, "templates"),
            static_folder=os.path.join(BASE_DIR, "static"))

# ================= LOAD ML MODEL =================
with open(os.path.join(BASE_DIR, "best_travel_model.pkl"), "rb") as file:
    model, X_columns = pickle.load(file)

# ================= HUGGINGFACE SETUP =================
HF_API_KEY = os.getenv("HF_API_KEY")

HF_API_URL = "https://router.huggingface.co/v1/chat/completions"

HF_HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")

# ================= ML PREDICTION =================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        city = request.form["city"]
        place_type = request.form["type"]
        best_time = request.form["best_time"]

        new_data = pd.DataFrame({
            "City": [city],
            "Type": [place_type],
            "Best_Time": [best_time]
        })

        new_data = pd.get_dummies(new_data)
        new_data = new_data.reindex(columns=X_columns, fill_value=0)

        prediction = model.predict(new_data)

        result = "FREE place 🎉" if prediction[0] == 0 else "PAID place 💰"

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# ================= AI TRIP PLANNER =================
@app.route("/plan", methods=["POST"])
def plan_trip():
    try:
        data = request.get_json()

        destination = data.get("destination")
        days = data.get("days")
        min_budget = data.get("min_budget")
        max_budget = data.get("max_budget")

        # Better formatted prompt for map extraction
        prompt = f"""
        Plan a {days}-day student budget trip to {destination}.
        Budget range: {min_budget} to {max_budget} INR.

        Format strictly like:

        Day 1:
        - Place Name 1
        - Place Name 2

        Day 2:
        - Place Name 3
        - Place Name 4

        After listing places, provide short explanation.
        Use real tourist locations only.
        """

        payload = {
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 700,
            "temperature": 0.7
        }

        response = requests.post(
            HF_API_URL,
            headers=HF_HEADERS,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            return jsonify({"error": response.text})

        result = response.json()

        # Safe extraction
        itinerary = result.get("choices", [{}])[0]\
                          .get("message", {})\
                          .get("content", "No itinerary generated.")

        return jsonify({"itinerary": itinerary})

    except Exception as e:
        return jsonify({"error": str(e)})

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)