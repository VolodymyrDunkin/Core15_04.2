lst_m = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9], [10, 11, 12, [23, 45, 67]]]

# print(lst_m[2][2][2])

for lst in lst_m:
    for element in lst:
        print(element)

print(lst_m[1].pop(0))

print(lst_m)

def flatten(data):
    result = []

    for element in data:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)

    return result

    
print(flatten(lst_m))

