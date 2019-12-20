import re

print("'quit' to exit\n")
previous = 0
run = True


def calculate():
    global run
    global previous
    equ = ""
    if previous ==0:
        equ = input("Enter equation:")
    else:
        equ= input(str(previous))

    if equ == 'quit':
        print("GOODBYE")
        run = False
    else:
        equ = re.sub('[a-zA-Z,.:()" "]', " ", equ)
        if previous ==0:
            previous = eval(equ)
        else:
            previous  =  eval(str(previous)+equ)


while run:
    calculate()
