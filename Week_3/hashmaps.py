from time import time

class HashMap:
    def __init__(self):
    #Given a key, will return the value associated with that key if it's in 
    #the Table. This function will return None if the key is not in the hash map.
    #O(1) runtime
        pass

    def put(self, key, value):
    #Inserts the key-value pair into the hashmap
    #If the key already exists it will overwrite the previous valu with the new value
    #O(1) Runtime
        pass

    def containts(self, key):
        #Returns true if it contains the key
        pass

    def _hash(self, key):
        #Private function to compute an integer hash value for a given key.
        #O(1) runtime
        pass

    def hash_integer(integer_key):
        #Set M equal to a large prime number. (We could always pick larger)
        M = 97
        return integer_key % 97
    
    def hash_string(string_key):
        M = 1001
        # R is the size of the Alphabet. Because we are working with ASCII 256,
        #We set R = 256.
        R = 256
        hash_value = 0
        for char in string_key:
            hash_value = (hash_value * R + int(char)) % M
        return hash_value
    
    

#Properties of a Hash Function
#Deterministic  - The same key will always produce the same hash value
#Efficient - It should be fast to compute
#Uniform - The hash function should distribute  the keys uniformly

# These three functions below DO NOT SATISFY the above conditions
    
    #Hash returns the current time in seconds mod 97
    def non_deterministic_hash(integer_key):
        M = 97
        current_time_int = int(time.time())
        return current_time_int % 97
    
    #Hash returns the square of integer key mod M
    def non_efficient_hash(integer_key):
        M = 97
        hash_value = 0
        for i in range(integer_key):
            M = 97
            hash_value = 0
            for i in range(integer_key):
                for j in range(integer_key):
                    hash_value += 1
        return hash_value % M
        
    
    #Hash that maps every integer key to 1.
    def non_uniform_hash(integer_key):
        return 1

    


