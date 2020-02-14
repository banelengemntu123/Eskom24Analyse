def word_splitter(df):

    """
    Add appropriate docstring
    """

    tweet_split = []
    for tweet in df['Tweets']:
        tweet_split.append(tweet.lower().split())#added method to convert string to lowercase

    df['Split Tweets'] = tweet_split

    return df
