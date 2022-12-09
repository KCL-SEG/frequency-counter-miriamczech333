"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items: 
        item_s = str(item)
        if item_s not in frequencies: 
            n = 0
            for i in range(len(items)):
                if str(items[i]) == item_s:
                    n = n + 1
            frequencies[item_s] = n

    return frequencies
