#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:13:55 2019

@author: mac
"""

def display_board(board):
    num1 = board[1]
    num2 = board[2]
    num3 = board[3]
    num4 = board[4]
    num5 = board[5]
    num6 = board[6]
    num7 = board[7]
    num8 = board[8]
    num9 = board[9]
    
    print('   |   |   ')
    print(f' {num1} | {num2} | {num3}')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {num4} | {num5} | {num6}')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {num7} | {num8} | {num9}')
    print('   |   |   ')
    
def player_input():
    player_1 = input("Player 1 - Please pick a marker X or O:")
    player_1 = player_1.upper()
    while player_1 != 'X' and player_1 != 'O':
        print("Wrong selection.")
        player_1 = input("Player 1 - Please pick a marker X or O:")
        player_1 = player_1.upper()
        
    return player_1
        
def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):
    if (board[1] == mark) and (board[2] == mark) and (board[3] == mark):
        return True
    elif (board[4] == mark) and (board[5] == mark) and (board[6] == mark):
        return True
    elif (board[7] == mark) and (board[8] == mark) and (board[9] == mark):
        return True
    elif (board[1] == mark) and (board[5] == mark) and (board[9] == mark):
        return True
    elif (board[7] == mark) and (board[5] == mark) and (board[3] == mark):
        return True
    elif (board[1] == mark) and (board[4] == mark) and (board[7] == mark):
        return True
    elif (board[2] == mark) and (board[5] == mark) and (board[8] == mark):
        return True
    elif (board[3] == mark) and (board[6] == mark) and (board[9] == mark):
        return True
    else:
        return False
    

def choose_first():
    import random
    first_player = random.randint(1, 2)
    print(f'Player_{first_player} goes first')
    return first_player

def space_check(board, position):
    return (board[position] == 'X') or (board[position] == 'O')

def full_board_check(board):
    board_chck = list()
    for y in list(range(1,10,1)):
        if board[y] == 'X' or board[y] == 'O':
            board_chck.append(board[y])
    return len(board_chck) == 9  

def player_choice(board):
    position = int(input("Select a position between (1-9):"))
    
    while (board[position] == 'X') or (board[position] == 'O'):
        position = int(input("Select a position between (1-9) previous selection has already been selected:"))
        
    return position
        
def play():
    decision = input("Ready to play? (Yes or No):")
    decision = decision.upper()
    while decision != 'YES' and decision != 'NO':
        print("Wrong selection.")
        decision = input("Ready to play? (Yes or No):")
        decision = decision.upper()
        
    return decision == 'YES'

def replay():
    decision = input("Want to play again? (Yes or No):")
    decision = decision.upper()
    while decision != 'YES' and decision != 'NO':
        print("Wrong selection.")
        decision = input("Want to play again? (Yes or No):")
        decision = decision.upper()
        
    return decision == 'YES'

while True:        
    print('Welcome to Tic Tac Toe!')
    marker1 = player_input()
    if marker1 == 'X':
        marker2 = 'O'
        
    else:
        marker2 = 'X'
    
    player_turn = choose_first()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    decision = play()
         
    while decision:
        #Player 1 Turn
        if player_turn == 1:
            display_board(board)
            position = player_choice(board)
            place_marker(board, marker1, position)
            player_turn = 2
        
        #Player 2 Turn
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, marker2, position)
            player_turn = 1
        
        #Checking for Winner
        if win_check(board, marker1):
            display_board(board)
            print("Player_1 WINS!")
            break
            
        elif win_check(board, marker2):
            display_board(board)
            print("Player_2 WINS!")
            break
        
        elif full_board_check(board):
            display_board(board)
            print("It's a DRAW!")
            break
        
    if not replay():
        break