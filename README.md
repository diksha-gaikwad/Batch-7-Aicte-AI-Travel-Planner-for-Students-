🧳 AI Travel Recommendation System


📌 Overview

The AI Travel Recommendation System is a Flask-based web application that uses Artificial Intelligence (AI) and a Machine Learning classification model to recommend the best travel destination based on user preferences.

The system predicts destinations such as Delhi, Mumbai, Pune, and others, generates personalized travel itineraries, and dynamically displays related city images. It can also integrate modern AI APIs, such as the Hugging Face API and Google Gemini API, to provide enhanced intelligent recommendations.

🚀 Features

🤖 AI-powered travel recommendations

🧠 Machine Learning classification model

📍 Personalized itinerary generation

🌐 Flask web integration

🖼️ Dynamic city image display

🔌 Hugging Face & Gemini API integration support

🛠️ Technologies Used

| Tool / Technology | Description                                                           |
| ----------------- | --------------------------------------------------------------------- |
| Python            | Main programming language used to build the application logic         |
| Flask             | Backend web framework used to handle routing and requests             |
| Scikit-learn      | Machine learning library used to train and build the prediction model |
| HTML              | Used to create the structure of the web pages                         |
| CSS               | Used to design and style the user interface                           |
| Pickle            | Used to save and load the trained machine learning model              |
| Hugging Face API  | Provides AI model integration for enhanced intelligent features       |
| Google Gemini API | Used for advanced AI recommendations and itinerary generation         |




📂 Project Structure


├── app_flask.py          
├── train_model.py     
├── predict.py            
├── best_travel_model.pkl 


├── templates/


├── index.html 


├── static/ 


├── ai-travel.csv        

⚙️ How It Works

The dataset is used to train a classification model.

The trained model is saved as best_travel_model.pkl.

Flask loads the model and handles user input.

The model predicts the most suitable travel destination.

The system generates an itinerary and displays related city images.



▶️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/diksha-gaikwad/Batch-7-Aicte-AI-Travel-Planner-for-Students.git
cd Batch-7-Aicte-AI-Travel-Planner-for-Students

2️⃣ Install Dependencies

Flask==3.1.3

pandas==3.0.1

python-dotenv==1.2.1

Requests==2.32.5


scikit_learn==1.8.0


3️⃣ Add Your AI API Token

Open config.py or create a .env file:

AI_API_KEY = "your_api_token_here"

or

AI_API_KEY=your_api_token_here

4️⃣ Run the Application

python app_flask.py

5️⃣ Open in Browser
Visit: http://127.0.0.1:5000
