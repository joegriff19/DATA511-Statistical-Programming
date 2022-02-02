#Nearest Neighbors Program
print("DATA-51100, Spring 2021")
print("NAME: Joe Griffin")
print("PROGRAMMING ASSIGNMENT #3")

#Import NumPy
import numpy as np

#Parse data from training and testing data
training_attributes=np.loadtxt("/Users/joegriffin/Downloads/iris-testing-data.csv", delimiter=',',usecols=(0,1,2,3))
training_labels=np.loadtxt("/Users/joegriffin/Downloads/iris-testing-data.csv", dtype='<U15', delimiter=',',usecols=(4))
testing_attributes=np.loadtxt("/Users/joegriffin/Downloads/iris-training-data.csv", delimiter=',',usecols=(0,1,2,3))
testing_labels=np.loadtxt("/Users/joegriffin/Downloads/iris-training-data.csv", dtype='<U15', delimiter=',',usecols=(4))

#Compute predicted labels and accuracy
distances=np.sqrt(((testing_attributes[:,np.newaxis] - training_attributes[np.newaxis,:])**2).sum(2)).argmin(1)
predicted_labels=np.array([[training_labels[i]] for i in distances]).reshape(training_labels.shape)

#Print results
x=0
y=1
mismatch=0
print("")
print("#, True, Predicted")
while x < 75:
    print(y, ",", testing_labels[x], ",", predicted_labels[x], sep='')
    if testing_labels[x] != predicted_labels[x]:
        mismatch=mismatch+1
    x=x+1
    y=y+1
        
#Calculate accuracy of predictions from algorithm
accuracy = ((75 - mismatch)/75.0)*100
print("Accuracy:",' ', round(accuracy,2), "%", sep='')