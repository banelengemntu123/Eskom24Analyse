from eskomfunctions import function3

def test_date_parser(dates):

    """
    Test function to ensure it operates correctly.
    """

    date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
    date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
    date_parser(dates[0:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
