a=0;
b=3;
for row in range(4):
    for col in range(7):
        if col==0 or col==6 or (col==5 and row==2) or (col==4 and row==1):
            print("*",end="")
        elif row==a and  col==b:
            print("*",end="")
            a=a+1
            b=b-1
        else:
            print(end=" ")
    print()
