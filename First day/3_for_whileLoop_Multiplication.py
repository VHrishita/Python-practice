table = int(input("Enter table name:"))
limit = int(input("Enter the limit:"))
for i in range(1, limit +1):
    print(f"{table}x{i} = {table * i}")