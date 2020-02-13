#Function3

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
    """"      

        mylist= []
        for date in dates:
            mylist.append(date[:10])
        return mylist

#__________________________________________________________________________________________________________________________________________