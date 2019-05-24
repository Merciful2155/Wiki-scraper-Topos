import requests
from bs4 import BeautifulSoup
import csv
# sets up for scrape
scrape_soup = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
info = BeautifulSoup(scrape_soup.text, 'html.parser')

#Finds the table containing all the information about Amecican cities 
table_info = info.find('table', style="text-align:center")
print(len(table_info))
#this finds the table elements for  cities
rows = table_info.findAll('tr')

#creates a writable csv file
with open('city_info.csv', 'w', newline='') as new_file:
	csv_writer = csv.writer(new_file)
#header for the csv file
	csv_writer.writerow(['rank', 'City', 'State', '2018 estimate', '2010 Census', 'Change', '2016 land area(mi)', '2016 land area(km^2)', '2016 population density(mi)', '2016 population density(km^2)', 'Location'])
	for row in rows: 
		data = row.findAll('td')
		datas = [i.text.strip( ) for i in data]
		csv_writer.writerow(datas)
#this for loop goes into the different links and finds more 
#information about the top 5 ranked cities
count = 1;
#loops through the top 5 cities and their hyperlinks
for x in range(1,6):
	
	count_string = str(count)
	city_name = rows[x].a
	city_links =city_name['href']
	# debuging
	print(city_links)
	find_gdp = requests.get('https://en.wikipedia.org'+city_links)
	city_info = BeautifulSoup(find_gdp.text, 'html.parser')
#finds the table containing information about the city
	city_table = city_info.find('table')
	tables = city_table.findAll('tr')
# writes the information about the city into a seperate csv file
	with open('city_info' +count_string+'.csv', 'w', newline='') as new_file:
		csv_writer = csv.writer(new_file)
		city = []
		for table in tables:
			get_th = table.findAll('th')
			get_td = table.findAll('td')
			get = [i.text.strip() for i in get_th]
			city.append(get)	
			gets = [i.text.strip() for i in get_td]
			city.append(gets)
			csv_writer.writerow(city)
			del city[:]
	#debuging
	print(count_string)
	print(count)
	count = count + 1
# can comment out all print statements. they are just used check if program is running 














