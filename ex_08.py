key = "name"
key1 = "cicle"

lst = ["name", "age", "height"]

if key not in lst:
    print("Yes")
else:
    print("No")

dct = dict.fromkeys(lst, "KLdlfjksciclekjfcmkdj")

print(dct)

if key1 in dct.values():
    print("Yes")
else:
     print("No")
     
print(str(dct.values()))