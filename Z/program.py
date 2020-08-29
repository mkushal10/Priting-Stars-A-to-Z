a=1
b=4
for row in range(0,6):
    for col in range(0,6):
        if row==0 or row==5:
            print("*",end="")
        elif row==a and col==b:
            a=a+1
            b=b-1
            print("*",end="")
        else:
            print(end=" ")
    print()
