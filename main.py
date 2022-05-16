from algorithm import *

operation = input("Encryption or Decryption ? (e/d)")
if operation.lower() == "e":
    plaintext = input("plaintext : ")
    katakunci = input("kata kunci : ")
    ciphertext = enkripsi(plaintext, katakunci)
    print(ciphertext)
elif operation.lower() == "d":
    ciphertext = input("ciphertext : ")
    katakunci = input("kata kunci : ")
    plaintext = dekripsi(ciphertext, katakunci)
    print(plaintext)
