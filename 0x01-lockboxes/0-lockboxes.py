#!/usr/bin/python3
def canUnlockAll(boxes):

    # Initialize a set to store the keys we have

    keys = set(boxes[0])

    # Initialize a set to store the opened boxes

    opened_boxes = {0}

    # Keep track of the number of boxes we've opened

    num_opened_boxes = 1

    # While we have keys and there are still unopened boxes

    while keys and num_opened_boxes < len(boxes):

        # Try to open a new box with the keys we have

        new_keys = set()

        for key in keys:

            if key < len(boxes) and key not in opened_boxes:

                opened_boxes.add(key)

                new_keys.update(boxes[key])

                num_opened_boxes += 1

        # Update the keys we have

        keys = new_keys

    # Return True if all boxes are opened, else return False

    return num_opened_boxes == len(boxes)
