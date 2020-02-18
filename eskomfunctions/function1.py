def dictionary_of_metrics(list):

    """
    Calculate the metrics (minumum, maximum, mean, median, variance and standard deviation) for a list of numerical data

    Args:
        list (list) : list (or array) of numerical data

    Returns:
        dictionary : keys of metric names linked to appropriate values

    Examples:
        >>> dictionary_of_metrics([12,125,3,89,36])
        {'mean': 53.0, 'median': 36, 'var': 2737.5, 'std': 52.32, 'min': 3, 'max': 125}
    """

    # initialising metric dicitionary
    metrics = {"mean":0, "median":0, 'variance':0, 'standard deviation':0, 'min':0, 'max':0}

    # counting number of elements in list
    n = len(list)

    # sorting elements in list in ascending order
    srt = sorted(list)

    # calculating maximum and minimum values of dataset and adding to metric dictionary
    metrics['max'] = max(list)
    metrics['min'] = min(list)

    # calculating mean of dataset and adding to metric dictionary, rounded to 2 decimal places
    mean = sum(list)/n
    metrics['mean'] = round(mean,2)

    # calculating median of dataset, accounting for whether dataset has an even or odd number of elements
    # adding median to metric dictionary
    if n%2 == 0:
        metrics['median'] = round(((srt[int(n/2)] + srt[int((n//2)-1)])/2), 2)
    else:
        metrics['median'] = round((srt[(n//2)]), 2)

    # calculating variance of dataset
    var = 0
    for x in list:
        var += (x-mean) ** 2

    # adding variance, rounded to 2 decimal places, to metric dictionary
    metrics['variance'] = round ((var/(n-1)), 2)

    # calculating standard deviation of dataset and adding to metric dictionary, rounded to 2 decimal places
    metrics['standard deviation'] = round(((var/(n-1))**(1/2)), 2)

    # return metric dictionary with values appended to each key
    return metrics

# ________________________________________________________________________________________________________________________________________________________
