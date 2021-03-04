# import the library module
import hashlib

#Fonctions
def sha(text):
    x = "0"
    h = 0



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
id = shaone("bettiouifarid")

# initialize the Y
y = "03b1663dda6549a0939ffdd712a852e0d4234e6b"
