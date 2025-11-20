import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from recommender import recommend


def test_basic_recommend():
    r = recommend('stressed', 'focus')
    assert r['playlist_name'] is not None
    assert 'explanation' in r
    assert 'pomodoro' in r
