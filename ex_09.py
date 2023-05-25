dct = {str(x): [x] * 3 for x in range(10)}

for key, value in dct.items():
    print(f"{key} - {sum(value)}")