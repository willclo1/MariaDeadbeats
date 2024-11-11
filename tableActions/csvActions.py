import csv
def getNewData(fileName):
    currData = []
    with open(fileName) as file:
        allStarFullData = csv.reader(file, delimiter=',')
        header = next(allStarFullData)  # Skip the header row
        year_index = header.index("yearID") if "yearID" in header else None
        if year_index is None:
            raise ValueError("The CSV file does not contain a 'yearID' column.")

        for row in allStarFullData:
            if row[year_index] == "2023":
                currData.append(row)

    return currData