import random

# Funkcja wyświetlająca planszę gry
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board, player):
    # Sprawdzenie wierszy
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def bot_move(board):
    for player in ["O", "X"]:
        for row, col in get_available_moves(board):
            board[row][col] = player
            if check_winner(board, player):
                board[row][col] = " "
                return row, col
            board[row][col] = " "
    
    if (1, 1) in get_available_moves(board):
        return 1, 1
    
    for move in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if move in get_available_moves(board):
            return move
    
    return random.choice(get_available_moves(board))

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        player_turn = True
        
        while True:
            print_board(board)
            
            if player_turn:
                try:
                    row, col = map(int, input("Podaj ruch (wiersz i kolumna, np. 1 1): ").split())
                    if board[row][col] != " ":
                        print("To miejsce jest już zajęte!")
                        continue
                except (ValueError, IndexError):
                    print("Nieprawidłowe dane. Podaj dwie liczby od 0 do 2.")
                    continue
            else:
                row, col = bot_move(board)
                print(f"Bot wybiera: {row} {col}")
                
            board[row][col] = "X" if player_turn else "O"
            
            if check_winner(board, "X" if player_turn else "O"):
                print_board(board)
                print("Wygrał", "gracz" if player_turn else "bot")
                break
            
            if not get_available_moves(board):
                print_board(board)
                print("Remis!")
                break
            
            player_turn = not player_turn
        
        if input("Chcesz zagrać ponownie? (tak/nie): ").lower() != "tak":
            break

if __name__ == "__main__":
    play_game()
