import pandas as pd
import openpyxl

#Import the dataframe from csv file
df = pd.read_csv("UKTemperatures.csv")

#Rename the column of the date and time and split it into two columns
df.rename(columns={'Unnamed: 0':'Date'},inplace=True)
df[['Date','Time']]= df['Date'].str.split(' ', n = 1, expand = True)

#Insert a column at the end to store the average temperature of each meassurement taken
df.insert( 8, 'Average', df.mean(axis=1), allow_duplicates=False)

#Replace the nan values with the mean value calculated
df.fillna({'Brice Norton': df.Average,'Herstmonceux': df.Average,'Heathrow': df.Average,'Nottingham': df.Average,'Shawbury': df.Average,'Waddington': df.Average}, inplace=True)

#Calculate the weighted average and store it in a column
df.insert( 9, 'UK Average', (df['Brice Norton']*0.14+df['Herstmonceux']*0.1+df['Heathrow']*0.3+df['Nottingham']*0.13+df['Shawbury']*0.2+df['Waddington']*0.13), allow_duplicates=False)
df['Date']=pd.to_datetime(df.Date, dayfirst=True)
#Group measurements by day in order to calculate the average temperature of each day
# Result = pd.DataFrame(df.groupby('Date')['UK Average'].mean())
Result = df.groupby('Date')['UK Average'].mean()

#Print the results
print('The average temperature each day is:\n')
print(Result)

#Store the results to a csv file
Result.to_csv(r'Result.csv')
