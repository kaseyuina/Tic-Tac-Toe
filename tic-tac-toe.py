

field = [0,0,0][0,0,0]

'''
     A   B   C 
1      |   |
    ---|---|---
2      |   |   
    ---|---|---
3      |   |   
'''

turn = True
completed = False

while completed == False:
    if turn == True:
        player = 1
        symbol = "O"
    else:
        player = 2
        symbol = "X"
    
    valid = False
    while valid == False:
        print("Player" + player + "'s turn.")
        place = input("Please select an empty space. (e.g. A1): ")
        if not len(place) == 2:
            print("Invalid space.")
        else:
            if not place[0] == "A" and not place[0] == "B" and not place[0] == "C":
                print("Invalid space.")
            elif not place[1] == "1" and not place[1] == "2" and not place[1] == "3":
                print("Invalid space.")
            else:
                if place[0] == "A":
                    col = 0
                elif place[0] == "B":
                    col = 1
                elif place[0] == "C":
                    col = 2
                
                row = int(place[1] - 1)

                if not field[col][row] == 0:    
                    print("Not an empty space.")     
                else:
                    valid = True
    field[col][row] = symbol
    
                

