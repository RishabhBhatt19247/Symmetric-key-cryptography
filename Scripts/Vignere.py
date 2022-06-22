def Vignere_generateKey(string, key):
  key = list(key)
  if len(string) == len(key):
    return(key)
  else:
    for i in range(len(string) -len(key)):
      key.append(key[i % len(key)])
  return("" . join(key))

def Vignere_cipher_encrypt(plain_text, key):
    encryptedtext = ""
    for c,k in zip(plain_text,key):
        if c.islower():
            index = ord(c) - ord('a')
            k_index = ord(k) - ord('a')
            c_shift = (index + k_index) % 26 + ord('a')
            c_new = chr(c_shift)
            encryptedtext += c_new
        else:
            encryptedtext += c
    return encryptedtext
def Vignere_cipher_decrypt(ciphertext, key):
    decryptedtext = ""
    for c,k in zip(ciphertext,key):
        if c.islower():
            index = ord(c) - ord('a')
            k_index = ord(k) - ord('a')
            e_position = (index - k_index) % 26 + ord('a')
            e = chr(e_position)
            decryptedtext += e
        else:
            decryptedtext += c

    return decryptedtext