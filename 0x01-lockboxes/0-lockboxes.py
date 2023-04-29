#!/usr/bin/python3
"""
LockBoxes Module
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    Args:
        boxes: A list of lists, where each inner list represents a box and
               contains the keys to other boxes.
    Returns:
        True if all boxes can be opened, else False.
    """
    unlocked = [0]  # List of boxes unlocked
    # iterates through the outer list to get the index and inner list
    for box_id, box in enumerate(boxes):
        if not box:  # if box is empty, continue.
            continue
        for key in box:
            # iterate through the inner list and compare the values
            # the condition checks for values that is less than the box length
            # that hasn't been unlocked yet and it is not
            # the same value as its index.
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)  # then we append it to the unlock list
    # if the len of the unlock and original box is same.
    # then all box can be unlocked.
    if len(unlocked) == len(boxes):
        return True
    return False