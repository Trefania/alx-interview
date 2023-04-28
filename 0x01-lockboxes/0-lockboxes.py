#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes: A list of lists, where each inner list represents a box and
           contains the keys to other boxes.

    Returns:
    True if all boxes can be opened, else False.
    """
    num_boxes = len(boxes)
    # create a list to keep track of which boxes are unlocked
    unlocked = [True] * num_boxes
    # the first box is unlocked by default
    unlocked[0] = True
    # create a list to keep track of the keys we have
    keys = [0]
    # loop through the keys we have and try to unlock new boxes
    while keys:
        # get the first key from the list
        key = keys.pop(0)
        # loop through the boxes the key can unlock
        for box in boxes[key]:
            # check if the box is already unlocked
            if not unlocked[box]:
                # unlock the box
                unlocked[box] = True
                # add the keys from the box to the list
                keys.extend(boxes[box])
    # check if all boxes are unlocked
    return all(unlocked)
