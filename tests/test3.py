from eskomfunctions import function3

def test_date_parser(dates):

    """
    expected outcomes:
    """

    date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
    date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']
<<<<<<< HEAD
=======
    date_parser(dates[0:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
>>>>>>> e62054dbb7b30662f171036195b3980479bbf554
