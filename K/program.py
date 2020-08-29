a=0
b=4

for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1):
            print("*",end="")
        elif (row==a and col==b):
            print("*",end="")
            a=a+1
            b=b-1
        else:
            print(end=" ")
    print()
