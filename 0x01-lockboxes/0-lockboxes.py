#!/usr/bin/python3

"""Simple code which determines if all boxes in a list can be unlocked"""

def canUnlockAll(boxes):
    # list of unlocked boxes
    unlocked_boxes = [0]

    # iterate over unlocked boxes and add keys to new boxes
    for box in unlocked_boxes:
        for key in boxes[box]:
            if key not in unlocked_boxes:
                unlocked_boxes.append(key)

    # if all boxes are unlocked, return True
    return len(unlocked_boxes) == len(boxes)
