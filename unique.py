#!/usr/bin/env python3

def unique(text):
    chars = []
    for char in text:
        if char not in chars:
            chars.append(char)
        else:
            return False
    return True

print(unique("abczxhj"))
print(unique("abxhjazut"))
