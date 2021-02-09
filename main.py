# import the library module
import hashlib
 
# initialize a id
id = "bettioui farid"
 
# encode the string
encoded_str = id.encode()
 
# create a sha1 hash object initialized with the encoded string
hash_obj = hashlib.sha1(encoded_str)
 
# convert the hash object to a hexadecimal value
hexa_value = hash_obj.hexdigest()
 
# print
print("\n", hexa_value, "\n")