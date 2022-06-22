def Autokey_cipher_encrypt(plain_text, key):
    encryptedtext = ""
    for c in plain_text:
        if c.isupper():
            index = ord(c) - ord('A')
            c_shift = (index + key) % 26 + ord('A')
            c_new = chr(c_shift)
            encryptedtext += c_new
            key = index
        elif c.islower():
            index = ord(c) - ord('a')
            c_shift = (index + key) % 26 + ord('a')
            c_new = chr(c_shift)
            encryptedtext += c_new
            key = index
        else:
            encryptedtext += c
    return encryptedtext
def Autokey_cipher_decrypt(ciphertext, key):
    decryptedtext = ""
    for c in ciphertext:
        if c.isupper():
            index = ord(c) - ord('A')
            e_position = (index - key) % 26 + ord('A')
            e = chr(e_position)
            decryptedtext += e
            key = (index - key) % 26
        elif c.islower():
            index = ord(c) - ord('a')
            e_position = (index - key) % 26 + ord('a')
            e = chr(e_position)
            decryptedtext += e
            key = (index - key) % 26
        else:
            decryptedtext += c

    return decryptedtext
