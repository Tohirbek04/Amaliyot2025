# RC4 funksiyasi
import os
import pandas as pd

def rc4(key: bytes, data: bytes) -> bytes:
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    keystream = []
    for _ in range(len(data)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return bytes([c ^ k for c, k in zip(data, keystream)])


# A5/1 funksiyalari
class LFSR:
    def __init__(self, size, taps, clock_bit):
        self.reg = [0] * size
        self.taps = taps
        self.clock_bit = clock_bit

    def clock(self):
        xor = 0
        for t in self.taps:
            xor ^= self.reg[t]
        self.reg = [xor] + self.reg[:-1]

    def get_bit(self):
        return self.reg[-1]

    def load_key(self, key_bits):
        for i in range(len(self.reg)):
            self.reg[i] = key_bits[i]

def majority(a, b, c):
    return (a & b) | (a & c) | (b & c)

def a5_1_encrypt(key_bits, plaintext_bits):
    R1 = LFSR(19, [13, 16, 17, 18], 8)
    R2 = LFSR(22, [20, 21], 10)
    R3 = LFSR(23, [7, 20, 21, 22], 10)

    R1.load_key(key_bits[:19])
    R2.load_key(key_bits[19:41])
    R3.load_key(key_bits[41:64])

    keystream = []
    for _ in range(len(plaintext_bits)):
        m = majority(R1.reg[R1.clock_bit], R2.reg[R2.clock_bit], R3.reg[R3.clock_bit])
        if R1.reg[R1.clock_bit] == m:
            R1.clock()
        if R2.reg[R2.clock_bit] == m:
            R2.clock()
        if R3.reg[R3.clock_bit] == m:
            R3.clock()
        keystream.append(R1.get_bit() ^ R2.get_bit() ^ R3.get_bit())

    return [p ^ k for p, k in zip(plaintext_bits, keystream)]

def bytes_to_bits(data: bytes) -> list:
    return [int(b) for byte in data for b in format(byte, '08b')]

def bits_to_bytes(bits: list) -> bytes:
    return bytes([int("".join(map(str, bits[i:i+8])), 2) for i in range(0, len(bits), 8)])

def append_to_excel(filename, new_row):
    if os.path.exists(filename):
        old_df = pd.read_excel(filename)
        new_df = pd.concat([old_df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        new_df = pd.DataFrame([new_row])
    new_df.to_excel(filename, index=False)