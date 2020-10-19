#!/usr/bin/env python3

def urlify(text):
    return text.replace(" ", "%20")

print(urlify("http://this.com: this is a test"))
