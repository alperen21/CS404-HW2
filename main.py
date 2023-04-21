from Board import Board

def main():
    board = Board()
    board.initialize("input.txt")
    board.solve()

if __name__ == "__main__":
    main()