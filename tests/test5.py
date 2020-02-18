from eskomfunctions import function5 :

def test_number_of_tweets_per_day:

    """"
    Test function to ensure it operates correctly.

    """

    assert function5.number_of_tweets_per_day(twitter_df.copy()).loc['2019-11-20', 'Tweets'] == 18, 'incorrect'
    assert function5.number_of_tweets_per_day(twitter_df.copy()).loc['2019-11-22', 'Tweets'] == 25, 'incorrect'
    assert function5.number_of_tweets_per_day(twitter_df.copy()).loc['2019-11-28', 'Tweets'] == 32, 'incorrect'
