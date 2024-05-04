def feistel_cipher(plaintext, key, rounds):
   
    left_half = plaintext[:len(plaintext)//2]
    right_half = plaintext[len(plaintext)//2:]

  
    for round in range(rounds):
        temp = right_half

        right_half = xor(left_half, round_function(right_half, key))
      
        left_half = temp

   
    ciphertext = left_half + right_half
    return ciphertext

def round_function(data, round_key):
   
    return xor(data, round_key)

def xor(a, b):
   
    result = ""
    for char_a, char_b in zip(a, b):
        result += str(int(char_a) ^ int(char_b))
    return result

