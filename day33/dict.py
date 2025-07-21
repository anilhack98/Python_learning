dict={"Anil":"Boy NAME","Email":"anilchau5492@gmail.com","Ph.No":"9817243758"}
print(dict["Anil"])
print(dict["Email"])
print(dict["Ph.No"])
print(dict.keys())  # Prints all the Keys
print(dict.values())  # To Print values

# TO print the values Other method
for key in dict.keys():
    print(f"The value corresponding to the key {key} is {dict[key]}")

print(dict.items())
for key,value in dict.items():
    print(f"The value corresponding to the key {key} is {value}")