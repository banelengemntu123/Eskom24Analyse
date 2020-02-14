<<<<<<< HEAD
import pandas as pd 

def number_of_tweets_per_day(df):
  
    """
    Calculate  the number of tweets that were posted per day

    Args:
        df (dataframe) : df pandas dataframe
        

    Returns:
        df (Dataframe) : dataframe, grouped by day, with the number of tweets for that day.
    Examples:
        >>> number_of_tweets_per_day(twitter_df.copy())   
    """


     # your code here
    df["Date"] = [i.split(' ',1)[0] for i in df["Date"]]
    a = sorted(list(df["Date"].unique()))
    dictp = {}
    for i in a:
        for x in df[df["Date"] == i]["Date"]:
            if x in dictp.keys():
                dictp[x] += 1
        else:
            dictp[x] = 1 
    new_df = pd.Dataframe.from_dict(data=dictp,orient="index", coloumns= ["Tweets"])
    new_df.index.name = "Date"
    
    return new_df

### END FUNCTION
=======
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
>>>>>>> 3e1cf6744afcd1f574c94bb095fa350f357dd03c
