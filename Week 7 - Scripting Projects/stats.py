import math
import statistics
numbers = [1, 2, 2, 4, 4, 4, 5]
meanList = statistics.mean(numbers)
modeList = statistics.mode(numbers)

print("Here is a list of numbers:", *numbers)
print("The mean of these numbers is:", meanList)
print("The mode of these numbers is:", modeList)
