def main():
    x = float(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    # Can also use pow(n, 2)
    return n ** 2

main()
