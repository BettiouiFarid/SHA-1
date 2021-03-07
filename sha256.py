# import the library module
import hashlib

def sha256 (text):
    # encode the string
    encoded_str = text.encode()

    # create a sha1 hash object initialized with the encoded string
    hash_obj = hashlib.sha256(encoded_str)

    # convert the hash object to a hexadecimal value
    hexa_value = hash_obj.hexdigest()

    return hexa_value

def H(text1,text2):
    id = text1
    y = text2
    x = 0       #10000000015880       20505

    while True :
        
        print('\n\n==> X = ',x ,'\n===> X apres le hashage est : ',sha256( str(x) ))
        h = sha256( id + str(x) )
        
        if h <= y :
            print('====> la valeur de H apres le hashage : ',sha256(id + str(x)) )
            return x
        
        x += 1
        
id = input("veuillez-vous saiser votre ID : ")
y = "00005d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4"

x = H(id , y)

#X apres le hashage est :  bdc954f3c2058d4a7a5c349cccc8295eac3d244ac2c2b7383b447d76fb0a2830
#la valeur de H apres le hashage :  00000a04e461b771d88284ed986dd69b49f3ab3ef19898cd7ee821b93a4da3c9