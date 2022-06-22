def Ceaser_cipher_encrypt(plain_text, key):
    encryptedtext = ""
    for c in plain_text:
        if c.isupper():
            index = ord(c) - ord('A')
            shift = (index + key) % 26 + ord('A')
            new = chr(shift)
            encryptedtext += new
        elif c.islower():
            index = ord(c) - ord('a')
            shift = (index + key) % 26 + ord('a')
            new = chr(shift)
            encryptedtext += new
        elif c.isdigit():
            new = (int(c) + key) % 10
            encryptedtext += str(new)
        else:
            encryptedtext += c
    return encryptedtext
def Ceaser_cipher_decrypt(ciphertext, key):
    decryptedtext = ""
    for c in ciphertext:
        if c.isupper():
            index = ord(c) - ord('A')
            e_position = (index - key) % 26 + ord('A')
            e = chr(e_position)
            decryptedtext += e
        elif c.islower():
            index = ord(c) - ord('a')
            e_position = (index - key) % 26 + ord('a')
            e = chr(e_position)
            decryptedtext += e
        elif c.isdigit():
            e = (int(c) - key) % 10
            decryptedtext += str(e)
        else:
            decryptedtext += c
    return decryptedtext