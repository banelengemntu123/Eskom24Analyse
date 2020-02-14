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

### END FUNCTIONg