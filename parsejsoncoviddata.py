import json
import csv

with open('covid_cases.json', 'r') as read_json:
    json_cov = json.load(read_json)

data_file = open('parsedjsonreq.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
header_exist = 0
#Retrieve the date reported, countries and territories, number of cases, and deaths.
for cov_data in json_cov['records']:
    if header_exist==0:
        titles = ['dateRep', 'countriesAndTerritories', 'cases', 'deaths']
        csv_writer.writerow(titles)
        header_exist+=1
    cov_vals = [cov_data['dateRep'], cov_data['countriesAndTerritories'], cov_data['cases'], cov_data['deaths']]
    csv_writer.writerow(cov_vals)