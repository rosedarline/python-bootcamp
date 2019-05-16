from csv import writer, DictWriter

with open("files.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Leo",
        "Breed": "Siberian",
        "Age": 2
    })