#Calculating probabilities of outcomes from input file table
print("DATA-51100, Spring 2021")
print("NAME: Joe Griffin")
print("PROGRAMMING ASSIGNMENT #4")
print("")

import pandas as pd

#Import file
cars = pd.read_csv('/Users/joegriffin/Downloads/cars.csv')
cars_selected_df=cars[['make', 'aspiration']]

#Establish lists and variables
std = list()
turbo = list()
std_probabilities = list()
turbo_probabilities = list()
unique_makes=list()
unique_makes=cars_selected_df['make'].unique()
n = cars_selected_df['make'].count()

#Calculate make probability
make_counts = cars_selected_df.make.value_counts().sort_index()
asp_list = cars_selected_df.aspiration
make_probabilities = (make_counts / n * 100).round(decimals=2)
nm=len(make_counts)

#Calculate and print std and turbo probability per unique make
z=0
x=0
while x<nm:
    t=0
    y=make_counts[x]
    for i in range (0, y):
        if asp_list[z] == 'turbo':
            t=t+1
        z=z+1
    turbo.append(t)
    s=make_counts[x]-turbo[x]
    std.append(s)
    std_probabilities.append (std[x] / make_counts[x] * 100)
    turbo_probabilities.append (turbo[x] / make_counts[x] * 100)
    print('Prob(aspiration=std|make=',unique_makes[x],') = ',"{:.2f}".format(std_probabilities[x]),'%',sep = '')
    print('Prob(aspiration=turbo|make=',unique_makes[x],') = ',"{:.2f}".format(turbo_probabilities[x]),'%',sep = '')
    x=x+1

#Convert series object to dataframe for printing the output
print()
make_probabilities_df = pd.DataFrame({'make_name': cars_selected_df['make'].unique(), 'make_probability': make_probabilities})
print_make_probability = lambda x: print('Prob(make='+x.make_name+') = ',x.make_probability,'%',sep = '')
make_probabilities_df.apply(print_make_probability, axis=1)