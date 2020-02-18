from eskomfunctions import function3

def test_date_parser(dates):

    """
    expected outcomes:
    """

    date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
    date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
    date_parser(dates[3:6]) == ['2019-11-29', '2019-11-29', '2019-11-29']