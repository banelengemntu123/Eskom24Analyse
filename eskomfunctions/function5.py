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

    # initialising varianle to store new list
    a = []

    # adding date portion of datetime string to list 'a'
    for i in df['Date']:
        a.append(i[:10])

    # creating dictionary with values counting how many times the specfic date appears in list a
    dict_a = {i:a.count(i) for i in a}

    # creating a DataFrame using data from dictionary
    df_a = pd.DataFrame(data=dict_a.values(), index=dict_a, columns = ['Tweets'])

    # naming index column
    df_a.index.names = ['Date']

    # sorting DataFrame by datetime in descending order
    df_a.index = pd.to_datetime(df_a.index)

    # returning sorted DataFrame in ascending order
    return df_a.iloc[::-1]
