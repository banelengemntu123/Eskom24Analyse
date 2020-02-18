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

    Example:
        >>>>word_splitter(twitter_df).loc[0, 'Split Tweets']
        ['@bongadlulane', 'please', 'send', 'an', 'email', 'to', 'mediadesk@eskom.co.za']
    """
    
    #create an empty list
    tweet_split = []

    #iterate through all the Tweets in the Dataframe['Tweets'] column
    for tweet in df['Tweets']:
    #append lowecase word split list to tweet_split
        tweet_split.append(tweet.lower().split())#added method to convert string to lowercase

    #create a new 'Split Tweets' column to original dataframe
    df['Split Tweets'] = tweet_split

    #return updated dataframe
    return df
