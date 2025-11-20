# recommender.py
import json
from db import get_db

RULES = {
    ("stressed", "focus"): {
        "type": "calm",
        "pomodoro": (25,5),
        "breathing": {"pattern":"4-6-8", "duration_seconds":60},
        "explanation": "Stressed + focus: calming binaural/ambient reduces anxiety and enables sustained attention; short 25/5 pomodoro helps manage stress."
    },
    ("calm", "focus"): {
        "type": "focus",
        "pomodoro": (50,10),
        "breathing": None,
        "explanation": "Calm + focus: longer intervals (50/10) to leverage current calm state for deeper flow."
    },
    ("tired", "memorize"): {
        "type": "memory",
        "pomodoro": (20,5),
        "breathing": {"pattern":"box", "duration_seconds":30},
        "explanation": "Tired + memorize: shorter chunks to avoid fatigue, rhythmic tracks improve memory encoding."
    },
    ("bored", "creative"): {
        "type": "creative",
        "pomodoro": (45,10),
        "breathing": None,
        "explanation": "Bored + creative: upbeat instrumentals and longer work blocks encourage creative flow."
    },
    ("default", "default"): {
        "type": "focus",
        "pomodoro": (25,5),
        "breathing": None,
        "explanation": "Balanced recommendation: 25/5 pomodoro with focus ambient tracks."
    }
}

def lookup_rule(mood, intent):
    key = (mood, intent)
    if key in RULES:
        return RULES[key]
    if (mood, "default") in RULES:
        return RULES[(mood, "default")]
    if ("default", intent) in RULES:
        return RULES[("default", intent)]
    return RULES[("default", "default")]

def fetch_playlist_by_type(ptype, db_path='moodstudy.db'):
    db = get_db(db_path)
    cur = db.cursor()
    cur.execute("SELECT id, name, type, description, tracks FROM playlists WHERE type = ? LIMIT 5", (ptype,))
    row = cur.fetchone()
    if not row:
        cur.execute("SELECT id, name, type, description, tracks FROM playlists LIMIT 1")
        row = cur.fetchone()
    if not row:
        return None
    p = {k: row[k] for k in row.keys()}
    p['tracks'] = json.loads(p['tracks'])
    return p

def recommend(mood, intent, db_path='moodstudy.db'):
    mood = (mood or "default").lower()
    intent = (intent or "default").lower()
    rule = lookup_rule(mood, intent)
    playlist_type = rule['type']
    playlist = fetch_playlist_by_type(playlist_type, db_path)
    resp = {
        "mood": mood,
        "study_intent": intent,
        "playlist_id": playlist.get("id") if playlist else None,
        "playlist_name": playlist.get("name") if playlist else None,
        "tracks": playlist.get("tracks") if playlist else [],
        "pomodoro": {"work": rule['pomodoro'][0], "break": rule['pomodoro'][1]},
        "breathing": rule.get('breathing'),
        "explanation": rule.get('explanation')
    }
    return resp
