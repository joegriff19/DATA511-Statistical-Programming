#Import pandas and data file
import pandas as pd
raw_data = pd.read_csv('/Users/joegriffin/Downloads/csv_hil(1)/ss13hil.csv', usecols=['HHL', 'HINCP', 'VEH', 'TAXP', 'VALP', 'WGTP', 'MRGP', 'HHT', 'ACCESS'],
skip_blank_lines=True)
pd.set_option('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000)

#Assignment details
print("DATA-51100, Spring 2021")
print("NAME: Joe Griffin")
print("PROGRAMMING ASSIGNMENT #7")
print("")

#Table1
print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
household_income_df = raw_data[['HHT', 'HINCP']]
groups_df = household_income_df.groupby(['HHT']).agg(['mean', 'std','count','min','max'])
groups_df = groups_df.sort_values(groups_df.columns[0],ascending = False)
groups_df.rename(index={1:'Married couple household',
                     2:'Nonfamily household:Male householder:Not living alone',
                     3:'Nonfamily household:Female householder:Not living alone',
                     4:'Other family household:Male householder, no wife present',
                     5:'Other family household:Female householder, no husband present',
                     6:'Nonfamily household:Male householder:Living alone',
                     7:'Nonfamily household:Female householder:Living alone'},inplace=True)
print(groups_df)
print("")

#Table2
print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***")
hhl_access_df = raw_data[['HHL', 'ACCESS', 'WGTP']].copy()
hhl_labels = {1 : "English only",2 : "Spanish",3 : "Other Indo-European languages",4 : "Asian and Pacific Island languages",5 : "Other language"}
access_labels = {1 : "Yes, w/ Subsrc.",2 : "Yes, wo/ Subsrc.",3 : "No",4 : "All"}
hhl_access_df.dropna(inplace = True)
hhl_access_df['HHL'] = hhl_access_df['HHL'].apply(lambda id : hhl_labels[int(id)])
hhl_access_df.rename(columns = {'HHL':'HHL - Household language'}, inplace = True)
hhl_access_df['ACCESS'] = hhl_access_df['ACCESS'].apply(lambda id: access_labels[int(id)])
table_two = pd.crosstab(index=hhl_access_df['HHL - Household language'], columns=hhl_access_df['ACCESS'],values = hhl_access_df['WGTP'],aggfunc='sum', margins= True, normalize = 'all')
table_two.sort_values(by='All', ascending=False, inplace=True)
table_two = table_two.reindex(list(hhl_labels.values()) + ['All'])
table_two = table_two.applymap(lambda x: "{0:.2f}%".format(x*100))
table_two = table_two[['Yes, w/ Subsrc.','Yes, wo/ Subsrc.', 'No', 'All']]
print(table_two)
print()

#Table3
print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***")
table_three_df = raw_data[['HINCP','WGTP']]
hincp_dropnan = table_three_df.HINCP.dropna()
grouping = pd.qcut(hincp_dropnan, 3, labels=["low", "medium", "high"]) 
grouped = hincp_dropnan.groupby(grouping)
table_three = grouped.describe()
table_three= table_three[['min','max', 'mean' ,'count']]
table_three.rename(columns = {'count':'household_count'}, inplace = True)
print(table_three)
