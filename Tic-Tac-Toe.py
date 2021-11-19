# Python project for tic-tac-toe
import random
import time

#function to print the current board, it will receive the list as the argument and will present the list in the form of our usual playing board for tic tac toe
def print_board(l):
    print("Current board:")
    print("///////////////////////////////")
    print("  ",l[0][0],"   |   ",l[0][1],"   |   ",l[0][2],"  ")
    print("______________________________")
    print("  ",l[1][0],"   |   ",l[1][1],"   |   ",l[1][2],"  ")
    print("______________________________")
    print("  ",l[2][0],"   |   ",l[2][1],"   |   ",l[2][2],"  ")
    print("///////////////////////////////")

#function to print the welcome message
def print_welcome_message():
    print("Welcome to the tic-tac-toe game!")

#function to check if the board is full or not, it will help in determining when to end the game if no one wins
def check_full(l):
    flag=0
    for x in range(3):
        for y in range(3):
            if l[x][y]==" ":
                flag=1
                break
        if flag==1:
            break
    return flag

#function to reset the board for the new game
def reset_board(l):
    for x in range(3):
        for y in range(3):
            l[x][y]=" "

#function to update the score of each cell, which will later decide the move of the computer
def update_score(s,l):
    #resetting the current score cell chart s to 0
    for x in range(3):
        for y in range(3):
            s[x][y]=0
    #updating the score of each cell of the list s, the score is calculated in the following manner:
    #the number of X are calculated which are present in the row and coulum and diagoinal(if applicable for the cell) in which the cell under observation lies
    #those cells are not updated which are already filled
    for x in range(0,3):
        for y in range(0,3):
            if l[x][y] == " ":
                for i in range(0, 3):
                    if l[x][i] == "X":
                        s[x][y]=s[x][y]+1
                for i in range(0, 3):
                    if l[i][y] == "X":
                        s[x][y]=s[x][y]+1
                if (x==0 and y==0) or (x==2 and y==2):
                    for i in range(0, 3):
                        if l[i][i] == "X":
                            s[x][y]=s[x][y]+1
                if (x==0 and y==2) or (x==2 and y==0):
                    for i in range(0, 3):
                        if l[i][2-i] == "X":
                            s[x][y]=s[x][y]+1

#function where the computer calculates its score for each cell, this function will take care that the computer could also focus on its winning chances
#it updates its score matrix just like the update_score function, whith the difference that O is replaced with X
def update_my_score(s,l):
    for x in range(3):
        for y in range(3):
            s[x][y]=0
    for x in range(0,3):
        for y in range(0,3):
            if l[x][y] == " ":
                for i in range(0, 3):
                    if l[x][i] == "O":
                        s[x][y]=s[x][y]+1
                for i in range(0, 3):
                    if l[i][y] == "O":
                        s[x][y]=s[x][y]+1
                if (x==0 and y==0) or (x==2 and y==2):
                    for i in range(0, 3):
                        if l[i][i] == "O":
                            s[x][y]=s[x][y]+1
                if (x==0 and y==2) or (x==2 and y==0):
                    for i in range(0, 3):
                        if l[i][2-i] == "O":
                            s[x][y]=s[x][y]+1

#function to analyse the urrent board situation to check if anyone won or not
#returns 0 if we won
#returns 1 if the comuter wins
#returns -1 otherwise
def check_win(l):
    #checking for horizontal matches
    for i in range(3):
        if l[i][0] == "X" and l[i][1] == "X" and l[i][2] == "X":
            return 0
        if l[i][0] == "O" and l[i][1] == "0" and l[i][2] == "O":
            return 1
        #checking for vertical matchings
        if l[0][i] == "O" and l[1][i] == "0" and l[2][i] == "O":
            return 1
        if l[0][i] == "X" and l[1][i] == "X" and l[2][i] == "X":
            return 0
    #checking for diagonal matches
    if l[0][0] == "X" and l[1][1] == "X" and l[2][2] == "X":
        return 0
    if l[0][2] == "X" and l[1][1] == "X" and l[2][0] == "X":
        return 0
    if l[0][0] == "O" and l[1][1] == "O" and l[2][2] == "O":
        return 1
    if l[0][2] == "O" and l[1][1] == "O" and l[2][0] == "O":
        return 1
    else:
    #returning -1 if noting was matched
        return -1

