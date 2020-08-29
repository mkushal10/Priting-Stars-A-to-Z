a=0;
b=4;
for row in range(5):
    for col in range(5):
        if row==a and col==b:
            print("*",end="")
            a=a=a+1
            b=b-1
        elif row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
