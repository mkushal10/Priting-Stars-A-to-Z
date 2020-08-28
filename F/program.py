#row 7 needed
for row in range(7):
    #column 5 needed
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and (col>0)):
            print("*",end="")
        else:
            print(end=" ")
    print()
