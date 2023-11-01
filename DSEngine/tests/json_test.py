from DSEngine import *

datadict = {"foo": "bar"}

#save("test.sav", datadict)
data = load("test.sav")
print(data["foo"])