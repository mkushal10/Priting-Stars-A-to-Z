#row 7 needed, for loop, row and col are variable name
for row in range(7):
    #column 6 needed
    for col in range(6):
        if col==0 or (col==4 and (row!=1 and row!=2)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==3 and (col==3 or col==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
