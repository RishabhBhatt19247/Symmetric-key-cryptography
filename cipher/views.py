from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import sys
sys.path.extend(['./Scripts'])
from Ceaser import Ceaser_cipher_encrypt,Ceaser_cipher_decrypt
from Multiplicative import multiplicative_cipher_decrypt,multiplicative_cipher_encrypt,modInverse
from Affine import affine_cipher_encrypt, affine_cipher_decrypt
from Autokey import Autokey_cipher_encrypt,Autokey_cipher_decrypt
from Vignere import Vignere_generateKey,Vignere_cipher_encrypt,Vignere_cipher_decrypt
from Playfair import Playfair_key_matrix,Playfair_cipher_encrypt,Playfair_cipher_decrypt

def button(request):
    return render(request,'index.html')
def Ceaser(request):
    return render(request,'Ceaser.html')
def Multiplicative(request):
    return render(request,'Multiplicative.html')
def Affine(request):
    return render(request,'Affine.html')
def Autokey(request):
    return render(request,'Autokey.html')
def Vignere(request):
    return render(request,'Vignere.html')
def Playfair(request):
    return render(request,'Playfair.html')

# Create your views here.
def output(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key = request.POST['Key']
        if key.isdigit() :
            key = int(key)
            if 'decrypt' in request.POST:
                encryptedtext = Ceaser_cipher_encrypt(text,key)
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                decryptedtext = Ceaser_cipher_decrypt(text,key)
                data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
    return render(request,"Ceaser.html",{'data':data})

#multiplicative Cipher
def multiplicative(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key = request.POST['Key']
        if key.isdigit() :
            key = int(key)
            if 'decrypt' in request.POST:
                encryptedtext = multiplicative_cipher_encrypt(text,key)
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                key = modInverse(key,26)
                if key== -1:
                    data = 'Key not possible'
                else:
                    decryptedtext = multiplicative_cipher_decrypt(text,key)
                    data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
    return render(request,"Multiplicative.html",{'data':data})

def affine(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key1 = request.POST['Key1']
        key2 = request.POST['Key2']
        if key1.isdigit() and key2.isdigit() :
            key1 = int(key1)
            key2 = int(key2)
            if 'decrypt' in request.POST:
                encryptedtext = affine_cipher_encrypt(text,key1,key2)
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                key1 = modInverse(key1,26)
                if key1== -1:
                    data = 'Key not possible'
                else:
                    decryptedtext = affine_cipher_decrypt(text,key1,key2)
                    data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
    return render(request,"Affine.html",{'data':data})

def autokey(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key = request.POST['Key']
        if key.isdigit() :
            key = int(key)
            if 'decrypt' in request.POST:
                encryptedtext = Autokey_cipher_encrypt(text,key)
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                if key== -1:
                    data = 'Key not possible'
                else:
                    decryptedtext = Autokey_cipher_decrypt(text,key)
                    data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
    return render(request,"Autokey.html",{'data':data})
def vignere(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key = request.POST['Key']
        text = text.lower()
        key = key.lower()
        if key.islower() :
            key = Vignere_generateKey(text,key)
            if 'decrypt' in request.POST:
                encryptedtext = Vignere_cipher_encrypt(text,key)
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                if key== -1:
                    data = 'Key not possible'
                else:
                    decryptedtext = Vignere_cipher_decrypt(text,key)
                    data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
    return render(request,"Vignere.html",{'data':data})

def playfair(request):
    if request.method == "POST" :
        text = request.POST['Data']
        key = request.POST['Key']
        text = "".join([char for char in text.lower() if char.isalnum()])
        key = key.lower()
        if key.isalpha():
            key = Playfair_key_matrix(key)
            if 'decrypt' in request.POST:
                encryptedtext = Playfair_cipher_encrypt(key,text)
                encryptedtext_pair = " ".join(encryptedtext)
                encryptedtext = "".join(encryptedtext)
                data1 = 'encryptedtext pair : ' + encryptedtext_pair
                data = 'encrypted text :  '+ encryptedtext
            elif 'encrypt' in request.POST:
                if key== -1:
                    data = 'Key not possible'
                else:
                    decryptedtext = Playfair_cipher_decrypt(key,text)
                    decryptedtext_pair = " ".join(decryptedtext)
                    decryptedtext = "".join(decryptedtext)
                    data1 = 'encryptedtext pair : ' + decryptedtext_pair
                    data = 'decrypted text :  '+ decryptedtext
        else:
            data = 'key data is not valid'
            data1 = ''
    return render(request,"Playfair.html",{'data1':data1,'data':data})
