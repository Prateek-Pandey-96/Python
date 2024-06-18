# key-value pairs, unordered, mutable
# basically a hashmap in cpp

# create a dict
mydict = {"name": "prateek", "age": "27", "city": "new york"}

# using dict keyword
mydict2 = dict(name="prateek", age="27", city="new york")
mydict2["email"] = "abc@gmail.com"

# del a key
del mydict2["email"]

# check for a key
if "name" in mydict2:
    print(mydict2["name"])

# loop in a dict
for key in mydict2:
    print(key, "-", mydict2[key])

# both key and val
for key, val in mydict2.items():
    print(key, "-", val)

# copy by reference -> changing copy dict will change original dict as well
# similar stuff happens for lists as well
mydict_copy = mydict

# make an actual copy
my_dict_copy2 = mydict.copy()
print(my_dict_copy2)

# tuple as a key
mytupel = (2, 3)
dict_x = {mytupel: 5}
print(dict_x)

# list can't be used as a key 
mylist = [2, 3]
dict_y = {mylist: 5}
print(dict_y)