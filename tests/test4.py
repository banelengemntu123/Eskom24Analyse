extract_municipality_hashtags(twitter_df.copy()).loc[4, 'hashtags'] == ['#eskomfreestate', '#mediastatement']
extract_municipality_hashtags(twitter_df.copy()).loc[5, 'municipality'] == ['Johannesburg']
extract_municipality_hashtags(twitter_df.copy()).loc[18, 'municipality'] == ['Johannesburg']
