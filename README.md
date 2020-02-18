# EskomDataAnalyser

EskomDataAnalyser is a Python package with 7 built in functions to calculate the metric data of Eskom's numerical data and to display important data from Eskom related Tweets.

Function 1 returns metrics (minimum, maximum, mean, median, variance and standard deviation) of an input list of numerical data.

Function 2 returns the five number summary (minimum, maximum and the 1st, 2nd and 3rd quartiles) of an input list of numerical data.

Function 3 returns a list of strings edited into a 'yyyy-mm-dd' format from an input list containing strings in the formate 'yyyy-mm-dd hh:mm:ss'

Function 4 adds 2 columns to an input dataframe, named 'municipality' and 'hashtags', containing the municipality and hashtags referenced in the tweet found in the 'Tweets' column.

Function 5 creates a new dataframe using data from an input dataframe. The new dataframe returns the number of tweets sent on a specific day.

Function 6 adds a new column to an input dataframe, named 'Split Tweets', which consists of the string in the column 'Tweets' separated into a list of separated words.

Function 7 adds a new column to an input dataframe, named 'Without Stop Words', which consists of the string in the column 'Tweets' separated into a list of separated words, excluding any words found in the dictionary defined.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install EskomDataAnalyser.

```bash
pip install git+https://github.com/banelengemntu123/Eskom24Analyse.git

pip install --upgrade git+https://github.com/banelengemntu123/Eskom24Analyse.git
```

## Usage

```python
from eskomfunctions import function1, function2, function3, function4, function5, function6, function7

function1.dictionary_of_metrics([12,36,25,14,36,18,36])
  # returns {'mean': 25.29,
  #          'median': 25,
  #          'variance': 116.9,
  #          'standard deviation': 10.81,
  #          'min': 12,
  #          'max': 36}

function2.five_num_summary([25,36,48,39,23,21,45])
  # returns {'min': 21, 'q1': 24.0, 'median': 36.0, 'q3': 42.0, 'max': 48}

function3.date_parser(dates[:3])
# returns ['2019-11-29', '2019-11-29', '2019-11-29']

function4.extract_municipality_hashtags(twitter_df.copy()).loc[8, "Municipality"]
# returns ['Johannesburg']

function5.number_of_tweets_per_day(twitter_df.copy()).loc['2019-11-20', 'Tweets']
# returns 18

function6.word_splitter(twitter_df.copy()).loc[0, 'Split Tweets']
# returns ['@bongadlulane', 'please', 'send', 'an', 'email', 'to', 'mediadesk@eskom.co.za']
```
## Authors and Acknowledgement

Kgaogelo Mamadi
  mrmamadi@outlook.com

Michael Sathekge
  michael@hopmedia.co.za

Victoria Chepape
  chepape87@gmail.com


Banele Ngemntu
  banelengemntu@gmail123.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
