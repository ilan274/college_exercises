# I made this exercise without any try / except, so, please insert the correct values (integers or strings)

def older(x,y):
    if x[2] == y[2]:
        if x[1] == y[1]:
            if x[0] == y[0]:
                print(f"{x[-1]} and {y[-1]} were born in the same date.")
            elif x[0] > y[0]:
                print(f"{x[-1]} is younger than {y[-1]}")
            else:
                print(f"{y[-1]} is younger than {x[-1]}")
        elif x[1] > y[1]:
            print(f"{x[-1]} is younger than {y[-1]}")
        else:
            print(f"{y[-1]} is younger than {x[-1]}")
    elif x[2] > y[2]:
        print(f"{x[-1]} is younger than {y[-1]}")
    else:
        print(f"{y[-1]} is younger than {x[-1]}")


date1 = []
date2 = []
order = ["day","month","year"]

name1 = input("Type your name: ")
for i in range(3):
    date = int(input(f"Type your birth {order[i]}: "))
    date1.append(date)
date1.append(name1)

name2 = input("Type your name: ")
for i in range(3):
    date = int(input(f"Type your birth {order[i]}: "))
    date2.append(date)
date2.append(name2)

older(date1,date2)
