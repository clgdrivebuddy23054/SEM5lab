import csv

# Opening the CSV file
with open('Giants.csv', mode='r') as file:
    # Reading the CSV file
    csvFile = csv.reader(file)
    
    # Skipping the header (uncomment if needed)
    # next(csvFile)  

    # Displaying the contents of the CSV file
    for line in csvFile:
        print(line)