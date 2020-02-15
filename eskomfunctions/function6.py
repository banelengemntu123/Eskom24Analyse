def word_splitter(df):

    """
    Splits the sentences in a dataframe's column into a list of the separate words. 
    The created lists will be placed in a column named 'Split Tweets' in the original dataframe.
    All wordsin lower case.

    Args:
        df (DataFrame) : a pandas dataframe which should contain a column, named 'Tweets'.

    Returns:
        df (Dataframe) : a modified pandas dataframe from the original with an extra column "Tweets"
        added.
    """

    tweet_split = []
    for tweet in df['Tweets']:
        tweet_split.append(tweet.lower().split())#added method to convert string to lowercase

    df['Split Tweets'] = tweet_split

    return df
