from requests.adapters import HTTPAdapter
from sqlalchemy import create_engine, text
from urllib3 import Retry
from .csi3335f2024 import engineStr, API_KEY
import requests


def create_parks_columns():
    engine = create_engine(engineStr)
    with engine.connect() as conn:
        try:
            # Add the latitude and longitude columns to the parks table
            conn.execute(text("ALTER TABLE parks ADD COLUMN latitude FLOAT"))
            conn.execute(text("ALTER TABLE parks ADD COLUMN longitude FLOAT"))
            print("Columns 'latitude' and 'longitude' added successfully to the parks table.")
        except Exception as e:
            print(f"An error occurred while altering the table: {e}")


def get_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": API_KEY}

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses
        results = response.json().get("results", [])
        if results:
            location = results[0]["geometry"]["location"]
            return location["lat"], location["lng"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
    return None, None


def update_lat_longitude():
    engine = create_engine(engineStr)
    create_parks_columns()
    with engine.connect() as conn:
        try:
            result = conn.execute(text(
                "SELECT parkID, park_name, city, state, country FROM parks WHERE latitude IS NULL OR longitude IS NULL"))
            parks = result.fetchall()

            for park in parks:
                parkID, park_name, city, state, country = park
                address = f"{park_name}, {city}, {state}, {country}"

                latitude, longitude = get_coordinates(address)
                if latitude and longitude:
                    conn.execute(
                        text("UPDATE parks SET latitude = :latitude, longitude = :longitude WHERE parkID = :parkID"),
                        {"latitude": latitude, "longitude": longitude, "parkID": parkID}
                    )
                    print(f"Updated {park_name} -> Latitude: {latitude}, Longitude: {longitude}")
                else:
                    print(f"Failed to fetch coordinates for {park_name}")
        except Exception as e:
            print(f"An error occurred: {e}")

        conn.commit()
