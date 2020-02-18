import numpy as np
import pandas as pd

mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

def dictionary_of_metrics(list):
    metrics = {"mean":0, "median":0, 'variance':0, 'standard deviation':0, 'min':0, 'max':0}

    # counting number of elements in list
    n = len(list)

    # sorting elements in list in ascending order
    srt = sorted(list)

    # calculating maximum and minimum values of dataset and adding to metric dictionary
    metrics['max'] = max(list)
    metrics['min'] = min(list)

    # calculating mean of dataset and adding to metric dictionary, rounded to 2 decimal places
    mean = sum(list)/n
    metrics['mean'] = round(mean,2)

    # calculating median of dataset, accounting for whether dataset has an even or odd number of elements
    # adding median to metric dictionary
    if n%2 == 0:
        metrics['median'] = round(((srt[int(n/2)] + srt[int((n//2)-1)])/2), 2)
    else:
        metrics['median'] = round((srt[(n//2)]), 2)

    # calculating variance of dataset
    var = 0
    for x in list:
        var += (x-mean) ** 2

    # adding variance, rounded to 2 decimal places, to metric dictionary
    metrics['variance'] = round ((var/(n-1)), 2)

    # calculating standard deviation of dataset and adding to metric dictionary, rounded to 2 decimal places
    metrics['standard deviation'] = round(((var/(n-1))**(1/2)), 2)

    # return metric dictionary with values appended to each key
    return metrics

def five_num_summary(items):

    summary = {'min':0,
                  'q1':0,
                  'median':0,
                  'q3':0,
                  'max':0}

    # calculating minimum and maximum values of dataset and adding to summary dictionary
    summary['min'] = min(items)
    summary['max'] = max(items)

    # calculating 1st, 2nd and 3rd quartile of dataset and adding to summary dicitonary
    summary['q1'] = np.quantile(items, .25)
    summary['q3'] = np.quantile(items, .75)
    summary['median'] = np.quantile(items, .5)

    # return summary dictionary with values appended to each key
    return summary

def date_parser(dates):

    #Initializing an empty list to append a new list in
    mylist= []

    #slicing only the dates from the old list and appending to a new list
    for date in dates:
        mylist.append(date[:10])

    #returning a new list with only a string of dates.
    return mylist

def extract_municipality_hashtags(df):

    #create a empty list
    mun_list = []

    #Iterate through a column and split
    for tweet in df['Tweets']:
        x = tweet.split()

    #Create a boolean variable for the while loop to hold true
        flag =False
        while flag == 0:

    #Iterate through each splited value in the dataframe column
            for key in x:
                if key[0] == '@':
                    if key in mun_dict.keys():

    #if the key which contains an '@ exists in a dictionary it will append to mun_list'
                        mun_list.append([mun_dict[key]])
                        flag = True

    #should a key contain a : at the end, it should append as well
                    elif key[0:-1] in mun_dict.keys():
                        mun_list.append([mun_dict[key[0:-1]]])
                        flag=True
                        break
            if flag==False:
                mun_list.append(np.nan)
                flag=True

    #new list for hashtags
    hashtags=[]
    for tweet in df['Tweets']:

    #loop through tags in the column after splitting and lowing each tweet
        hashtags.append([tags for tags in tweet.lower().split() if tags[0][0] == '#'])

    #every '#' will append to the new list as a lower case list
        hashtags = [np.nan if x == [] else x for x in hashtags]
    df['municipality'] = mun_list
    df['hashtags'] = hashtags
    return df

def number_of_tweets_per_day(df):

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

def word_splitter(df):

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

def stop_words_remover(df):

    # initialising empty list 'a'
    a = []

    # splitting each row of strings in column "Tweets" into individual. lowercase elements
    for i in df['Tweets']:
        new = [x.lower() for x in i.split()]
    # removing stopwords from list of individual lowercase words
        for j in new.copy():
            if j in stop_words_dict['stopwords']:
                new.remove(j)
    # adding list of lowercase elements, excluding stopwords, to list 'a'
        a.append(new)

    # adding column 'Without Stop Words' to existing DataFrame with data from array 'a'
    df['Without Stop Words'] = a

    # returning new DataFrame
    return df
