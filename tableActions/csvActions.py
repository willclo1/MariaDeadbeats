import csv
def getNewData(fileName):
    currData = []
    with open(fileName) as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        # Convert header to lowercase for case-insensitive matching
        lower_header = [col.lower() for col in header]
        year_index = lower_header.index("yearid") if "yearid" in lower_header else None
        if year_index is None:
            raise ValueError("The CSV file does not contain a 'yearID' column (case-insensitive).")

        for row in data:
            if row[year_index] == "2023":
                currData.append(row)

    return currData


def getPeopleData(fileName):
    currData = []
    seen_players = set()

    with open(fileName, encoding="latin-1") as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        player_index = header.index("playerID") if "playerID" in header else None

        if player_index is None:
            raise ValueError("The CSV file does not contain a 'playerID' column.")

        for row in data:
            if row[player_index] not in seen_players:
                seen_players.add(row[player_index])
                currData.append(row)

    return currData

def getHomeData(fileName):
    currData = []
    with open(fileName) as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        year_index = header.index("yearkey") if "yearkey" in header else None
        if year_index is None:
            raise ValueError("The CSV file does not contain a 'yearID' column.")

        for row in data:
            if row[year_index] == "2023":
                currData.append(row)

    return currData