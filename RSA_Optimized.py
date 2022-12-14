# This is a program to run a more optimized version of RSA to comprare time
# with Shor's Algorithm.

# https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import numpy as np
from decimal import Decimal

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)

print('-' * 20 + ' n (Product of p and q) ' + '-' * 20)
print(pubKey.n)

print("This key will take a classical computer over 300 trillion years to crack")
