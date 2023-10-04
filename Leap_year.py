year = int(input("Adj meg egy évszámot: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Szökőév")
        else:
            print("Nem szökőév")    
    else:
        print("Szökőév")    
else:
    print("Nem szökőév")