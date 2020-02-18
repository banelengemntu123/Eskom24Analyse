# EskomDataAnalyser

EskomDataAnalyser is a Python package with 7 built in functions to calculate the metric data of Eskom's numerical data and to display important data from Eskom related Tweets.

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
#returns ['2019-11-29', '2019-11-29', '2019-11-29']

```

## License
[MIT](https://choosealicense.com/licenses/mit/)
