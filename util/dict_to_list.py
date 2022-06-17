def dict_to_list(data):
    """
    change type dict to list
    """
    d_l = list()
    for key, value in data.items():
        temp = [key,value]
        d_l.append(temp)
    return d_l
