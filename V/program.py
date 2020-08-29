a=0;
b=6;
for row in range(4):
    for col in range(7):
        if row==col or col==row:
            print("*",end="")
        elif row==a and col==b:
            print("*", end="")
            a=a+1
            b=b-1
        else:
            print(end=" ")
    print()
