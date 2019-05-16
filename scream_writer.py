#works with only 1 file open at a time.
#data converted to a list ansd save to variable.
from csv import reader, writer

with open('fighters.csv') as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open('scream_fighters.csv', 'w') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

#Using nested with statements.
#data never converted to list.
from csv import reader, writer

with open('fighters.csv') as file:
    csv_reader = reader(file)
    with open('scream_fighters.csv', 'w') as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])