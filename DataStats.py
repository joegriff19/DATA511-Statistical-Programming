print("DATA 51100 - Spring 2021")
print("NAME: JOE GRIFFIN")
print("PROGRAMMING ASSIGNMENT #5")
print("")

import pandas as pd
import numpy as np
pd.set_option('mode.chained_assignment', None)

#Import file and establish lists
cps = pd.read_csv('/Users/joegriffin/Downloads/cps.csv')
cps_selected_df=cps[['School_ID', 'Short_Name', 'Is_High_School', 'Zip', 'Student_Count_Total', 'College_Enrollment_Rate_School', 'Grades_Offered_All', 'School_Hours']]
School_ID=cps_selected_df['School_ID']
Short_Name=cps_selected_df['Short_Name']
Is_High_School=cps_selected_df['Is_High_School']
Zip=cps_selected_df['Zip']
College_Enrollment_Rate_School=cps_selected_df['College_Enrollment_Rate_School']
Student_Count_Total=cps_selected_df['Student_Count_Total']
Grades_Offered_All=cps_selected_df['Grades_Offered_All']
School_Hours=cps_selected_df['School_Hours']
n = cps_selected_df['School_ID'].count()

#Calculate college enrollment rate for high schools; calculate mean; impute missing values with mean of other rates
enrollment=list()
for x in range (len(Is_High_School)):
   if Is_High_School[x] == True:
       if College_Enrollment_Rate_School[x] != College_Enrollment_Rate_School[x]:
           j=0
       else:
           enrollment.append(College_Enrollment_Rate_School[x])
enrollment_mean=np.mean(enrollment)
cps_selected_df['College_Enrollment_Rate_School'] = cps_selected_df['College_Enrollment_Rate_School'].fillna(cps_selected_df['College_Enrollment_Rate_School'].mean())
col_enrl_rate_hs_std = cps_selected_df['College_Enrollment_Rate_School'][cps_selected_df['Is_High_School']  == True].std()

#Calculate total student count, mean, and std for non-high schools
non_hs_student_count=list()
for x in range (len(Is_High_School)):
   if Is_High_School[x] == False:
       non_hs_student_count.append(Student_Count_Total[x])
non_hs_mean=np.mean(non_hs_student_count)
non_hs=cps_selected_df[['Is_High_School', 'Student_Count_Total']]
df_non_hs=non_hs[non_hs['Is_High_School'] == False]
std_non_hs=df_non_hs['Student_Count_Total'].std()

#Get lowest and highest grade
lowest_grade=list()
highest_grade=list()
highest_grade=Grades_Offered_All.apply(lambda x: x.split(",")[-1])
cps_selected_df["Grades_Offered_All"]=cps_selected_df["Grades_Offered_All"].astype(str)
cps_selected_df["Grades_Offered_All"]=cps_selected_df["Grades_Offered_All"].str.split(",", 1) 
lowest_grade=cps_selected_df["Grades_Offered_All"].str.get(0) 

#Calculate number of schools in Loop
l=0
for x in range (len(Zip)):
   if Zip[x] == 60601:
       l=l+1
   if Zip[x] == 60602:
       l=l+1
   if Zip[x] == 60603:
       l=l+1
   if Zip[x] == 60604:
       l=l+1
   if Zip[x] == 60605:
       l=l+1
   if Zip[x] == 60606:
       l=l+1
   if Zip[x] == 60607:
       l=l+1
   if Zip[x] == 60616:
       l=l+1

#Get starting hour and count tally for each starting hour
starting_hour=list()
seven=0
eight=0
nine=0
import re
for x in range (len(School_Hours)):
    if School_Hours[x] != School_Hours[x]:
        starting_hour.append(0)
    else:
        y=School_Hours[x]
        z=re.findall('[7-9]+', y)[0]
        starting_hour.append(z)
        if z=='7':
            seven=seven+1
        if z=='8':
            eight=eight+1
        if z=='9':
            nine=nine+1

#New dataframe for printing
print_df = cps_selected_df[['School_ID', 'Short_Name', 'Is_High_School', 'Zip', 'Student_Count_Total','College_Enrollment_Rate_School']].copy()
print_df['Lowest_Grade'] = lowest_grade
print_df['Highest_Grade'] = highest_grade
print_df['School_Start_Hour'] = starting_hour

#Print results
print(print_df.head(10).to_string())
print("")
print("College Enrollment Rate for High Schools = ","{:.2f}".format(enrollment_mean),' (sd=',"{:.2f}".format(col_enrl_rate_hs_std),')',sep='')
print("")
print("Total Student Count for non-High Schools = ","{:.2f}".format(non_hs_mean),' (sd=',"{:.2f}".format(std_non_hs),')',sep='')
print("")
print("Distribution of Starting Hours:")
print(" 8am:",eight)
print(" 7am:",seven)
print(" 9am:",nine)
print("")
print("Number of schools outside Loop:",len(Zip)-l)