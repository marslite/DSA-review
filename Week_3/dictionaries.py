name_to_age_map = {}
name_to_age_map["Ann"] = 16
name_to_age_map["Bob"] = 12
name_to_age_map["Sam"] = 14


# .keys() returns a list of all keys in the dictionary
print(name_to_age_map.keys()) #["Ann","Bob","Sam"]

# .values() returns a list of all values in the dictionary
print(name_to_age_map.values()) #[16,12,14]

# .items() returns a list of tuples with all the key value pairs in the dict
print(name_to_age_map.items())

# We can then check if any key is in the dict within O(1) time complexity.
print("Ryan" in name_to_age_map) #False
print("Bob" in name_to_age_map) #True

#Directly accessing a key that does not exists will result in an error.
# name_to_age_map["Ryan"] #This will throw an error because Ryan is not a key

#This instead will check if "Ryan" by checking all the elements  in a list, not a dictionary
print("Sam" in name_to_age_map.keys())
