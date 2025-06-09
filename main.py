import pandas as pd

from algorithms import rc4, bytes_to_bits, a5_1_encrypt, bits_to_bytes, append_to_excel


def rc4_run(text, key):
    rc4_encrypted = rc4(key.encode(), text.encode())
    rc4_deciphered = rc4(key.encode(), rc4_encrypted)

    row = {
        "Matn": text,
        "Kalit": key,
        "Shifrlangan matn (RC4)": rc4_encrypted.hex(),
        "Deshifrlangan matn (RC4)": rc4_deciphered.decode()
    }
    append_to_excel("rc4_natija.xlsx", row)
    return {"Shifrlangan matn (RC4)": rc4_encrypted.hex()}

def a5_1_run(text, key):
    key_bits_64 = [int(b) for b in format(int.from_bytes(key.encode()[:8].ljust(8, b'\0'), 'big'), '064b')]
    matn_bits = bytes_to_bits(text.encode())

    a5_1_encrypted_bits = a5_1_encrypt(key_bits_64, matn_bits)
    a5_1_encrypted = bits_to_bytes(a5_1_encrypted_bits)

    a5_1_deciphered_bits = a5_1_encrypt(key_bits_64, a5_1_encrypted_bits)
    a5_1_deciphered = bits_to_bytes(a5_1_deciphered_bits)

    row = {
        "Matn": text,
        "Kalit": key,
        "Shifrlangan matn (A5/1)": a5_1_encrypted.hex(),
        "Deshifrlangan matn (A5/1)": a5_1_deciphered.decode()
    }
    append_to_excel("a5_1_natija.xlsx", row)
    return {'Shifrlangan matn (A5/1)': a5_1_encrypted.hex()}


# 🔧 Asosiy ishlovchi qism
if __name__ == "__main__":

    def main():
        algorithm_selection = input(
"""
Algoritmni turini tanlang 
    0. Chiqish
    1. RC4
    2. A5/1
    >>> """)

        if algorithm_selection == "1":
            text = input("Matn kiriting: ")
            key = input("Kalit kiriting (kamida 8 ta belgili): ")
            print(rc4_run(text, key))
            main()

        elif algorithm_selection == "2":
            text = input("Matn kiriting: ")
            key = input("Kalit kiriting (kamida 8 ta belgili): ")
            print(a5_1_run(text, key))
            main()
        elif algorithm_selection == "0":
            print("Dasturdan chiqildi")
        else:
            print("Noto'g'ri tanlov")
            return main()
    main()