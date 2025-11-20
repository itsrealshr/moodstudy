# app.py
import json
from flask import Flask, request, jsonify
from recommender import recommend
from db import init_db, get_db

DATABASE = 'moodstudy.db'
app = Flask(__name__)
init_db(DATABASE)

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/recommend', methods=['POST'])
def recommend_endpoint():
    data = request.get_json() or {}
    mood = data.get('mood')
    intent = data.get('study_intent')
    user_id = data.get('user_id')
    if not mood or not intent:
        return jsonify({"error": "mood and study_intent are required"}), 400

    rec = recommend(mood.lower().strip(), intent.lower().strip())

    db = get_db(DATABASE)
    cur = db.cursor()
    cur.execute(
        "INSERT INTO history (user_id, mood, study_intent, playlist_id, explanation) VALUES (?, ?, ?, ?, ?)",
        (user_id, mood, intent, rec.get("playlist_id"), rec.get("explanation"))
    )
    db.commit()

    return jsonify(rec)

@app.route('/playlists', methods=['GET'])
def list_playlists():
    db = get_db(DATABASE)
    cur = db.cursor()
    cur.execute("SELECT id, name, type, description, tracks FROM playlists")
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    result = [dict(zip(cols, r)) for r in rows]
    for p in result:
        try:
            p['tracks'] = json.loads(p['tracks'])
        except:
            p['tracks'] = []
    return jsonify(result)

@app.route('/history', methods=['GET'])
def get_history():
    user_id = request.args.get('user_id')
    db = get_db(DATABASE)
    cur = db.cursor()
    if user_id:
        cur.execute("SELECT * FROM history WHERE user_id = ? ORDER BY recommended_at DESC", (user_id,))
    else:
        cur.execute("SELECT * FROM history ORDER BY recommended_at DESC")
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return jsonify([dict(zip(cols, r)) for r in rows])

if __name__ == '__main__':
    app.run(debug=True)
