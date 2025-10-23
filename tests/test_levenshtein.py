from metrics.levenshtein import levenshtein_distance

def test_levenshtein_distance():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("abc", "adc") == 1
    assert levenshtein_distance("abc", "ab") == 1