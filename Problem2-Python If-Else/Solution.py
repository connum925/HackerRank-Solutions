if __name__ == '__main__':
    n = int(input().strip())
    # Check if the number is odd
    # If n%2 == 1, it means the remainder of dividing n by 2 is 1 (odd)
    if (n%2) == 1:
        print("Weird")
    else:
        # If the number is even (n%2 == 0)
        if 2<=n<=5:
            print("Not Weird")
        # If n is in the range from 6 to 20 (inclusive)
        elif 6<=n<=20:
            print("Weird")
        else:
            # If n is greater than 20 (and even)
            print("Not Weird")