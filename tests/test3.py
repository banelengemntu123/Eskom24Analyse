from eskomfunctions import function3

def test_date_parser(dates):

    """
    Test function to ensure it operates correctly.
    """

    assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
    assert date_parser(dates[-3:]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
    assert date_parser(dates[3:6]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'