import numpy as np

def dictionary_of_metrics(list):



    # Function 1
    """
    Calculate the five number metrics for a list of numerical data

    Args:
        list (list) : list (or array) of numerical data

    Returns:
        dictionary : keys of metric names linked to appropriate values

    Examples:
        >>> dictionary_of_metrics([12,125,3,89,36])
        {'mean': 53.0, 'median': 36, 'var': 2737.5, 'std': 52.32, 'min': 3, 'max': 125}
    """

    metrics = {"mean":0, "median":0, 'variance':0, 'standard deviation':0, 'min':0, 'max':0}

    n = len(list)
    srt = sorted(list)

    metrics['max'] = max(list)
    metrics['min'] = min(list)

    mean = sum(list)/n
    metrics['mean'] = round(mean, 2)

    if n%2 == 0:
        metrics['median'] = round(((srt[int(n/2)]+srt[int((n//2)-1)])/2), 2)
    else:
        metrics['median'] = round((srt[(n//2)]), 2)

    var = 0
    for x in list:
        var += (x - mean) ** 2

    # Assuming received data is a sample of the population
    metrics['variance'] = round ((var / (n-1)), 2)
    metrics['standard deviation'] = round(((var/(n-1)) **(1/2)), 2)


    return metrics

# ________________________________________________________________________________________________________________________________________________________

def five_num_summary(items):



    #Function 2

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

    summary = {'min':0,
              'q1':0,
              'median':0,
              'q3':0,
              'max':0}

    summary['min'] = min(items)
    summary['max'] = max(items)
    summary['q1'] = np.quantile(items, .25)
    summary['q3'] = np.quantile(items, .75)
    #summary['median']= np.median(data)
    summary['median'] = np.quantile(items, .5)

    return summary

    print (3+6)
