from eskomfunctions import function4

def extract_municipality_hashtags(df):


    assert function4.extract_municipality_hashtags(twitter_df.copy()).loc[4, 'hashtags'] == ['#eskomfreestate', '#mediastatement'], 'incorrect'
    assert function4.extract_municipality_hashtags(twitter_df.copy()).loc[5, 'municipality'] == 'Johannesburg' , 'incorrect'
    assert function4.extract_municipality_hashtags(twitter_df.copy()).loc[18, 'municipality'] == ['Johannesburg', 'Tshwane'] , 'incorrect'
