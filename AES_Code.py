from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
# pip install pycryptodome
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text

# Example 
plaintext = b"Hello,AyA!"
key = get_random_bytes(16)  # Generate a random 128-bit key
print("Plaintext:", plaintext)

# Encryption
encrypted_text = aes_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decryption
decrypted_text = aes_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
