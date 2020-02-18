import pandas as pd

def number_of_tweets_per_day(df):

    """
    Create a function that counts the number of tweets sent in a day
    and converts data to a pandas dataframe.

    Args:
        df (DataFrame) : a pandas dataframe with a column 'Date' for when
        each tweet was sent.

    Returns:
        df (Dataframe) : a new pandas dataframe with an index columns
        for the 'Date' and a column 'Tweets' for the number of tweets sent that day.
    """

    a = []

    for i in df['Date']:
        a.append(i[:10])
    dict_a = {i:a.count(i) for i in a}
    df_a = pd.DataFrame(data=dict_a.values(), index=dict_a, columns = ['Tweets'])
    df_a.index.names = ['Date']

    df_a.index = pd.to_datetime(df_a.index)

    return df_a.iloc[::-1]
