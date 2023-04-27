#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]
    for key in keys:
        if key < n:
            opened[key] = True
            keys += boxes[key]
    while True:
        new_keys = False
        for i in range(n):
            if opened[i]:
                keys = boxes[i]
                for key in keys:
                    if key < n and not opened[key]:
                        opened[key] = True
                        new_keys = True
        if not new_keys:
            break
    return all(opened)








