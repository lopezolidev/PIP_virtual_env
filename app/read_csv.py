import csv      # calling the native python module to read csv files

def read_csv(path): # declaring the function
    with open(path, 'r') as csvfile:     # reading the file pointing it is going to use the '.close()' method
        reader = csv.reader(csvfile, delimiter=',') # reading the csv file and pointing the delimiter
        header = next(reader)       # iterating to the first line of the file, being the columns of each row
        data = []   # we want a list of dictionaries related to each country
        for row in reader:  # for loop to read each row of the file 
            iterable = zip(header, row) # linking two lists into a list of tuples (header_key, row_value)
            country_dict = {key: value for key, value in iterable}  # using dictionary comprehensions we create a dictionary from the tuples list of iterable
            data.append(country_dict)   # appending at the end of the list each new dictionary with the info of each country
        return data
# we want to execute the module in the terminal

if __name__ == '__main__':
    result = read_csv('./data.csv')
    print(result)