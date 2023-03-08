
field = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

'''
     A   B   C 
1      |   |
    ---|---|---
2      |   |   
    ---|---|---
3      |   |   
'''
def show_field():
    print()
    print("   A   B   C ")
    print("1  " + field[0][0] + " | " + field[0][1] + " | " + field[0][2] + " ")
    print("  ---|---|---")
    print("2  " + field[1][0] + " | " + field[1][1] + " | " + field[1][2] + " ")
    print("  ---|---|---")
    print("3  " + field[2][0] + " | " + field[2][1] + " | " + field[2][2] + " ")
    print()

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
        show_field()
        print("Player" + str(player) + "'s turn.")
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
                
                row = int(place[1]) - 1

                if not field[row][col] == " ":
                    print()
                    print("*******************")
                    print("Not an empty space!")     
                else:
                    valid = True
    field[row][col] = symbol
    turn = not turn

    def comp_check():
        completed = True
        print()
        print("Player " + str(player + 1) + " won the game!")

    if field[0][0] == field[0][1] and field[0][1] == field[0][2] and not field[0][0] == " ":
        comp_check()
    elif field[1][0] == field[1][1] and field[1][1] == field[1][2] and not field[1][0] == " ":
        comp_check()
    elif field[2][0] == field[2][1] and field[2][1] == field[2][2] and not field[2][0] == " ":
        comp_check()
    elif field[0][0] == field[1][0] and field[1][0] == field[2][0] and not field[0][0] == " ":
        comp_check()
    elif field[0][1] == field[1][1] and field[1][1] == field[2][1] and not field[0][1] == " ":
        comp_check()
    elif field[0][2] == field[1][2] and field[1][2] == field[2][2] and not field[0][2] == " ":
        comp_check()
    elif field[0][0] == field[1][1] and field[1][1] == field[2][2] and not field[0][0] == " ":
        comp_check()
    elif field[0][2] == field[1][1] and field[1][1] == field[2][0] and not field[0][2] == " ":
        comp_check()
    
    draw = True
    for i in range(3):
        for j in range(3):
            if field[i][j] == " ":
                draw = False
                break
        else:
            continue
        break

    if draw == True:
        print()
        print("******")
        print("Draw!!")
        completed = True