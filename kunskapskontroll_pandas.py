# importing Pandas
import pandas as pd

file_path = '/Users/demafalih/Documents/kunskapskontroll2/cars_data.csv'
data = pd.read_csv(file_path)


# Explain what a CSV file is:
# En vanlig fil där jag kan ha strukturerad data då jag kan se all data i form av tabeller, typ som excell tabell men istället är det bara text i en fil. Så varje rad i texten motsvarar en rad i en tabell och kolumnerna separeras med ett kommatecken, exempel:
# name, age, city
# Elias, 17, Göteborg
# Adam, 25, Lund
# Dema, 20, Helsingborg
# En sådan fil används oftast när man vill överföra, spara eller visa data, såsom jag gör i koderna nedan.
# En csv fil är bra och användbar för att den är enkel då den är lätt att läsa, den kan öppnas i flera program och datautbyte då man kan överföra mellan olika system och program.


# Print the first 10 rows of the data
print(data.head(10))


# Print the last 5 rows
print(data.tail(5))


# By using the info method, check how many non-null rows each coloumn have
df = pd.read_csv('cars_data.csv')
df.info()


# if any column has a missing value, drop the entire row. Notice, the operation should be inplace meaning you change the dataframe itself
df.dropna(inplace=True)
df.info()
# dropna() för att ta bort rader som innehåller saknade värden
# inpkace=True för att spara/tillämpa ändringen i självaste dataframen utan att skapa en ny


# Calculate the mean of each numeric column 
mean_values = df.mean(numeric_only=True)
print(mean_values)


# select the rows where the column "company" is equal to 'honda'
honda_rows = df[df('company') == 'honda']
print(honda_rows)


# sort the data set by price in descending order. This should not be an inplace operation
sorted_df = df.sort_values(by='price', ascending=False)
print(sorted_df)


# select the rows where the column "company" is equal to any of thw values (audi, bmw, porsche)
selected_rows = df[df('company').isin(['audi', 'bmw', 'porsche'])]
print(selected_rows)
# isin() för att jag har en lista med flera alternativ och jag vill bara ha dessa tre av alla alternativ i listan


# find the number of cars (rows) for each company
car_count_by_company = df.groupby('company').size()
print(car_count_by_company)
# groupby för att inte få alla rader sammanlagt, så jag får det för EACH company
# size() för att räkna antalet rader för varje företag


# find the maximum price for each company
max_price_by_company = df.groupby('company')['price'].max()
print(max_price_by_company)
# max() för att få ut det maximala priset för VARJE företag därav använder jag också groupby