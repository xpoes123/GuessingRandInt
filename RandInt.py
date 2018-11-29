#Imports
import random

#Range of Guess values
IntegerMin = 1
IntegerMax = 2
#Setting up variabels
list = []
Counter = 1
amount = 1000000
#Guessing Function
for i in range(amount):


    OriginalRandomInteger = random.randint(IntegerMin, IntegerMax)

    MachineGuessing = random.randint(IntegerMin, IntegerMax)

    MachineGuessingShadow = MachineGuessing
    list.append(Counter)
    Counter = 1
    print(OriginalRandomInteger,MachineGuessing)
    print(Counter)



    while MachineGuessing != OriginalRandomInteger:


        if MachineGuessing == OriginalRandomInteger:
            print("Why")


        elif MachineGuessing > OriginalRandomInteger:

            MachineGuessing = random.randint(OriginalRandomInteger, MachineGuessingShadow-1)

            MachineGuessingShadow = MachineGuessing

            Counter = Counter+1

            print(OriginalRandomInteger,MachineGuessing)

            print(Counter)


        else:

            MachineGuessing = random.randint(MachineGuessingShadow+1, OriginalRandomInteger)

            Counter = Counter+1

            MachineGuessingShadow = MachineGuessing

            print(OriginalRandomInteger,MachineGuessing)

            print(Counter)

#Analytics
print(list)
mininum = min(list)
print("Min:", mininum)
maximum = max(list)
print("Max:", maximum)
average = sum(list)
average = average/amount
print(average)
print(IntegerMin, IntegerMax)
