import math

def computeAverage(filePath):
    file = open(filePath, 'r')
    numbers = list(map(float, file.read().splitlines()))
    file.close()
    average = sum(numbers) / len(numbers)
    return average


filePath = 'average.txt'
avg = computeAverage(filePath)
print(f"The average is:", avg)
