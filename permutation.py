#!/usr/bin/env python3

def permutation(text1, text2):
    text1Sorted = sorted(text1)
    text2Sorted = sorted(text2)
    return (text1Sorted == text2Sorted)

print(permutation("abcde", "cbead"))
print(permutation("abcde", "edcba"))
print(permutation("abcde", "abcdz"))
