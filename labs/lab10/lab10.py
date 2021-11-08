"""
Name: <Sydney Wertz>
<lab10>.py
"""

def build_board():
    base_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return base_list

def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])

def place_marker(board, player, placement):
    placement_index = placement - 1
    board[placement_index] = player

def legal_move(board, placement):
    if (board[placement] == "X" or board[placement] == "O") or (placement < 0 or placement > 8):
        return False
    else:
        return True

def win_game(board):
    win_con = [[0,1,2], [3, 4, 5,], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_con:
        counter_x = 0
        for spot in condition:
            if board[spot] == "X":
                counter_x += 1
            if counter_x == 3:
                return True

        counter_o = 0
        for spot in condition:
            if board[spot] == "O":
                counter_o += 1
            if counter_o == 3:
                return True

def game_over(board, turn_count):
    if (win_game(board) == True) or (turn_count >= 9): #turn count starts at 0
        return True
    else:
        return False

def play_game():
    board = build_board()
    display_board(board)
    print()
    turn_counter = 0

    while game_over(board, turn_counter) == False:
        if (turn_counter % 2) == 0:
            print("It is X's turn")
            placement = eval(input("Enter where you would like to place your mark: "))
            if legal_move(board, (placement - 1)) == True:
                place_marker(board, "X", placement)
                display_board(board)
                print()
                win_game(board)
                turn_counter += 1

                if win_game(board) == True:
                    game_over(board, turn_counter) == True
                    print("X wins")
                    break
                elif game_over(board, turn_counter) == True:
                    print("Tie")
                    break

            else:
                print("Please enter a valid move")

        if (turn_counter % 2) == 1:
            print("It is O's turn")
            placement = eval(input("Enter where you would like to place your mark: "))
            if legal_move(board, placement - 1) == True:
                place_marker(board, "O", placement)
                display_board(board)
                print()
                turn_counter += 1

                if win_game(board) == True:
                    game_over(board, turn_counter) == True
                    print("O wins")
                    break
                elif game_over(board, turn_counter) == True:
                    print("Tie")
                    break

            else:
                print("Please enter a valid move")

    print("Game Over")

def main():
    play_game()
    pass

main()
