import random


numbers = [50 , 1.5 , 5]
lowest = numbers[0]
for i in numbers:
    if i < lowest:
        lowest = i
    print(lowest)