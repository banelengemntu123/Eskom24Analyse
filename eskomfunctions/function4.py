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

def extract_municipality_hashtags(df):

    """
    Return a modified pandas dataframe that contains of two new columns about the municipality and the hashtag of the tweets

    Args:
        df(DataFrame): df pandas dataframe

    Returns:
        df(DataFrame): DataFrame with new municipality and hashtag columns
    """


    #create a empty list
    mun_list = []
    for tweet in df['Tweets']:#Iterate through a column and split
        x = tweet.split()
        flag =False #Create a boolean variable for the while loop to hold true
        while flag == 0:
            for key in x: #Iterate through each splited value in the dataframe column
                if key[0] == '@':
                    if key in mun_dict.keys():
                        mun_list.append([mun_dict[key]]) #if the key which contains an '@ exists in a dictionary it will append to mun_list'
                        flag = True
                    elif key[0:-1] in mun_dict.keys(): #should a key contain a : at the end, it should append as well
                        mun_list.append([mun_dict[key[0:-1]]])
                        flag=True
                        break
            if flag==False:
                mun_list.append(np.nan)
                flag=True

    hashtags=[] #new list for hashtags
    for tweet in df['Tweets']:
        hashtags.append([tags for tags in tweet.lower().split() if tags[0][0] == '#']) #loop through tags in the column after splitting and lowing each tweet
        hashtags = [np.nan if x == [] else x for x in hashtags]  #every '#' will append to the new list as a lower case list
    df['municipality'] = mun_list
    df['hashtags'] = hashtags
    return df
