bag1 = ["apple", "mango", "water", "sweet"]
bag2 = ["water", "apple", "chips", "mango"]

print(sorted(set(bag1 + bag2)))

bag1 = ["apple", "mango", "water", "sweet"]
bag2 = ["water", "apple", "chips", "mango"]

combined = bag1 + bag2
unique_items = set(combined)
result = sorted(unique_items)

print(result)
