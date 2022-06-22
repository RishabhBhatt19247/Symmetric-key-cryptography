def multiplicative_cipher_encrypt(plain_text, key):
    encryptedtext = ""
    for c in plain_text:
        if c.isupper():
            index = ord(c) - ord('A')
            c_shift = (index * key) % 26 + ord('A')
            c_new = chr(c_shift)
            encryptedtext += c_new
        elif c.islower():
            index = ord(c) - ord('a')
            c_shifted = (index * key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encryptedtext += c_new
        else:
            encryptedtext += c
    return encryptedtext
def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return -1
def multiplicative_cipher_decrypt(ciphertext, key):
    decryptedtext = ""
    for c in ciphertext:
        if c.isupper():
            index = ord(c) - ord('A')
            e_postion = (index * key) % 26 + ord('A')
            e = chr(e_postion)
            decryptedtext += e
        elif c.islower():
            index = ord(c) - ord('a')
            e_postion = (index * key) % 26 + ord('a')
            e = chr(e_postion)
            decryptedtext += e
        else:
            decryptedtext += c
    return decryptedtext