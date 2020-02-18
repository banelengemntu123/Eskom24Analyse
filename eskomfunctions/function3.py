def date_parser(dates):

    """
    A function that takes a list of datetime strings and returns only the date in 'yyyy-mm-dd' formates

    Args:
        dates(list): list of datetime strings

    returns:
        list: lists of only the date

    Example:
      >>>>date_parser(dates[:3])
      ['2019-11-29', '2019-11-29', '2019-11-29']
    """

    #Initializing an empty list to append a new list in
    mylist= []

    #slicing only the dates from the old list and appending to a new list
    for date in dates:
        mylist.append(date[:10])

    #returning a new list with only a string of dates.
    return mylist

#__________________________________________________________________________________________________________________________________________
