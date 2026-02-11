##* ** ***
for i in range(1,4):
    print('*' *i)

##----------------
##1 12 123
for i in range(1,4):
    for j in range(1, i+1):
        print(j, end="")
    print()
##-----------------
##***  **  ***
for i in range(3):
    for j in range(3):
        if i==1 and j==1:
            print(" ", end="")
        else:
            print("*",end="")
    print()