import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv(r"C:\Users\user\Desktop\ibm-skill-build\ai-travel.csv")

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")

# Convert Entry_Fee
df['Entry_Fee'] = pd.to_numeric(df['Entry_Fee'], errors='coerce')
df['Entry_Fee'] = df['Entry_Fee'].fillna(0)

# Create target
df['Fee_Category'] = df['Entry_Fee'].apply(lambda x: 0 if x == 0 else 1)

# Features
X = df[['City', 'Type', 'Best_Time']]
y = df['Fee_Category']

# Convert categorical
X = pd.get_dummies(X)

# Save columns for prediction
X_columns = X.columns

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model + columns
with open("best_travel_model.pkl", "wb") as file:
    pickle.dump((model, X_columns), file)

print("Model trained and saved successfully ✅")
