from random import randint
from time import sleep

def s():
    sleep(0.01 * randint(1, 100))


def get_number(prompt, min_num = 1, max_num = 1000):
    while True:
        try:
            x = input(prompt)
            if x == "quit":
                exit()
            else:
                x = int(x)
                if x > max_num or x < min_num:
                    raise ValueError
        except ValueError:
            prompt = f"The input is not an integer in the interval [{min_num},{max_num}]. Please enter again: "
        else:
            return x


print("""-------------------------Guess the number-------------------------
Now there is a random integer in the interval [1,1000], and you and I take turns guessing to see who gets it first.
At any time you want to quit, enter 'quit' (without quotation marks).
""")
s()
key = randint(1, 1000)

method = get_number("How would you like me to guess the number (1/2)?\n1. Guess randomly\n2. Binary search\n\nChoose: ", 1, 2)

ans = get_number("\nYou go first: ")
r = "You"

mi, ma = 1, 1000

while ans != key:
    s()
    if ans == key:
        r = "You"
        break
    elif ans < key:
        print("The number you guessed is too small.")
        if mi < ans + 1:
            mi = ans + 1
    else:
        print("The number you guessed is too big.")
        if ma > ans - 1:
            ma = ans - 1
    if method == 1:
        ans = randint(mi, ma)
    else:
        ans = (mi + ma) // 2
    s()
    print("\nNow it's my turn.")
    s()
    print(f"I guess {ans}.")
    s()
    if ans == key:
        r = "I"
        break
    elif ans < key:
        print("The number I guessed is too small.")
        mi = ans + 1
    else:
        print("The number I guessed is too big.")
        ma = ans - 1
    s()
    ans = get_number("\nYou again: ")
    
print(f"{r} win！\nThe answer is {key}.")
input()
