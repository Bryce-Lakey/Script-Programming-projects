organisms = int(input("Input the total number of organisms: "))
growthRate = int(input("Input the rate of growth (greater than 0): "))
growthPeriod = int(input("How many hours does it take to achieve this rate? "))
growingHours = int(input("How many hours will pass during the growth? "))

num_of_periods = growingHours // growthPeriod 
totalPopulation = organisms * (growthRate ** num_of_periods)

print("The total population after", growingHours, "hours is:", totalPopulation)


   
