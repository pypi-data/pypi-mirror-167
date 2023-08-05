import re


def char_to_num(text):
    return ord(text.lower()) - 97

def num_to_char(num):
    return chr(num + 97).lower()

def clean_text(text):
    return re.sub('[^A-Za-z\s!?., $]*', '', text.lower())

def tvd(freq1, freq2):
    # Takes in two numpy arrays of length 26.
    diff = abs(freq1 - freq2)
    return sum(diff)/2

def pad_key(key, length):
    key = clean_text(key)
    newkey = ""
    k = 0
    while len(newkey) < length:
        newkey += key[k]
        k+=1
        k%=len(key)
    return newkey

def shift_letter(char, shift):
    if not char.isalpha():
        return char
    else:
        return num_to_char((char_to_num(char) + shift) % 26) 