def cube(num):
    """
    Return cubed num.
    :num param: int or float.
    :return: cubed number.
    """
    try:
        return num**3
    except ValueError:
        print("fuck off")
