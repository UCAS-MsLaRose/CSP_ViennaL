#Tic Tac Toe - Arsh, Nathaly, Isaac, Juan

#Board - Group
board1 = ["1", "2", "3"]
board2 = ["4", "5", "6"]
board3 = ["7", "8", "9"]
print("", board1,"\n", board2,"\n", board3)

#Function to ask the player what slot they want to choose
def playing(player):
     return(int(input(f"{player} turn. Choose a slot 1-9: ")))
#Function to inform the player the slot has already been taken
def slot(number):
     print(f"{number} has already been taken! Try again.")

#Player 1 input - Arsh
#Whole code is a loop
while True:
    #Smaller loop for each input
    while True:
        X = playing("X's")
        if X == 1 and board1[0] == "1": #Conditionals to check where to put the input on the board
            board1[0] = "X"
            break
        elif X == 2 and board1[1] == "2":
            board1[1] = "X"
            break
        elif X == 3 and board1[2] == "3":
            board1[2] = "X"
            break
        elif X == 4 and board2[0] == "4":
            board2[0] = "X"
            break
        elif X == 5 and board2[1] == "5":
            board2[1] = "X"
            break
        elif X == 6 and board2[2] == "6":
            board2[2] = "X"
            break
        elif X == 7 and board3[0] == "7":
            board3[0] = "X"
            break
        elif X == 8 and board3[1] == "8":
            board3[1] = "X"
            break
        elif X == 9 and board3[2] == "9":
            board3[2] = "X"
            break
        else:
            print("Invalid input, try again.")
    print("", board1, "\n", board2, "\n", board3)

    # Player 2 input - Nathaly
    while True:
        O = playing("O's")
        if O < 1 or O > 9:
            print("Invalid input, try again.")
            continue
        elif O == 1 and board1[0] == "1":
            board1[0] = "O"
            break
        elif O == 2 and board1[1] == "2":
            board1[1] = "O"
            break
        elif O == 3 and board1[2] == "3":
            board1[2] = "O"
            break
        elif O == 4 and board2[0] == "4":
            board2[0] = "O"
            break
        elif O == 5 and board2[1] == "5":
            board2[1] = "O"
            break
        elif O == 6 and board2[2] == "6":
            board2[2] = "O"
            break
        elif O == 7 and board3[0] == "7":
            board3[0] = "O"
            break
        elif O == 8 and board3[1] == "8":
            board3[1] = "O"
            break
        elif O == 9 and board3[2] == "9":
            board3[2] = "O"
            break
        else:
            slot(X)
            continue
    print("", board1, "\n", board2, "\n", board3)

    # Keep Going - Isaac
    while True:
        X = playing("X's")
        if X < 1 or X > 9:
            print("Invalid input, try again.")
            continue
        elif X == 1 and board1[0] == "1":
            board1[0] = "X"
            break
        elif X == 2 and board1[1] == "2":
            board1[1] = "X"
            break
        elif X == 3 and board1[2] == "3":
            board1[2] = "X"
            break
        elif X == 4 and board2[0] == "4":
            board2[0] = "X"
            break
        elif X == 5 and board2[1] == "5":
            board2[1] = "X"
            break
        elif X == 6 and board2[2] == "6":
            board2[2] = "X"
            break
        elif X == 7 and board3[0] == "7":
            board3[0] = "X"
            break
        elif X == 8 and board3[1] == "8":
            board3[1] = "X"
            break
        elif X == 9 and board3[2] == "9":
            board3[2] = "X"
            break
        else:
            slot(X)
            print("You cannot input that, try again")
    print("", board1, "\n", board2, "\n", board3)

    while True:
        O = playing("O's")
        if O < 1 or O > 9:
            print("Invalid input, try again.")
            continue
        elif O == 1 and board1[0] == "1":
            board1[0] = "O"
            break
        elif O == 2 and board1[1] == "2":
            board1[1] = "O"
            break
        elif O == 3 and board1[2] == "3":
            board1[2] = "O"
            break
        elif O == 4 and board2[0] == "4":
            board2[0] = "O"
            break
        elif O == 5 and board2[1] == "5":
            board2[1] = "O"
            break
        elif O == 6 and board2[2] == "6":
            board2[2] = "O"
            break
        elif O == 7 and board3[0] == "7":
            board3[0] = "O"
            break
        elif O == 8 and board3[1] == "8":
            board3[1] = "O"
            break
        elif O == 9 and board3[2] == "9":
            board3[2] = "O"
            break
        else:
            slot(X)
            continue
    print("", board1, "\n", board2, "\n", board3)

    while True:
        X = playing("X's")
        if X < 1 or X > 9:
            print("Invalid input, try again.")
            continue
        elif X == 1 and board1[0] == "1":
            board1[0] = "X"
            break
        elif X == 2 and board1[1] == "2":
            board1[1] = "X"
            break
        elif X == 3 and board1[2] == "3":
            board1[2] = "X"
            break
        elif X == 4 and board2[0] == "4":
            board2[0] = "X"
            break
        elif X == 5 and board2[1] == "5":
            board2[1] = "X"
            break
        elif X == 6 and board2[2] == "6":
            board2[2] = "X"
            break
        elif X == 7 and board3[0] == "7":
            board3[0] = "X"
            break
        elif X == 8 and board3[1] == "8":
            board3[1] = "X"
            break
        elif X == 9 and board3[2] == "9":
            board3[2] = "X"
            break
        else:
            slot(X)
            print("You cannot input that, try again")
    print("", board1, "\n", board2, "\n", board3)
    
    #Check who wins - Juan
    #Not in a loop so it can end the whole game once someone wins
    if board1 == ["X", "X", "X"] or board2 == ["X", "X", "X"] or board3 == ["X", "X", "X"]:
        print("X Wins!")
        break
    elif board1[0] == board2[1] == board3[2] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[1] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[0] == board2[0] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[1] == board2[1] == board3[1] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[2] == board3[2] == "X":
        print("X Wins!")
        break

    while True:
        O = playing("O's")
        if O < 1 or O > 9:
            print("Invalid input, try again.")
            continue
        elif O == 1 and board1[0] == "1":
            board1[0] = "O"
            break
        elif O == 2 and board1[1] == "2":
            board1[1] = "O"
            break
        elif O == 3 and board1[2] == "3":
            board1[2] = "O"
            break
        elif O == 4 and board2[0] == "4":
            board2[0] = "O"
            break
        elif O == 5 and board2[1] == "5":
            board2[1] = "O"
            break
        elif O == 6 and board2[2] == "6":
            board2[2] = "O"
            break
        elif O == 7 and board3[0] == "7":
            board3[0] = "O"
            break
        elif O == 8 and board3[1] == "8":
            board3[1] = "O"
            break
        elif O == 9 and board3[2] == "9":
            board3[2] = "O"
            break
        else:
            slot(X)
            continue
    print("", board1, "\n", board2, "\n", board3)

    if board1 == ["O", "O", "O"] or board2 == ["O", "O", "O"] or board3 == ["O", "O", "O"]:
        print("O Wins!")
        break
    elif board1[0] == board2[1] == board3[2] == "O":
        print("O Wins!")
        break
    elif board1[2] == board2[1] == board3[0] == "O":
        print("O Wins!")
        break
    elif board1[0] == board2[0] == board3[0] == "O":
        print("O Wins!")
        break
    elif board1[1] == board2[1] == board3[1] == "O":
        print("O Wins!")
        break
    elif board1[2] == board2[2] == board3[2] == "O":
        print("O Wins!")
        break

    while True:
        X = playing("X's")
        if X < 1 or X > 9:
            print("Invalid input, try again.")
            continue
        elif X == 1 and board1[0] == "1":
            board1[0] = "X"
            break
        elif X == 2 and board1[1] == "2":
            board1[1] = "X"
            break
        elif X == 3 and board1[2] == "3":
            board1[2] = "X"
            break
        elif X == 4 and board2[0] == "4":
            board2[0] = "X"
            break
        elif X == 5 and board2[1] == "5":
            board2[1] = "X"
            break
        elif X == 6 and board2[2] == "6":
            board2[2] = "X"
            break
        elif X == 7 and board3[0] == "7":
            board3[0] = "X"
            break
        elif X == 8 and board3[1] == "8":
            board3[1] = "X"
            break
        elif X == 9 and board3[2] == "9":
            board3[2] = "X"
            break
        else:
            slot(X)
            print("You cannot input that, try again")
    print("", board1, "\n", board2, "\n", board3)

    if board1 == ["X", "X", "X"] or board2 == ["X", "X", "X"] or board3 == ["X", "X", "X"]:
        print("X Wins!")
        break
    elif board1[0] == board2[1] == board3[2] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[1] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[0] == board2[0] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[1] == board2[1] == board3[1] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[2] == board3[2] == "X":
        print("X Wins!")
        break

    while True:
        O = playing("O's")
        if O < 1 or O > 9:
            print("Invalid input, try again.")
            continue
        elif O == 1 and board1[0] == "1":
            board1[0] = "O"
            break
        elif O == 2 and board1[1] == "2":
            board1[1] = "O"
            break
        elif O == 3 and board1[2] == "3":
            board1[2] = "O"
            break
        elif O == 4 and board2[0] == "4":
            board2[0] = "O"
            break
        elif O == 5 and board2[1] == "5":
            board2[1] = "O"
            break
        elif O == 6 and board2[2] == "6":
            board2[2] = "O"
            break
        elif O == 7 and board3[0] == "7":
            board3[0] = "O"
            break
        elif O == 8 and board3[1] == "8":
            board3[1] = "O"
            break
        elif O == 9 and board3[2] == "9":
            board3[2] = "O"
            break
        else:
            slot(X)
            continue
    print("", board1, "\n", board2, "\n", board3)

    if board1 == ["O", "O", "O"] or board2 == ["O", "O", "O"] or board3 == ["O", "O", "O"]:
        print("O Wins!")
        break
    elif board1[0] == board2[1] == board3[2] == "O":
        print("O Wins!")
        break
    elif board1[2] == board2[1] == board3[0] == "O":
        print("O Wins!")
        break
    elif board1[0] == board2[0] == board3[0] == "O":
        print("O Wins!")
        break
    elif board1[1] == board2[1] == board3[1] == "O":
        print("O Wins!")
        break
    elif board1[2] == board2[2] == board3[2] == "O":
        print("O Wins!")
        break

    while True:
        X = playing("X's")
        if X < 1 or X > 9:
            print("Invalid input, try again.")
            continue
        elif X == 1 and board1[0] == "1":
            board1[0] = "X"
            break
        elif X == 2 and board1[1] == "2":
            board1[1] = "X"
            break
        elif X == 3 and board1[2] == "3":
            board1[2] = "X"
            break
        elif X == 4 and board2[0] == "4":
            board2[0] = "X"
            break
        elif X == 5 and board2[1] == "5":
            board2[1] = "X"
            break
        elif X == 6 and board2[2] == "6":
            board2[2] = "X"
            break
        elif X == 7 and board3[0] == "7":
            board3[0] = "X"
            break
        elif X == 8 and board3[1] == "8":
            board3[1] = "X"
            break
        elif X == 9 and board3[2] == "9":
            board3[2] = "X"
            break
        else:
            slot(X)
            print("You cannot input that, try again")
    print("", board1, "\n", board2, "\n", board3)

    if board1 == ["X", "X", "X"] or board2 == ["X", "X", "X"] or board3 == ["X", "X", "X"]:
        print("X Wins!")
        break
    elif board1[0] == board2[1] == board3[2] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[1] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[0] == board2[0] == board3[0] == "X":
        print("X Wins!")
        break
    elif board1[1] == board2[1] == board3[1] == "X":
        print("X Wins!")
        break
    elif board1[2] == board2[2] == board3[2] == "X":
        print("X Wins!")
        break
    else:
        print("Tied!") #Ties if no other conditions are met as this is the last round
        break