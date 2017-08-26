# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 19:33:06 2017

@author: hundred
"""

def print_board(board):
    for i in board:
        for j in i:
            if(j==1):
                print('X',end=" ")
            elif(j==2):
                print('O',end=" ")
            else:
                print('_',end=" ")
        print()

def check_win(board):
    for i in range(3):
        if(board[i] == ([1]*3)):
            return 1
        if(board[i] == ([2]*3)):
            return 2
        if(board[0][i] == board[1][i] and board[0][i] == board[2][i]):
            return board[0][i]
    if((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        return board[1][1]
    return 0
        

def validate_input(n,options):
    n = int(n)
    if(n in options):
        return n
    else:
        print("Invalid position to mark. Retry")
        n = input()
        n = validate_input(n,options)
        return n

def insert_mark(player, position, board):
    if(position>6):
        r = 0
    elif(position>3):
        r = 1
    else:
        r = 2
    
    c = (position % 3) -1 
    board[r][c] = player
    return board

def take_next_input(options):
    p = len(options)%2
    p = p + (not p) + (not p)
    print("Player ",p,"'s turn:")
    inp = input().strip()
    inp = validate_input(inp,options)
    return (inp,p)

def play(p1,p2):
    board = [[0,0,0],[0,0,0],[0,0,0]]
    opt = [1,2,3,4,5,6,7,8,9]
    while(opt!=[]):
        print_board(board)
        (pos, pl) = take_next_input(opt)
        board = insert_mark(pl,pos,board)
        opt.remove(pos)
        winner = check_win(board)
        if(winner):
            break

    print_board(board)
    if(winner==1):
        p1 += 1
        print("player 1 wins")
    elif(winner==2):
        p2 += 1
        print("player 2 wins")
    else:
        print("This match was a draw")
    print("the score is ", p1, " v ", p2)
    return(p1,p2)
        
(p1,p2) = play(0,0)
k = input("Enter q to exit; any other key to play again")
while(k!="q"):
    (p1,p2) = play(p1,p2)
    k = input("Enter q to exit; any other key to play again")
