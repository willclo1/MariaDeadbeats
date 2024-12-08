import pandas as pd
from bs4 import BeautifulSoup
import requests
from sqlalchemy import create_engine
from .csi3335f2024 import engineStr
from sqlalchemy.orm import sessionmaker
from Tables.negroLeague import Base, NegroLeague


def fetch_negro_league_players(url, output_csv=None):
    import re

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all rows containing player data
    rows = soup.find_all('tr', bgcolor=True)  # Look for rows with the 'bgcolor' attribute

    # Initialize a list to store player data
    players_data = []

    # Process rows to extract player data
    for row in rows:
        cols = row.find_all('td')
        if len(cols) > 3:  # Ensure there are enough columns to process
            try:
                # Extract player data
                name = cols[1].find('a').text.strip()

                # Skip players without a last name (e.g., no space in the name)
                if ' ' not in name:
                    continue

                years = cols[2].text.strip()
                start_year, end_year = years.split('-') if '-' in years else (years, years)

                position = cols[3].text.strip()

                # Replace `-` values with None
                start_year = None if start_year == '-' else start_year
                end_year = None if end_year == '-' else end_year
                position = None if position == '-' else position

                players_data.append({
                    "Name": name,
                    "Start Year": start_year,
                    "End Year": end_year,
                    "Position": position
                })
            except Exception as e:
                print(f"Error processing row: {e}")

    # Convert to a DataFrame
    df = pd.DataFrame(players_data)

    # Save the data to a CSV file if a path is provided
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Data has been successfully saved to '{output_csv}'")

    return df

    # Convert to a DataFrame
    df = pd.DataFrame(players_data)

    # Save the data to a CSV file if a path is provided
    if output_csv:
        df.to_csv(output_csv, index=False)
        print(f"Data has been successfully saved to '{output_csv}'")

    return df

def create_negro_league_table():
    engine = create_engine(engineStr, echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)

    try:
        session = session()
        session.commit()
        print("Negro League table created!")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()


def update_negro_league_table():
    # Ensure the table is created
    create_negro_league_table()

    # Fetch the data
    df = fetch_negro_league_players(
        "https://www.seamheads.com/NegroLgs/history.php?tab=players&first=1886&last=1948&lgID=All&lgType=N&NeL=Y&HOF=All&pos=All&bats=All&throws=All&results=5000&sort=Player_a")

    # Create a database engine and session
    engine = create_engine(engineStr, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Iterate through the DataFrame and add records to the table
        for _, row in df.iterrows():
            player = NegroLeague(
                playerName=row["Name"],
                startYear=int(row["Start Year"]),
                endYear=int(row["End Year"]),
                position=row["Position"]
            )
            session.add(player)


        session.commit()
        print("NegroLeague table updated successfully!")

    except Exception as e:
        session.rollback()
        print(f"An error occurred while updating the table: {e}")

    finally:
        session.close()
