#Declaring the field
field = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

'''
Field visual sample
     A   B   C 
1      |   |
    ---|---|---
2      |   |   
    ---|---|---
3      |   |   
'''
#A function to show field
def show_field():
    print()
    print("   A   B   C ")
    print("1  " + field[0][0] + " | " + field[0][1] + " | " + field[0][2] + " ")
    print("  ---|---|---")
    print("2  " + field[1][0] + " | " + field[1][1] + " | " + field[1][2] + " ")
    print("  ---|---|---")
    print("3  " + field[2][0] + " | " + field[2][1] + " | " + field[2][2] + " ")
    print()

#Showing invalid message
def show_invalid_message():
    print("Invalid input.")

turn = True
completed = False

#Loop until either player wins the game or draw
while completed == False:
    #Switching player and symbol each turn
    if turn == True:
        player = 1
        symbol = "O"
    else:
        player = 2
        symbol = "X"
    
    #Validating inputs
    #Allowed inputs are; A1, A2, A3, B1, B2, B3, C1, C2 or C3
    valid = False
    while valid == False:
        show_field()
        print("Player" + str(player) + "'s turn.")
        place = input("Please select an empty space. (e.g. A1): ")
        if not len(place) == 2:
            show_invalid_message()
        else:
            if not place[0] == "A" and not place[0] == "B" and not place[0] == "C":
                show_invalid_message()
            elif not place[1] == "1" and not place[1] == "2" and not place[1] == "3":
                show_invalid_message()
            else:
                #Storing column number
                if place[0] == "A":
                    col = 0
                elif place[0] == "B":
                    col = 1
                elif place[0] == "C":
                    col = 2
                
                #Storing row number
                row = int(place[1]) - 1

                #Checking if space is empty
                if not field[row][col] == " ":
                    print()
                    print("*******************")
                    print("Not an empty space!")     
                else:
                    valid = True
    #Storing symbol
    field[row][col] = symbol
    #Switching turn
    turn = not turn

    #Function to show win message
    def comp_check():
        show_field()
        print("***************************************")
        print("Player " + str(player) + " won the game!")
        print()
        return True

    #Checking if completed
    if field[0][0] == field[0][1] and field[0][1] == field[0][2] and not field[0][0] == " ":
        completed = comp_check()
    elif field[1][0] == field[1][1] and field[1][1] == field[1][2] and not field[1][0] == " ":
        completed = comp_check()
    elif field[2][0] == field[2][1] and field[2][1] == field[2][2] and not field[2][0] == " ":
        completed = comp_check()
    elif field[0][0] == field[1][0] and field[1][0] == field[2][0] and not field[0][0] == " ":
        completed = comp_check()
    elif field[0][1] == field[1][1] and field[1][1] == field[2][1] and not field[0][1] == " ":
        completed = comp_check()
    elif field[0][2] == field[1][2] and field[1][2] == field[2][2] and not field[0][2] == " ":
        completed = comp_check()
    elif field[0][0] == field[1][1] and field[1][1] == field[2][2] and not field[0][0] == " ":
        completed = comp_check()
    elif field[0][2] == field[1][1] and field[1][1] == field[2][0] and not field[0][2] == " ":
        completed = comp_check()
    
    #Checking if draw
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
        show_field()
        print("***********")
        print("Draw game!!")
        print()
        completed = True