# Write your solution here
def hash_square(side_length):
# Another solution, but it prints a newline after printing the text.
#    side = "#" * side_length + "\n"
#    print(f"{side * side_length}")
    length = side_length
    while length > 0:
        print("#" * side_length)
        length -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)