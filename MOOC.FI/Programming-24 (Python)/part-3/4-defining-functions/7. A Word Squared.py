# Write your solution here
def squared(string, side_length):
    side = string * (side_length ** 2)
    length = side_length
    while length > 0:
        print(side[:side_length])
        side = side[side_length:]
        length -= 1
## Another way to solve it
#    row = ""
#    counter = 0
#    while counter < side_length ** 2:
#        # Every time side_length is achieved (Counter Not Zero AND factor of side_length)
#        if counter > 0 and counter % side_length == 0:
#            # print row and reset it
#            print(row)
#            row = ""
#        # Add next character to the row if side_length to be reached yet
#        row += string[counter % len(string)]
#        counter += 1
#    # print the remaining last row
#    print(row)

# Test
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
    print()
    squared("ayb", 6)