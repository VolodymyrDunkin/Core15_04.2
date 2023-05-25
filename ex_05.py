car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "White")

print(car)

x = car["color"] = "Black"

print(x)