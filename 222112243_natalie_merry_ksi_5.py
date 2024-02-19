# -*- coding: utf-8 -*-
"""222112243_Natalie Merry_KSI 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NmCvD0yfKeKY7SjjVghtbM3z2cja3_hL

**A. Transposition Ciphers**

Enkripsi
"""

def enkrip(teks, key):
    teks_enkrip = ""

    teks = teks.replace(" ", "")

    blocks = [teks[i:i + key] for i in range(0, len(teks), key)]

    for i in range(key):
        for block in blocks:
            if len(block) > i:
                teks_enkrip += block[i]

    return teks_enkrip

def main():
    plain_text = input("Masukkan teks yang ingin dienkripsi: ")
    key = int(input("Masukkan kunci: "))
    teks_enkrip = enkrip(plain_text, key)
    print("Teks terenkripsi:", teks_enkrip)

if __name__ == "__main__":
    main()

"""Dekripsi"""

def dekrip(teks_enkrip, key):

    kolom = (len(teks_enkrip) + key - 1) // key
    baris = (len(teks_enkrip) + kolom - 1) // kolom
    kosong = (kolom * baris) - len(teks_enkrip)

    plaintext = [''] * kolom
    col = 0
    row = 0

    for symbol in teks_enkrip:
        plaintext[col] += symbol
        col += 1

        if (col == kolom) or (col == kolom - 1 and row >= baris - kosong):
            col = 0
            row += 1

    return ''.join(plaintext)

def main():
    teks_enkrip = input("Masukkan teks terenkripsi untuk didekripsi: ")
    key = int(input("Masukkan kunci : " ))

    decrypted_text = dekrip(teks_enkrip, key)
    print("Teks Asli:", decrypted_text)

if __name__ == "__main__":
    main()

"""**B. Substitution Ciphers**

Enkripsi
"""

def enkrip_subs(text, key):
    teks_enkrip = ""
    for char in text:
        char = char.lower()

        if char.isalpha():

            ascii_val = ord(char)
            shifted_ascii = ascii_val + key

            if shifted_ascii > ord('z'):
                shifted_ascii -= 26

            teks_enkrip += chr(shifted_ascii)

        else:
            teks_enkrip += char
    return teks_enkrip

def main():
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")
    key = int(input("Masukkan kunci: "))

    teks_enkrip = enkrip_subs(plaintext, key)
    print("Teks terenkripsi:", teks_enkrip)

if __name__ == "__main__":
    main()

"""Dekripsi"""

def dekrip_subs(text, key):
    teks_dekrip = ""
    for char in text:
        char = char.lower()

        if char.isalpha():
            ascii_val = ord(char)
            shifted_ascii = ascii_val - key

            if shifted_ascii < ord('a'):
                shifted_ascii += 26

            teks_dekrip += chr(shifted_ascii)
        else:
            teks_dekrip += char
    return teks_dekrip

def main():
    teks_enkrip = input("Masukkan teks terenkripsi untuk didekripsi: ")
    key = int(input("Masukkan kunci: "))

    teks_dekrip = dekrip_subs(teks_enkrip, key)
    print("Teks asli:", teks_dekrip)

if __name__ == "__main__":
    main()