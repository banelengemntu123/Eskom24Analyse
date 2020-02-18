def number_of_tweets_per_day(df):

    """
     Create a function that counts the number of tweets sent in a day
     and converts data to a pandas dataframe.

     Input is a DataFrame and the output is a dataframe with new column

    Args:
        df (DataFrame) : a pandas dataframe with a column 'Date' for when
        each tweet was sent.


    Returns:
        df (Dataframe) : a new pandas dataframe with an index columns,
        grouped by day, with the number of tweets for that day.

    Examples:
        >>> number_of_tweets_per_day(twitter_df.copy()).loc['2019-11-20', 'Tweets']
        18
    """

    #Iterate through the dataframe and split
    df["Date"] = [i.split(' ',1)[0] for i in df["Date"]]
    a = sorted(list(df["Date"].unique()))

    #Initialising an empty dictionary 'dictp'
    dictp = {}

    #iterate through the sorted list
    for i in a:
    #Iterate through each splited value in the dataframe
        for x in df[df["Date"] == i]["Date"]:
            if x in dictp.keys():
                dictp[x] += 1
            else:
                dictp[x] = 1

    #creating a new dataframe "new_df" with coloumn tweets
    new_df = pd.Dataframe.from_dict(data=dictp,orient="index", columns= ["Tweets"])
    new_df.index.name = "Date"

    #returning a new dataframe with the coloumn 'Tweets' and 'Date'
    return new_df
