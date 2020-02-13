def dictionary_of_metrics(list):

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
