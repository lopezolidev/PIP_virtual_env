import main

#print("main.data => ",main.data)

'''
    ['ven', 'col'] [25, 40]
    Type country name: Venezuela
    [{'Country': 'Venezuela', 'Population': 25}]
    
    main.data =>  [{'Country': 'Venezuela', 'Population': 25}, {'Country': 'Colombia', 'Population': 40}]

    Control flow went directly executing the file
'''

# changing the strcture of main.data modularizing everything into a function

print("main.data: ", main.data)
# main.data:  [{'Country': 'Venezuela', 'Population': 25}, {'Country': 'Colombia', 'Population': 40}]

# we extracted that data without executing the whole file

main.run()  # calling the method where the list of countries is being read and filtered
'''
Type country name: Venezuela
[{'Country': 'Venezuela', 'Population': 25}]
'''