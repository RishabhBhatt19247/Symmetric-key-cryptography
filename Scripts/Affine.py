def affine_cipher_encrypt(plain_text, key1,key2):
    encryptedtext = ""
    for c in plain_text:
        if c.isupper():
            index = ord(c) - ord('A')
            c_shift = ((index * key1)+key2) % 26 + ord('A')
            c_new = chr(c_shift)
            encryptedtext += c_new
        elif c.islower():
            index = ord(c) - ord('a')
            c_shift = ((index * key1) + key2 )% 26 + ord('a')
            c_new = chr(c_shift)
            encryptedtext += c_new
        else:
            encryptedtext += c
    return encryptedtext
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1
def affine_cipher_decrypt(ciphertext, key1,key2):
    decryptedtext = ""
    for c in ciphertext:
        if c.isupper():
            index = ord(c) - ord('A')
            e_position = ((index-key2) * key1) % 26 + ord('A')
            e = chr(e_position)
            decryptedtext += e
        elif c.islower():
            c_index = ord(c) - ord('a')
            e_position = ((c_index-key2) * key1) % 26 + ord('a')
            e = chr(e_position)
            decryptedtext += e
        else:
            decryptedtext += c
    return decryptedtext