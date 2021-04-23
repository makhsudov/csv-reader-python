import csv
array = []

path = ''
i = 0
with open(path, encoding='utf-8') as r_file:
    # Separator character ","
    csvReader = csv.DictReader(r_file, delimiter = ",")
    # Reading data from a CSV file 
    for row in csvReader:
        if i == 0:
            # Displays the first line that contains the headings for the columns 
            print(f'Columns: {", ".join(row)}')
        # Writing to an array of elements from a row called Row Name 
        elements = (f'{row["Row Name"]}')
        array.append (elements)
        i += 1
    print(f'There are {i} lines in the file.')