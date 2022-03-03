"""Exercise 9: Rename Method"""


# TODO: Rename this function to reflect what it's doing.
def cal_un_gr(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################


def get_value(li):  # TODO: Rename this function to reflect what it's doing.
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_value(li))

############################


# TODO: Rename this function to reflect what it's doing.
def process(sentence):
    words = sentence[0:].split(' ')
    return words


print(process('If you were a vegetable, you\'d be a \'cute-cumber.\''))
