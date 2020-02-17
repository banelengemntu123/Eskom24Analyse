import numpy as np

def five_num_summary(items):

    """
    Calculate the five number summary for numerical data

    Args:
        items (list) : list (or array) of numerical data

    Returns:
        dictionary : keys for five number summary linked to appropriate values

    Examples:
        >>>> five_num_summary([12,125,3,89,36])
        {'min': 3, 'q1': 12.0, 'median': 36.0, 'q3': 89.0, 'max': 125}
    """

    # initialising summary dictionary
    summary = {'min':0,
              'q1':0,
              'median':0,
              'q3':0,
              'max':0}

    # calculating minimum and maximum values of dataset and adding to summary dictionary
    summary['min'] = min(items)
    summary['max'] = max(items)

    # calculating 1st, 2nd and 3rd quartile of dataset and adding to summary dicitonary
    summary['q1'] = np.quantile(items, .25)
    summary['q3'] = np.quantile(items, .75)
    summary['median'] = np.quantile(items, .5)

    # return summary dictionary with values appended to each key
    return summary
