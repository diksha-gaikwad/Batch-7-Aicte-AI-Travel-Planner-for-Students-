🧳 AI Travel Recommendation System
📌 Overview

The AI Travel Recommendation System is a Flask-based web application that uses Artificial Intelligence (AI) and a Machine Learning classification model to recommend the best travel destination based on user preferences.

The system predicts destinations such as Delhi, Mumbai, and Pune, generates personalized travel itineraries, and displays related city images dynamically. It can also integrate modern AI APIs like Hugging Face API and Google Gemini API for enhanced intelligent recommendations.

🚀 Features

🤖 AI-powered travel recommendations

🧠 Machine Learning classification model

📍 Personalized itinerary generation

🌐 Flask web integration

🖼️ Dynamic city image display

🔌 Hugging Face & Gemini API integration support

🛠️ Technologies Used

Python

Flask

Scikit-learn

HTML / CSS

Pickle

Hugging Face API

Google Gemini API

📂 Project Structure


├── app_flask.py          
├── train_model.py     
├── predict.py            
├── best_travel_model.pkl 


├── templates/


│   └── index.html 


├── static/ 


└── ai-travel.csv        

⚙️ How It Works

The dataset is used to train a classification model.

The trained model is saved as best_travel_model.pkl.

Flask loads the model and handles user input.

The model predicts the most suitable travel destination.

The system generates an itinerary and displays related city images.

▶️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-travel-recommendation.git
cd ai-travel-recommendation

2️⃣ Install Dependencies


3️⃣ Run the Application
python app_flask.py


Open your browser and visit:

http://127.0.0.1:5000
