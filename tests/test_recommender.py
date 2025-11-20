from recommender import recommend
def test_basic_recommend():
    r = recommend('stressed', 'focus')
    assert r['playlist_name'] is not None
    assert 'explanation' in r
    assert 'pomodoro' in r
