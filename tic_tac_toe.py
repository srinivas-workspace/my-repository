def print_board(b):
    print("\n  0   1   2")
    for i in range(3):
        print(i, end=" ")
        print(b[i][0], "|", b[i][1], "|", b[i][2])
        if i != 2:
            print("  ---------")


def take_input(b, symbol):
    while True:
        move = input(f"Player {symbol}, enter row and column: ")

        if len(move.split()) != 2:
            print("Enter two numbers only (example: 1 2)")
            continue

        r, c = move.split()

        if not (r.isdigit() and c.isdigit()):
            print("Only numbers allowed")
            continue

        r = int(r)
        c = int(c)

        if r < 0 or r > 2 or c < 0 or c > 2:
            print("Row and column must be between 0 and 2")
            continue

        if b[r][c] != ' ':
            print("That place is already filled")
            continue

        b[r][c] = symbol
        break


def winner_found(b, s):
    # rows
    for i in range(3):
        if b[i][0] == s and b[i][1] == s and b[i][2] == s:
            return True

    # columns
    for j in range(3):
        if b[0][j] == s and b[1][j] == s and b[2][j] == s:
            return True

    # diagonals
    if b[0][0] == s and b[1][1] == s and b[2][2] == s:
        return True

    if b[0][2] == s and b[1][1] == s and b[2][0] == s:
        return True

    return False


def start_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'
    turn_count = 0

    print("\nWelcome to Tic Tac Toe")
    print("Player X goes first")
    print("Enter row and column like: 0 1")

    while True:
        print_board(board)
        take_input(board, current)
        turn_count += 1

        if winner_found(board, current):
            print_board(board)
            print(f"\nPlayer {current} wins")
            break

        if turn_count == 9:
            print_board(board)
            print("\nGame Draw!")
            break

        if current == 'X':
            current = 'O'
        else:
            current = 'X'


while True:
    start_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
