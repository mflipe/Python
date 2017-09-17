# Regex Version of strip()
# Marcos Felipe
# 03/09/2017

# Write a function that takes a string and does the same thing as the strip() string method.
# If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string. Otherwise,
# the characters specified in the second argument to the function will be removed from the string.
import re

def rStrip(rString):
    regex = re.compile(r'''
        (^\s)*(.[^\s]*)(\s$)*
        ''', re.VERBOSE)
    print(rString)
    rString = regex.sub(r'\2', rString)
    print(rString)
    return rString

def rStrip(rString, sept):
    regex = re.compile(re.escape(sept), re.IGNORECASE)
    print(rString, sept)
    rString = regex.sub(r'', rString)
    print(rString, sept)
    return rString

rStrip('Sábado cedo não tem carne.', ' não')
