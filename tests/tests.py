from eskomfunctions import eskomfunctions:

def test_dictionary_of_metrics:

    """"
    Test function to ensure it operates correctly.
    """

    assert dictionary_of_metrics([12,125,3,89,36]) == {'mean': 53.0, 'median': 36, 'var': 2737.5, 'std': 52.32, 'min': 3, 'max': 125}, 'incorrect'
    assert dictionary_of_metrics([100,326,856,369,231,213]) == {'mean': 349.17,'median': 278.5,'var': 70479.77,'std': 265.48,'min': 100,'max': 856}, 'incorrect'
    assert dictionary_of_metrics([1,2,4,5,6,9,8]) == {'mean': 5.0, 'median': 5, 'var': 8.67, 'std': 2.94, 'min': 1, 'max': 9}, 'incorrect'

    _________________________________________________________________________________________________________________________________________________________

def test_five_num_summary:



        "#Test function to ensure it operates correctly.


    assert five_num_summary([12,125,3,89,36]) == {'min': 3, 'q1': 12.0, 'median': 36.0, 'q3': 89.0, 'max': 125}, 'incorrect'
    assert five_num_summary([100,326,856,369,231,213]) == {'min': 100, 'q1': 217.5, 'median': 278.5, 'q3': 358.25, 'max': 856}, 'incorrect'
    assert five_num_summary([1,2,4,5,6,9,8]) == {'min': 1, 'q1': 3.0, 'median': 5.0, 'q3': 7.0, 'max': 9}, 'incorrect'
