# import the library module
import hashlib

def shaone (text):

    # encode the string
    encoded_str = text.encode()
    
    # create a sha1 hash object initialized with the encoded string
    hash_obj = hashlib.sha1(encoded_str)
    
    # convert the hash object to a hexadecimal value
    hexa_value = hash_obj.hexdigest()

    # print
    print("\n", hexa_value, "\n")

    return hexa_value

def H(text1,text2):
    id = text1
    y = text2
    x = 0

    while x < 100 :
        h = shaone(id + str(x) )
        
        if h <= y :
            print('le nombre de tentative est: ',x)
            print( shaone(x) )

            return x
        
        x += 1
        


id = "bettiouifarid"
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"

x = H(id , y)

