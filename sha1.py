# import the library module
import hashlib

def shaone (text):
    # encode the string
    encoded_str = text.encode()

    # create a sha1 hash object initialized with the encoded string
    hash_obj = hashlib.sha1(encoded_str)

    # convert the hash object to a hexadecimal value
    hexa_value = hash_obj.hexdigest()

    return hexa_value

def H(text1,text2):
    id = text1
    y = text2
    x = 0   #35    23

    while True :
        
        print('\n\n==> X = ',x ,'\n===> X apres le hashage est : ',shaone( str(x) ))
        h = shaone( id + str(x) )
        
        if h <= y :
            print('====> la valeur de H apres le hashage : ',shaone(id + str(x)) )
            return x
        
        x += 1
        
id = input("veuillez-vous saiser votre ID : ")
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"

x = H(id , y)

#X apres le hashage est :  972a67c48192728a34979d9a35164c1295401b71
#la valeur de H apres le hashage :  034d56442f5cd7e3141ef357db246ed4faf7b1e5