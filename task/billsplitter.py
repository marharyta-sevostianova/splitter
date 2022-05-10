new = {}
print("Enter the number of friends joining (including you): ")
try:
    n = int(input())
except (ValueError, NameError):
    print("No one is joining for the party")

if n <= 0:
    print("No one is joining for the party")

else:
    print("Enter the name of every friend (including you), each on a new line: ")
    for i in range(n):
        a = input()
        another_dictionary = {a: 0}
        new.update(another_dictionary)

if n <= 0:
    pass
else:
    print('Enter the total bill value:')
    b = float(input())
import random

if n <= 0:
    pass
else:
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    l = input()
    if l == 'Yes':
        def pick_random_key(d: new):
            keys = list(d.keys())
            random_key = random.choice(keys)
            return random_key


        randra = pick_random_key(new)
        print((randra), 'is the lucky one!')
        try:
            if b / (n - 1) % 2 == 0:
                for i in new.keys():
                    new[i] = (int(b)) / (int(n - 1))
            else:
                for i in new.keys():
                    new[i] = round((float(b)) / (float(n - 1)), 2)
        except (ZeroDivisionError):
            n = 0
        anothe_dictionary = {randra: 0}
        new.update(anothe_dictionary)
        print(new)
    elif l == 'No':
        print('No one is going to be lucky')
        try:
            if b / (n) % 2 == 0:
                for i in new.keys():
                    new[i] = (int(b)) / (int(n))
            else:
                for i in new.keys():
                    new[i] = round((float(b)) / (float(n)), 2)
        except (ZeroDivisionError):
            n = 0
        print(new)
