##################################################
# Author: Kshitij Bhat
##################################################
print("Thank you for using Kshitij's Tic Tac Toe. The computer enters O. User gets the first chance!!!")

from random import seed
from random import randint
import time

tic_tac_mat = [["0", "0", "0"],["0","0","0"],["0","0","0"]]

def print_mat(tic_tac_mat):

    for row in tic_tac_mat:
        print ("-------------")
        print("|   |   |   |")
        print("|",end="")
        for col in row:
            if(col=="0"):
                print(" "+" "+" |", end="")
            else:
                print(" "+col+" |", end="")
        print("")
        print("|   |   |   |")
    print ("-------------")

def user_entry(tic_tac_mat):
    x_entry = input("select the row:")
    x_entry = int(x_entry)-1
    y_entry = input("select the column:")
    y_entry = int(y_entry)-1

    if(tic_tac_mat[x_entry][y_entry]=="0"):
        tic_tac_mat[x_entry][y_entry] = "X"
    else:
        print("The place is taken. Try again")
        tic_tac_mat = user_entry(tic_tac_mat)
    return tic_tac_mat


def comp_entry(tic_tac_mat):
    time.sleep(3)
    comp_x = randint(0,2)
    comp_y = randint(0,2)
    if tic_tac_mat[comp_x][comp_y] != "X" and tic_tac_mat[comp_x][comp_y] != "O":
        tic_tac_mat[comp_x][comp_y] = "O"
    else:
        tic_tac_mat = comp_entry(tic_tac_mat)
    return tic_tac_mat


def check_and_enter(tic_tac_mat,player):
    if(player == "user"):
        tic_tac_mat = user_entry(tic_tac_mat)
        print_mat(tic_tac_mat)
    else:
        # i,j = collect_O(tic_tac_mat)
        # if i!=-1 and j!=-1:
        #     tic_tac_mat = comp_entry(tic_tac_mat)
        #     print_mat(tic_tac_mat)
        # else:
        #     tic_tac_mat[i][j] = "O"
        tic_tac_mat = comp_entry(tic_tac_mat)
        print_mat(tic_tac_mat)
    return tic_tac_mat

def row_check(tic_tac_mat):
    for row in tic_tac_mat:
        if row == user_row:
            print("Hurray!! you win!!")
            return 1
        if row == comp_row:
            print("Computer wins!! Better luck next time!")
            return 1
    return 0

def col_check(tic_tac_mat):
    for col in range(3):
        col_list = [row[col] for row in tic_tac_mat]
        if col_list == user_row:
            print("Hurray!! you win!!")
            return 1
        if col_list == comp_row:
            print("Computer wins!! Better luck next time!")
            return 1
    return 0
def diagonal_check(tic_tac_mat):
    forward_diagonal_list = [tic_tac_mat[0][0], tic_tac_mat[1][1], tic_tac_mat[2][2]]
    backward_diagonal_list = [tic_tac_mat[0][2], tic_tac_mat[1][1], tic_tac_mat[2][0]]
    if forward_diagonal_list == user_row or backward_diagonal_list == user_row:
        print("Hurray!! you win!!")
        return 1
    if forward_diagonal_list == comp_row or backward_diagonal_list == comp_row:
        print("Computer wins!! Better luck next time!")
        return 1
    return 0

'''def collect_O(tic_tac_mat):
    for row in range(3):
        if tic_tac_mat[row].count("O") == 2:
            i,j = row, tic_tac_mat[row].index("0")
            return i,j
    for col in range(3):
        col_O = [tic_tac_mat[row][col] for row in range(3)]
        if col_O.count("O") == 2:
            i,j = col_O.index("0"), col
    forward_diagonal = {tic_tac_mat[0][0]:(0,0), tic_tac_mat[1][1]:(1,1), tic_tac_mat[2][2]:(2,2)}
    backward_diagonal = {tic_tac_mat[0][2]:(0,2), tic_tac_mat[1][1]:(1,1), tic_tac_mat[2][0]:(2,0)}
    vals = list(forward_diagonal.keys())
    print(vals, type(vals))
    if vals.count("O") == 2:
        i,j = forward_diagonal[forward_diagonal.keys().index("0")]
        return i,j
    vals = list(backward_diagonal.keys())
    if vals.count("O") == 2:
        i,j = forward_diagonal[forward_diagonal.keys().index("0")]
        return i,j
    return -1,-1 '''


user_row = ["X","X","X"]
comp_row = ["O","O","O"]
flag=0
print("The Tic tac Grid is: ")
print_mat(tic_tac_mat)
print("Player enters his X first. Computer will enter its O after the player")
print("Select the row number and column number to enter your X")
for i in range(1,10):
    if(i%2==1):
        tic_tac_mat = check_and_enter(tic_tac_mat,"user")
    else:
        print("Computer is placing its O")
        tic_tac_mat = check_and_enter(tic_tac_mat,"computer")
    if(i>=5):
        flag = row_check(tic_tac_mat)
        if flag:
            break
        flag = col_check(tic_tac_mat)
        if flag:
            break
        flag = diagonal_check(tic_tac_mat)
        if flag:
            break
    if(flag==1):
        break
