
lucky_numbers = [4, 8, 15,16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed ")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.pop()
lucky_numbers.sort()
lucky_numbers.reverse()

friends2 = friends.copy()

# friends.clear()
print(friends.index("Oscar"))
print(friends.count("Jim"))
print(friends2)