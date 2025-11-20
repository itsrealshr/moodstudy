MoodStudy — Emotion-Driven Study Playlist Recommender
Author: Sharqiue Ansari
Date: 20 November 2025
Project Title: MoodStudy – Emotion-Based Study Music Recommender System

Overview:
MoodStudy is a simple web application that recommends a customized study playlist based on:
    Your current mood
    Your study intention (focus, memorization, creativity, calm study)
It uses a rule-based recommendation system, a Flask backend, and a simple HTML/JS frontend.
It also stores the user's previous recommendations using SQLite.

Features:
  Choose mood + study goal
  Get recommended playlists with:
                  Explanation
                  Pomodoro timer suggestions
                  Breathing exercise
  Tracks are stored in SQLite as JSON
  History of recommendations
  Lightweight and beginner-friendly
  Works offline on local system
  Requires no external API

Technologies & Tools Used:
  Python 3
  Flask
  SQLite
  HTML / CSS / JavaScript
  GitHub Desktop
  Pytest
  VS Code

Steps to Install & Run the Project:
1. Clone the repository
git clone https://github.com/<your-username>/moodstudy.git
2. Move into folder
cd moodstudy
3. Create virtual environment
python -m venv venv
4. Activate virtual environment
Windows:
venv\Scripts\activate
5. Install requirements
pip install -r requirements.txt
6. Run Flask
flask run

Open the browser and visit: http://127.0.0.1:5000/static/index.html

How to Test the Project-Run:pytest -q
You should see: 1 passed in X.XXs

Screenshots:
![alt text](<Screenshot (2).png>)
![alt text](<Screenshot (3).png>)
![alt text](<Screenshot (4).png>)
![alt text](<Screenshot (5).png>)
![alt text](<Screenshot (6).png>)
 [alt text](<Screenshot (7).png>)
![alt text](<Screenshot (8).png>) 
![alt text](<Screenshot (9).png>)
![alt text](<Screenshot (10).png>)
![alt text](<Screenshot (11).png>)

 
Project Structure
moodstudy/
│── app.py
│── db.py
│── recommender.py
│── report.md
│── README.md
│── statement.md
│── requirements.txt
│── static/
│     └── index.html
│── tests/
│     └── test_recommender.py
└── moodstudy.db
