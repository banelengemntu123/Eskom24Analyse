from eskomfunctions import function6

def word_splitter:

    """"
    Test function to ensure required operation.
    """
    
    assert word_splitter(twitter_df.copy()).loc[0, 'Split Tweets'] == ['@bongadlulane', 'please', 'send', 'an', 'email', 'to', 'mediadesk@eskom.co.za'], 'incorrect'
    assert word_splitter(twitter_df.copy()).loc[40, 'Split Tweets'] == ['rt', '@eskomfoundation:', 'as', 'we', 'get', 'closer', 'to', 'announcing', 'the', '#eskombic', 'winner,', 'we', "can't", 'help', 'but', 'reminisce', 'about', 'the', 'forum', 'we', 'hosted', 'early', 'last…'], 'incorrect'
    assert word_splitter(twitter_df.copy()).loc[100, 'Split Tweets'] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'of', 'supply', 'interruption', 'in', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'], 'incorrect'