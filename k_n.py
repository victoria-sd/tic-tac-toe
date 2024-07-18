import requests
import bs4
import pytest



def draw_board(board):
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")

def takeinput_x(board):
    while True:
        val_x = input("Введите номер ячейки, куда хотите сделать ход: ")
        if val_x.isdigit():
            val_x = int(val_x)
            # if 0 < val_x < 10:
            #     val_x -= 1
            #     if isinstance(board[val_x], int):
            #         print('Верно')
            #     else:
            #         print('данная ячейка занята')
            # else:
            #     print('Убедитесь, что вы ввели число от 1 до 9')
            if val_x in board:
                val_x -= 1
                return val_x
            else:
                print("неверная ячейка")
        else:
            print('Убедитесь, что вы ввели число')

def check_win(board):
    comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))
    for a,b,c in comb:
        if board[a] == board[b] ==board[c]:
            return True
    return False




def tictac():
    board = list(range(1, 10))
    count = 0
    while True:
        draw_board(board)
        if count % 2 == 0:
            sym = 'X'
        else:
            sym = 'O'
        print(f'Ваш ход {sym}')
        val = takeinput_x(board)
        board[val] = sym
        count += 1
        if check_win(board):
            print(f'Победил игрок {sym}')
            draw_board(board)
            return
        if count == 9:
            print('Ничья')
            draw_board(board)
            return

tictac()