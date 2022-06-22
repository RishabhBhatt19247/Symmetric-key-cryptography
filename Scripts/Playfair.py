def Playfair_key_matrix(key):
    atoz = 'abcdefghiklmnopqrstuvwxyz'
    k_mat = ['' for i in range(5)]
    visited = []
    i, j = 0,0
    for k in key:
        if k in atoz and k not in visited:
            k_mat[i]+=k
            visited+=k
            atoz = atoz.replace(k,'')
            j+=1
            if j>4:
                i+=1
                j=0
    for k in atoz:
        if k in atoz and k not in visited:
            k_mat[i]+=k
            visited.append(k)
            atoz.replace(k,'')
            j+=1
            if j>4:
                i+=1
                j=0

    return k_mat
def Playfair_cipher_encrypt(key_mat,plaintext):
    plain_pair = []
    cipher_pair = []
    i = 0
    while i<len(plaintext):
        a = plaintext[i]
        b = ''
        if (i+1) == len(plaintext):
            b='x'
        else:
            b = plaintext[i+1]
        if a!=b:
            plain_pair.append(a+b)
            i+=2
        else:
            if a == 'x':
                plain_pair.append(a+'a')
            else:
                plain_pair.append(a+'x')
            i+=1

    print(plain_pair)

    for pair in plain_pair:
        flag = False
        for row in key_mat:
            if pair[0] in row and pair[1] in row:
                cipher_pair.append(row[((row.find(pair[0]))+1)%5] + row[((row.find(pair[1]))+1)%5])
                flag = True
        if flag:
            continue
        for j in range(5):
            col = "".join(key_mat[i][j] for i in range(5))
            if pair[0] in col and pair[1] in col:
                cipher_pair.append(col[((col.find(pair[0]))+1)%5] + col[((col.find(pair[1]))+1)%5])
                flag = True
        if flag:
            continue
        i0,i1,j0,j1 = 0,0,0,0
        for i in range(5):
            row = key_mat[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])
        cipher_pair.append(key_mat[i0][j1]+key_mat[i1][j0])

    return cipher_pair

def Playfair_cipher_decrypt(key_mat,ciphertext):
    cipher_pair = []
    plain_pair = []
    i = 0
    while i<len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1]
        cipher_pair.append(a+b)
        i+=2
    print(cipher_pair)

    for pair in cipher_pair:
        flag = False
        for row in key_mat:
            if pair[0] in row and pair[1] in row:
                plain_pair.append(row[((row.find(pair[0]))-1)%5] + row[((row.find(pair[1]))-1)%5])
                flag = True
        if flag:
            continue
        for j in range(5):
            col = "".join(key_mat[i][j] for i in range(5))
            if pair[0] in col and pair[1] in col:
                plain_pair.append(col[((col.find(pair[0]))-1)%5] + col[((col.find(pair[1]))-1)%5])
                flag = True
        if flag:
            continue
        i0,i1,j0,j1 = 0,0,0,0
        for i in range(5):
            row = key_mat[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])
            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])
        plain_pair.append(key_mat[i0][j1]+key_mat[i1][j0])

    return plain_pair