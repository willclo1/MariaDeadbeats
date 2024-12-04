# Update Database (Python - Long Way)

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/willclo1/MariaDeadbeats.git
   ```
2. Log into your MariaDB server using the shell.
3. Create a new empty database:
   ```sql
   CREATE DATABASE MariaDeadbeats;
   ```
4. Navigate to the MariaDeadbeats database:
   ```sql
   USE MariaDeadbeats;
   ```
5. Run the SQL file to start the update:
   - **Mac/Linux:**
     ```sql
     source path/to/baseball.sql;
     ```
   - **Windows:**
     ```sql
     source C:\\path\\to\\baseball.sql;
     ```
6. Configure the `CFG` file with the correct connection information for your database.
7. Navigate to the project directory and run:
   ```bash
   python -m tableActions.updateDB
   ```
8. Your database is now updated!

---

# Update Database (SQL Dump - Short/Better Way)

### Steps:

1. Navigate to an empty database or create one:
   ```sql
   CREATE DATABASE MariaDeadbeats;
   ```
2. Run the SQL Dump file provided.
3. Your database is now updated!

---

# Updates to the Database

### Banned_Users
- **Description:**
  - A table with `id`, `username`, and `email`.
  - Used to track users banned from the Flask application.

### Batting
- **Updates:**
  - Added a new column `b_WAR` from a CSV dataset available at this link: [MLB WAR Data Historical](https://github.com/Neil-Paine-1/MLB-WAR-data-historical).

### Draft
- **Description:**
  - A table with `draft_id`, `playerID`, `yearID`, `nameFirst`, `nameLast`, `round`, `pick`, and `description`.
  - Includes data for players from the Amateur Draft (with the `description` column used to indicate this).
  - Dataset found here: [Baseball Draft Data](https://github.com/double-dose-larry/baseball_draft_data).

### Parks
- **Updates:**
  - Added `latitude` and `longitude` columns to show a map of parks in the Flask app.
  - Used Google Geocoding API to generate these values (see Python CFG file).

### Pitching
- **Updates:**
  - Added a new column `p_WAR` from a CSV dataset available at this link: [MLB WAR Data Historical](https://github.com/Neil-Paine-1/MLB-WAR-data-historical).
  - Added a new column `p_NH` for no-hitters, using data scraped from this site: [Baseball Reference No-Hitters](https://www.baseball-reference.com/friv/no-hitters-and-perfect-games.shtml?utm_campaign=2023_07_ig_possible_answers&utm_source=ig&utm_medium=sr_xsite).

### Users
- **Description:**
  - A table with `id`, `username`, `email`, `time_of_last_access`, `password_hash`, and `is_admin`.
  - Used in the Flask app to register new users.

---

# How to Run the Flask App

### Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/willclo1/MariaDeadbeatsSite.git
   ```
2. Navigate to the project root directory:
   ```bash
   cd MariaDeadbeatsSite
   ```
3. Run the Flask app:
   ```bash
   flask run
   ```
4. The project should now be running!


