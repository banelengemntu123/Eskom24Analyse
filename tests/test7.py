from eskomfunctions import function7

def test_stop_words_remover:

    """"
    Test function to ensure it operates correctly.
    """

    assert stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za'], incorrect
    assert stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'], incorrect
    assert stop_words_remover(twitter_df.copy()).loc[4, 'Without Stop Words'] == ['#eskomfreestate', '#mediastatement', ':', 'eskom', 'suspends', 'planned', 'electricity', 'supply', 'interruptions', 'mangaung', 'metropolitan…', 'https://t.co/mtbo6gjcte'], incorrect
