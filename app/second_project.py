import charts
# import utils
import read_csv
import pandas as pd

def run():
    # we'll use pandas to do the same data processing and chart creation 
    df = pd.read_csv('./data.csv')  # using pandas to read the csv
    df = df[df['Continent'] == 'South America']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)

    # "traditional way" reading csv and manipulating data
    '''
    data = read_csv.read_csv('./data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data)) # here we only calculate south american countries population for country

    country_keys = []
    country_world_pop_perct = []
    for country in data:
        country_keys.append(country['Country/Territory'])
        country_world_pop_perct.append(float(country['World Population Percentage']))
    charts.generate_pie_chart(country_keys, country_world_pop_perct)
    '''

if __name__ == '__main__':
    run()