################################################################################################
#main driver code
print_welcome_message()
#asking the user if it wants to play the game or not
print("Do you want to play the game?")
#receiving input
response=input()
flag1=1
#processing the output of yes
if response=="yes":
    while flag1!=0:
        # giving playing directions
        print("Welcome to the game!")
        print("Let me decide who will play first...")
        time.sleep(1)
        #deciding a random number which will decide who will play first
        n = random.randint(1, 10);
        # initializing the lists
        # list to keep track of moves
        l = []
        l.append([" ", " ", " "])
        l.append([" ", " ", " "])
        l.append([" ", " ", " "])
        # making the score list to decide the move for computer
        score = []
        score.append([0, 0, 0])
        score.append([0, 0, 0])
        score.append([0, 0, 0])
        # to keep track of the score for each cell for the computer
        my_score = []
        my_score.append([0, 0, 0])
        my_score.append([0, 0, 0])
        my_score.append([0, 0, 0])
        # counter to decide if it was the forst move or not
        count = 0
        # keep asking for input till the board is full
        while (check_full(l)):
            #if n is even then the computer will play the first move
            if n % 2 == 0:
                if count == 0:
                    print("I will play first :)")
                    print("You take 'X' and i will take 'O'")
                    print("Let's start with the game without any further delay :)")
                    l[1][1] = "O"
                    count = count + 1
                    print_board(l)
                    continue
            else:
                if count==0:
                    print("Your turn first :)")
                    print("You take 'X' and i will take 'O'")
                    print("Let's start with the game without any further delay :)")
            # asking the user the location of the place where it wants to put a X the address of each cell is shown in the diagram below for your convenience:
            # ///////////////////////////////
            #    (0,0)    |    (0,1)     |    (0,2)
            # _______________________________________
            #    (1,0)    |    (1,1)    |     (1,2)
            # _______________________________________
            #    (2,0)    |    (2,1)     |   (2,2)
            # ///////////////////////////////
            # if you want to mark (x,y), type the input as: x then press enter, then give y and press enter
            print("Type the location coordinate where you want to mark cross X")
            x = int(input())
            y = int(input())
            # checking if the cell is already filled or not
            if l[x][y] == " ":
                # if not then updating the cell
                l[x][y] = "X"
                count = count + 1
                time.sleep(1)
                # printing the board to show the user the board after it has given its move
                print_board(l)
            else:
                # otherwise printing the error message and pronting the current board to show the user
                print("Cell already filled!")
                print_board(l)
                continue
            #checking winning condition in case we win in the last move
            if check_win(l) == 0:
                print_board(l)
                print("YOU WON!")
                print("%%%%%%%%%%%%%%%%%%%%%%   THANK YOU FOR PLAYING   %%%%%%%%%%%%%%%%%%%%%%%%")
                print("Do you want to play again?")
                res = input();
                if res == "yes":
                    reset_board(l)
                    continue
                else:
                    flag1 = 0
                    break
            # after the first move, checking if middle cell is filled or not, if empty, then we will mark O at the center
            if count == 1:
                if l[1][1] == " ":
                    print("Ummm.... let me think...")
                    time.sleep(3)
                    print("How about this?")
                    l[1][1] = "O"
                    update_score(score, l)
                    update_my_score(my_score, l)
                    print_board(l)
                    continue

            print("Ummm.... let me think...")
            time.sleep(3)
            print("How about this?")
            #deciding the place where the computer must move
            update_score(score, l)
            update_my_score(my_score, l)
            max_x = 0
            max_y = 0
            max = -1
            #the cell with the heighest score must be filled by the computer on its move
            #finding the cell with max X score
            for x in range(3):
                for y in range(3):
                    if l[x][y] == " ":
                        if max <= score[x][y]:
                            max = score[x][y]
                            max_x = x
                            max_y = y
            # print("max is:", max)
            # print("coordinates are: ", max_x, max_y)
            my_max_x = 0
            my_max_y = 0
            my_max = -1
            #finding the cell with max O score
            for x in range(3):
                for y in range(3):
                    if l[x][y] == " ":
                        if my_max <= my_score[x][y]:
                            my_max = my_score[x][y]
                            my_max_x = x
                            my_max_y = y
            # print("my_max is:", my_max)
            # print("coordinates are: ", my_max_x, my_max_y)
            #choosing the cell with max score among them and then making the move on that cell itself
            if my_max >= max:
                max = my_max
                max_x = my_max_x
                max_y = my_max_y
            #placing the O at the desired location if the board is not full
            if max >= 0:
                l[max_x][max_y] = "O"

                #checking if there is a winning condition
                if check_win(l) == 0:
                    print_board(l)
                    print("YOU WON!")
                    count=0
                    print("%%%%%%%%%%%%%%%%%%%%%%   THANK YOU FOR PLAYING   %%%%%%%%%%%%%%%%%%%%%%%%")
                    print("Do you want to play again?")
                    res = input()
                    if res == "yes":
                        reset_board(l)
                        continue
                    else:
                        flag1=0
                        break
                # checking if there is a winning condition
                elif check_win(l) == 1:
                    print_board(l)
                    print("I WON!")
                    count=0
                    print("%%%%%%%%%%%%%%%%%%%%%%   THANK YOU FOR PLAYING   %%%%%%%%%%%%%%%%%%%%%%%%")
                    print("Do you want to play again?")
                    res = input()
                    if res == "yes":
                        reset_board(l)
                        continue
                    else:
                        flag1=0
                        break
                print_board(l)
            #printing game over if the board is full
            else:
                print("Game Over!")
                count=0
                print("%%%%%%%%%%%%%%%%%%%%%%   THANK YOU FOR PLAYING   %%%%%%%%%%%%%%%%%%%%%%%%")
                print("Do you want to play again?")
                res = input()
                if res == "yes":
                    reset_board(l)
                    continue
                else:
                    flag1=0
                    break
else:
    print("Why did you run the application then :(")