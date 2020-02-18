def date_parser(dates):

    """
    A function that takes a list of datetime strings and returns only a string of dates in the 'yyyy-mm-dd' format.
    
    The input is a list of datetime strings in the formate 'yyyy-mm-dd hh:mm:ss' and the output is only the date in the 'yyyy-mm-dd' format.
   
    Args:
        dates(list): list of datetime strings

    returns:
        list: lists of only the date strings

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
