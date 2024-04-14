x = int(input("Enter the value "))
match x:
    case 0:
        print("x is Zero")
    case 1:
        print("Coffee") 
    case 2:
        print("Milkshake")       
    case _ if x!=3:
        print(x,"Is not equal to 3")
    case _ if x!=4:
        print(x,"Is not equal to 4")
    case _ if x!=5:
        print(x,"Is not equal to 5")    