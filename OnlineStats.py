#Program to compute mean and variance as values are inputted by user
print("DATA-51100, Spring 2021")
print("NAME: Joe Griffin")
print("PROGRAMMING ASSIGNMENT #1")

#Establish variables
currentMean = 0
currentVariance = 0
numValues = 0

num = int(input("Enter a number: "))
while num >=0:
    #Number of values entered by user
    numValues = numValues+1
    
    #Variance formula
    if numValues==1:
        newVariance = 0
    if numValues>1:
        newVariance = (((numValues-2) / (numValues-1)) * currentVariance) + (((num - currentMean)*(num - currentMean))/numValues)
        currentVariance = newVariance
    
    #Mean formula
    newMean = currentMean + ((num - currentMean)/numValues)
    currentMean = newMean
    
    #Round values
    newMean = round(newMean, 10)
    newVariance = round(newVariance, 10)

    #Print values
    print(f'Mean is {newMean} variance is {newVariance}')
    
    #Ask for new input
    num = int(input("Enter a number: "))
    
    