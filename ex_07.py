first_people = "Illon Musk"
second_people = "Steve Jobs"
first_set = set(first_people)
second_set = set(second_people)

print(first_set, second_set)

print(len(first_people) == len(first_set))

# print(first_set[1])

print(first_set & second_set)
print(first_set | second_set)
print(first_set ^ second_set)
print(first_set.difference(second_set))


