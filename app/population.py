import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key,value in iterable}
            if country_dict['Country/Territory'] == 'Argentina':
                values = list(country_dict.values())[5:13]
                years = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
                both = zip(years, values)
                pop_by_year = {key: value for key, value in both}
                #print(pop_by_year)
                return pop_by_year                


if __name__ == '__main__':
    result = read_csv('./data.csv')
    print(result)