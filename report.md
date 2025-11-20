# MoodStudy — Emotion-Driven Study Playlist Recommender

**Author:** <Your Name>  
**Course:** Build Your Own Project  
**Date:** <DD Month YYYY>  
**Contact:** <your.email@example.com>

---

## Abstract
MoodStudy recommends study playlists based on a learner’s current mood and study intent. It returns an explainable playlist, suggested Pomodoro timings, and short breathing exercises. The system is intentionally rule-based for interpretability and easy demonstration.

## Problem Statement
Students often don't know which audio environment helps them best for focus, memory, or creativity. Generic playlists do not adapt to emotional or task contexts, reducing study efficiency.

## Objectives
1. Build a web app that takes mood and study intent as input.  
2. Provide a clear, explainable recommendation (playlist + pomodoro + breathing).  
3. Persist recommendation history.  
4. Prepare a report and demonstration to show the working system.

## System Design
- Frontend: Static HTML + Bootstrap.  
- Backend: Flask REST API exposing `/recommend`, `/playlists`, `/history`.  
- Database: SQLite (seeded with sample playlists).  
- Recommender: deterministic rule-based mapper (documented rules).

### Data model (simplified)
- `users(id, name, email)`  
- `playlists(id, name, type, description, tracks JSON)`  
- `history(id, user_id, mood, study_intent, playlist_id, explanation, recommended_at)`

## Recommender Logic
The system maps `(mood, study_intent)` pairs to a playlist type and provides supporting items:
- Pomodoro config (work / break minutes)  
- Short breathing exercise (pattern & duration)  
- Explanation text that justifies the recommendation using simple cognitive principles (e.g., calming ambient for stressed users).

A small sample rule:
- (stressed, focus) → calm playlist + 25/5 pomodoro + 4-6-8 breathing (reduces anxiety, improves attention)

## Implementation
Files:
- `app.py` — Flask API entry
- `db.py` — DB schema + seed data
- `recommender.py` — rule-based mapping
- `static/index.html` — frontend UI
- `tests/test_recommender.py` — pytest test
- `ml_model.py` — optional toy ML pipeline

Key endpoints:
- `POST /recommend` — `{mood, study_intent, user_id?}` → JSON recommendation
- `GET /playlists` — returns seeded playlists
- `GET /history` — returns recommendation history

## How to run (local)
1. Create virtual environment: `python3 -m venv venv && source venv/bin/activate`  
2. Install: `pip install -r requirements.txt`  
3. Run: `export FLASK_APP=app.py && flask run`  
4. Open: `http://127.0.0.1:5000/static/index.html`

## Tests
Run `pytest -q`. Example expected output:

## Demonstration Evidence
Include these:
1. Screenshot — frontend with recommendation shown.  
2. Screenshot — `pytest` result.  
3. Screenshot — `sqlite3` showing history rows with timestamps.  
4. Short screencast (60–90s) showing the live interaction.

## Limitations & Future Work
- Rule-based recommender is simple; better personalization requires real user data and a proper ML model.  
- No authentication/Tokens in demo (for simplicity).  
- Could add track preview playback and export to playlist formats (M3U).

## Personal Reflection
(Write this in first-person and be specific about your work)
I implemented MoodStudy by first creating the SQLite schema and seeding curated playlists. I then designed the rule matrix linking moods and study intents to playlist types. A bug I encountered: JSON parsing of playlist tracks failed until I ensured tracks were always stored as JSON strings and parsed on retrieval. Implementing the frontend taught me Fetch API and simple DOM manipulation. I wrote small unit tests to verify the recommender behaviour. Building this project taught me how to encode human-centered design rules in deterministic software and why explainability matters for recommendations.

## Files Submitted
- Source code (app.py, db.py, recommender.py, ml_model.py)  
- `static/index.html` and `README.md`  
- `report.pdf` (this document converted)  
- `tests/` and `model.joblib` (optional)

## References
(Optional) Add links to 2–3 short sources about music & cognition (cite if you used any).

---
