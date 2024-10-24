initialHeight = float(input("Enter the height at which the ball was dropped: "))
numBounces = int(input("Enter the amount of times the ball can bounce: "))
bounceIndex = float(input("Enter the bounciness index (number between 0 and 1): "))
totalDistance = 0

for count in range(numBounces):
    totalDistance += initialHeight
    initialHeight *= bounceIndex
    totalDistance += initialHeight

print("Total distance traveled by the ball: ", totalDistance)

    
    

    

