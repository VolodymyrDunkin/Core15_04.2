from sys import argv

print(argv[0])

mode = ""

# try:
#     mode = argv[1]
# except IndexError as e:
#     print(f"{e}")

# if mode == "d":
#     print("Debug mode")
# else:
#     print("Prod mode")

# for i in argv:
#     mode += i + " "

print(" ".join(argv))