from .utils import * 
import numpy as np

alphabet = "abdcedfghijklmnopqrstuvwxyz"
english_frequencies = {
    'a': .0812,
    'b': .0149,
    'c': .0271,
    'd': .0432,
    'e': .1202,
    'f': .0230,
    'g': .0203,
    'h': .0592,
    'i': .0731,
    'j': .0100,
    'k': .0069,
    'l': .0398,
    'm': .0261,
    'n': .0695,
    'o': .0768,
    'p': .0182,
    'q': .0011,
    'r': .0602,
    's': .0628,
    't': .0910,
    'u': .0288,
    'v': .0111,
    'w': .0209,
    'x': .0017,
    'y': .0211,
    'z': .0007
}
np_english_frequencies = np.fromiter(english_frequencies.values(), dtype=float)

def caesar_encrypt(plaintext, shift):
    plaintext = clean_text(plaintext)
    encrypted = ""
    for i in range(len(plaintext)):
        encrypted += shift_letter(plaintext[i], shift)
    return encrypted

def caesar_decrypt(ciphertext, shift):
    ciphertext = clean_text(ciphertext)
    decrypted = ""
    for i in range(len(ciphertext)):
        decrypted += shift_letter(ciphertext[i], -shift)
    return decrypted

def count_letters(text):
    # Return a dictionary with the counts of every letter.
    counts = {}
    text = text.lower()
    for letter in alphabet:
        counts[letter] = 0
    for letter in text:
        if (letter in alphabet):
            counts[letter] += 1
    
    return counts

def calculate_proportions(text): # Coded for you
    counts = count_letters(text).values()
    nparr = np.fromiter(counts, dtype=float)
    return nparr / sum(counts)

def find_best_shift(ciphertext):
    best_shift = 0
    best_tvd = 100
    
    for i in range(26):
        shifted = caesar_decrypt(ciphertext, i)
        shifted_freqs = calculate_proportions(shifted)
        result_tvd = tvd(np_english_frequencies, shifted_freqs)
        
        if (result_tvd < best_tvd):
            best_shift = i
            best_tvd = result_tvd
    
    return best_shift

def crack_caesar(ciphertext):
    shift = find_best_shift(ciphertext)
    return caesar_decrypt(ciphertext, shift)