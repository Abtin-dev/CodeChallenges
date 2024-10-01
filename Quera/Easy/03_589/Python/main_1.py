def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

def main():
    print(factorial(int(input())))

if __name__ == "__main__":
    main()
#Result 100/100
