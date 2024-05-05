from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.decrypt(ciphertext)

# Example:
plaintext = b"Hello,AyA!"
key = get_random_bytes(8)  # Generate a random 64-bit key
print("Plaintext:", plaintext)

# Encryption
encrypted_text = des_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = des_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
