import csv
def getNewData(fileName):
    currData = []
    with open(fileName) as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        year_index = header.index("yearID") if "yearID" in header else None
        if year_index is None:
            raise ValueError("The CSV file does not contain a 'yearID' column.")

        for row in data:
            if row[year_index] == "2023":
                currData.append(row)

    return currData


def getPeopleData(fileName):
    currData = []
    seen_players = set()  # Track playerIDs to avoid duplicates

    with open(fileName, encoding="latin-1") as file:  # Specify encoding
        data = csv.reader(file, delimiter=',')
        header = next(data)
        player_index = header.index("playerID") if "playerID" in header else None

        if player_index is None:
            raise ValueError("The CSV file does not contain a 'playerID' column.")

        for row in data:
            # Add to currData only if playerID is not already in seen_players
            if row[player_index] not in seen_players:
                seen_players.add(row[player_index])  # Mark this playerID as seen
                currData.append(row)  # Add the row to the result

    return currData