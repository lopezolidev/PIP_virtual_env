import utils        # importing the module → any file with '.py' extension
import read_csv
import charts

def run():
    data = read_csv.read_csv('./data.csv')
    country = input('Type country name: ')
    result = utils.population_by_country(data, country) # calling a function from a module using data from this file

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)   # calling the method of 'utils' module
        charts.generate_bar_chart(country['Country/Territory'],labels, values)
    
        print(result)   # Example: [{'Country': 'Venezuela', 'Population': 25}]

if __name__ == '__main__':  # if the file 'main.py' is being executed from the terminal, execute function 'run()'
    run()