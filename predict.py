import pickle
import pandas as pd

# Load model and columns
with open("best_travel_model.pkl", "rb") as file:
    model, X_columns = pickle.load(file)

print("Model loaded successfully ✅")

# Take user input
city = input("Enter City: ")
place_type = input("Enter Type: ")
best_time = input("Enter Best Time: ")

# Create DataFrame
new_data = pd.DataFrame({
    'City': [city],
    'Type': [place_type],
    'Best_Time': [best_time]
})

# Convert to dummy
new_data = pd.get_dummies(new_data)

# Match training columns
new_data = new_data.reindex(columns=X_columns, fill_value=0)

# Predict
prediction = model.predict(new_data)

if prediction[0] == 0:
    print("This is a FREE place 🎉")
else:
    print("This is a PAID place 💰")
