lucky_numbers = [4,6,8,15,16,23,42,1]
friends = ["Kevin","Karen","Jim","Oscar","Toby","Kevin","Kevin","Alvin"]
friends2= friends.copy()
friends.sort()
lucky_numbers.sort()
friends.extend(lucky_numbers)
friends.extend("Creed")
friends.append("Creed")
friends.append(lucky_numbers)
friends.insert(1, 'Kelly')
friends.remove("Toby")
friends.pop()
print(friends.count("Kevin"))
print(friends.index("Oscar"))
print(friends)
print(friends2)