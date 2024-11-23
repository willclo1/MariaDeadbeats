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

def getAllData(fileName):
    currData = []
    with open(fileName, encoding='latin1') as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        for row in data:
            currData.append(row)

    return currData

def getDraftData(fileName):
    """
    Extract draft-related data, including nameFirst, nameLast, and attributes used for disambiguation.
    Attributes not part of the Draft table (e.g., weight, bats, throws, birth_date) are used only for mapping.
    """
    import datetime

    draft_data = []
    with open(fileName, encoding="latin-1") as file:
        data = csv.reader(file, delimiter=',')
        header = next(data)
        name_index = header.index("name_first_last")
        round_index = header.index("round")
        pick_index = header.index("pick")
        description_index = header.index("description")
        weight_index = header.index("weight")
        bats_index = header.index("bats")
        throws_index = header.index("throws")
        birth_date_index = header.index("birth_date")

        for row in data:
            # Split the name into first and last
            full_name = row[name_index].strip().split(" ", 1)
            nameFirst = full_name[0] if len(full_name) > 0 else None
            nameLast = full_name[1] if len(full_name) > 1 else None

            # Validate round and pick values
            round_value = int(row[round_index]) if row[round_index].isdigit() else None
            pick_value = int(row[pick_index]) if row[pick_index].isdigit() else None

            # Parse additional fields for mapping
            weight_value = int(row[weight_index]) if row[weight_index].isdigit() else None
            bats_value = row[bats_index] if row[bats_index] else None
            throws_value = row[throws_index] if row[throws_index] else None
            birth_date_value = None
            if row[birth_date_index]:
                try:
                    birth_date_value = datetime.datetime.strptime(row[birth_date_index], "%Y-%m-%d").date()
                except ValueError:
                    pass  # Skip invalid dates

            draft_row = {
                "nameFirst": nameFirst,
                "nameLast": nameLast,
                "round": round_value,
                "pick": pick_value,
                "description": row[description_index],
                "weight": weight_value,
                "bats": bats_value,
                "throws": throws_value,
                "birth_date": birth_date_value,
            }

            draft_data.append(draft_row)

    return draft_data