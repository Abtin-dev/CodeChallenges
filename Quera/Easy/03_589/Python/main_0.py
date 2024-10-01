def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        return "error"
    else:
        for i in range(1, number):
            number *= i
        return number

def main():
    print(factorial(int(input())))

if __name__ == "__main__":
    main()
#Result 100/100
