"""
Return a modified dataframe that has a column of removed english stop words

Args:
    df(Dataframe): a pandas dataframe from twitter_df

Returns:
    df(Dataframe): A modified pandas DataFrame with a new column 'Without Stop Words'
"""
import numpy as np
    import pandas as pd

def stop_words_remover(df):
    # create a new empty list for tweets wiithout stop words
    no_stop_words=[]
    for tweets in df['Tweets']: #Iterate through tweets
        x = tweets.lower()
        lower_x = x.split() #lower and split version of the tweets
        for i in lower_x:#Iterate through lower tweets
            if i in stop_words_dict['stopwords']:
                lower_x.remove(i)#Remove all stop words from list

        no_stop_words.append(lower_x)
    df['Without Stop Words']= no_stop_words#Create new dataframe column
    return df