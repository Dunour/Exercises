# Write your solution here
def chessboard(side_length):
    line = 0
    while side_length > line:
        row = ("01" * side_length) if line % 2 else ("10" * side_length)
        print(row[:side_length])
        line += 1            
## Another way to solve it
#    row = side_length
#    line = 0
#    while row > 0:
#        width = side_length
#        line += 1
#        counter = 1 if line % 2 else 0
#        while width > 0:
#            print(f"{1 if (counter % 2) else 0}", end="")
#            counter += 1
#            width -= 1
#        print()
#        row -= 1
    
# Testing the function
if __name__ == "__main__":
    chessboard(3)
    print()
    chessboard(4)
    print()
    chessboard(5)
    print()
    chessboard(6)
