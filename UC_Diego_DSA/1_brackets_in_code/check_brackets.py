"""_summary_
"""

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    """check if the opening brackect matches the closing bracket

    Parameters
    ----------
    left : str
        opening bracket
    right : str
        closing bracket

    Returns
    -------
    bool
        return True if matched, else False
    """
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    """ Find the postion of the first unmacthed brackets

    Parameters
    ----------
    text : str
        strings

    Returns
    -------
    int, str
        The index of the first unmacthed opening bracket, else 'Success'
    """

    opening_brackets_stack = []
    for pos_idx, char in enumerate(text):
        item = Bracket(char, pos_idx+1)
        if item.char in "([{":
            # Process opening bracket
            opening_brackets_stack.append(item)
        if item.char in ")]}":
            # Process closing bracket
            # check if the stack is empty
            if not opening_brackets_stack:
                return item.position
            open_item = opening_brackets_stack.pop()
            if not are_matching(open_item.char, item.char):
                return item.position
    #
    if opening_brackets_stack:
        item = opening_brackets_stack.pop()
        return item.position
    else:
        return 'Success'

def main():
    """run the main program
    """
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
