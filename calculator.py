import re


print('My calculator')

print('Type "quit" to exit the program\n')

run = True
previous = 0

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input('Enter equation:')
    else:
        equation = input(str(equation))

    if equation == 'quit':
        print('Goodbye, Human!!!')
        run = False
    else:
        equation = re.sub('[a-zA-Z.,:()" "]', '', equation)
        
        if previous ==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)
    print(previous)

while run:
    performMath()

