# File chaos.py
# A simple program Illustrating chaotic behaviour


def main():
    print("This prgram llustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a another number here between 0 and 1: "))
    n = eval(input("How many times would you like your code to be executed?"))
    for i in range(n):
        i += 1
        x =  3.9 * x * (1 - x)
        y = 4.0 * y * (1 - y)
        print(x, y)
main()
