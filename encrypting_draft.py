import binascii
import secrets


def XOR(known_binary, random_code):
    random_message = ''
    for i in range(len(known_binary)):
        if known_binary[i] == '0' and random_code[i] == '0':
            random_message = random_message + '0'
        if known_binary[i] == '1' and random_code[i] == '0':
            random_message = random_message + '1'
        if known_binary[i] == '0' and random_code[i] == '1':
            random_message = random_message + '1'
        if known_binary[i] == '1' and random_code[i] == '1':
            random_message = random_message + '0'
    return random_message

wiadomosc = 'ja'
wiadomosc_binarna = bin(int.from_bytes(wiadomosc.encode(), 'big'))  #zamiana wiadomosci na ciag 01
print(wiadomosc_binarna)

wiadomosc_binarna_czysta = wiadomosc_binarna[2:]
print(wiadomosc_binarna_czysta, 'Wiadomosc zamieniona na 01')

klucz = ''
for i in wiadomosc_binarna_czysta:
    randomowo_generowane = str((secrets.choice((0,1))))
    klucz = klucz+randomowo_generowane
print(klucz,'Losowy klucz')

zaszyfowana_wiadomosc = XOR(wiadomosc_binarna_czysta, klucz)
hash_blockchain = int('0b'+zaszyfowana_wiadomosc, 2)
print("To jest wiadomosc ktora przekazujemy na blockchain: ", hash_blockchain)

"""ODSZYFROWYWANIE"""

przekonwertowany_hash = bin(hash_blockchain)[2:]
print(przekonwertowany_hash)
print(len(przekonwertowany_hash), len(klucz))
wiadomosc_koncowa = XOR(przekonwertowany_hash, klucz)
m = int('0b'+wiadomosc_koncowa, 2)
print(przekonwertowany_hash)
print(klucz)
original = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
print(original)

