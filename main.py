# import the library module
import hashlib
import random
import string

#Fonctions
def sha(text,result):
    count = 0
    
    x = "0"
    h = hashlib.new(text,x) 
    
    print (h.hexdigest())
    
    
    while 1:

        count += 1
        
        
        x = string.ascii_lowercase
        print ( ''.join(random.choice(x) for i in range(count)) )
        

        if h <= result:
            print(x)
            return x
    

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


# initialize a id
id = "bettiouifarid"

# initialize the Y
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"
