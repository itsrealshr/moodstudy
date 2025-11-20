# db.py
import sqlite3
import json
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS playlists (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  description TEXT,
  tracks TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS history (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  mood TEXT,
  study_intent TEXT,
  playlist_id INTEGER,
  recommended_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  explanation TEXT
);
"""

SAMPLE_PLAYLISTS = [
    {
        "name": "Focus — Low BPM Ambient",
        "type": "focus",
        "description": "Ambient, low-bpm tracks for deep focus.",
        "tracks": [
            {"title": "Soft Drift", "artist": "AmbientLab", "duration": "6:12"},
            {"title": "Quiet Flow", "artist": "StudySounds", "duration": "8:00"},
            {"title": "Monotone Ocean", "artist": "CalmTone", "duration": "10:00"}
        ]
    },
    {
        "name": "Memory — Rhythmic Loops",
        "type": "memory",
        "description": "Rhythmic, steady tracks that help encoding.",
        "tracks": [
            {"title": "Loop Aid", "artist": "Mnemonic Beats", "duration": "5:30"},
            {"title": "Anchor", "artist": "Recall Studio", "duration": "4:45"}
        ]
    },
    {
        "name": "Creative — Upbeat Instrumental",
        "type": "creative",
        "description": "Energetic instrumentals to spark ideas.",
        "tracks": [
            {"title": "Spark", "artist": "IdeaGroove", "duration": "3:45"},
            {"title": "Ignite", "artist": "MuseHop", "duration": "4:10"}
        ]
    },
    {
        "name": "Calm — Binaural & Rain",
        "type": "calm",
        "description": "Soft binaural beats and gentle rain for stress relief.",
        "tracks": [
            {"title": "Rain Lull", "artist": "NatureBox", "duration": "12:00"},
            {"title": "Slow Waves", "artist": "Binaural Studio", "duration": "10:00"}
        ]
    }
]

def init_db(path='moodstudy.db'):
    created = False
    if not Path(path).exists():
        created = True
    db = sqlite3.connect(path)
    cur = db.cursor()
    cur.executescript(SCHEMA)
    db.commit()
    if created:
        for p in SAMPLE_PLAYLISTS:
            cur.execute("INSERT INTO playlists (name,type,description,tracks) VALUES (?,?,?,?)",
                        (p['name'], p['type'], p['description'], json.dumps(p['tracks'])))
        db.commit()
    db.close()

def get_db(path='moodstudy.db'):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db
