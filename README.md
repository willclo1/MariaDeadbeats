# MariaDeadbeats: Comprehensive Database Management Guide

Welcome to the **MariaDeadbeats** project! This guide provides detailed steps for updating your database and running the associated Flask application, along with an overview of the database updates and their functionalities.

---

## **Update Database (Python - Long Way)**

### Step-by-Step Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/willclo1/MariaDeadbeats.git
   ```

2. Log into your MariaDB server:
   ```bash
   mysql -u your_username -p
   ```

3. Create a new empty database:
   ```sql
   CREATE DATABASE MariaDeadbeats;
   ```

4. Navigate to the `MariaDeadbeats` database:
   ```sql
   USE MariaDeadbeats;
   ```

5. Run the provided SQL file to initialize the database:
   - **Mac/Linux**:
     ```sql
     source /path/to/baseball.sql;
     ```
   - **Windows**:
     ```sql
     source C:\\path\\to\\baseball.sql;
     ```

6. Configure the `cfg.py` file with the correct connection information for your database.

7. Navigate to the project directory and run the following command:
   ```bash
   python -m tableActions.updateDB
   ```

8. Your database is now updated!

---

## **Update Database (SQL Dump - Short/Better Way)**

### Step-by-Step Instructions

1. Navigate to an empty database or create one:
   ```sql
   CREATE DATABASE MariaDeadbeats;
   ```

2. Run the provided SQL Dump file:
   ```sql
   source /path/to/sql_dump_file.sql;
   ```

3. Your database is updated!

---

## **Database Updates**

### **New and Updated Tables**

#### **Banned_Users**
- **Description**: Tracks banned users from the Flask application.
- **Columns**:
  - `id`
  - `username`
  - `email`

#### **Batting**
- **Description**: Added a new column `b_WAR` for Wins Above Replacement.
- **Source**: [MLB-WAR-data-historical](https://github.com/Neil-Paine-1/MLB-WAR-data-historical).

#### **Draft**
- **Description**: Displays Amateur Draft data.
- **Columns**:
  - `draft_id`
  - `playerID`
  - `yearID`
  - `nameFirst`
  - `nameLast`
  - `round`
  - `pick`
  - `description`
- **Source**: [baseball_draft_data](https://github.com/double-dose-larry/baseball_draft_data).

#### **Parks**
- **Description**: Added `latitude` and `longitude` columns for mapping.
- **Method**: Used Google Geocoding API.

#### **Pitching**
- **Description**: Added new columns:
  - `p_WAR` for Wins Above Replacement (Source: [MLB-WAR-data-historical](https://github.com/Neil-Paine-1/MLB-WAR-data-historical))
  - `p_NH` for no-hitters (Source: [Baseball Reference](https://www.baseball-reference.com/friv/no-hitters-and-perfect-games.shtml))

#### **Users**
- **Description**: Used for user registration and management in the Flask application.
- **Columns**:
  - `id`
  - `username`
  - `email`
  - `time_of_last_access`
  - `password_hash`
  - `is_admin`

---

## **Run the Flask Application**

1. Clone the Flask application repository:
   ```bash
   git clone https://github.com/willclo1/MariaDeadbeatsSite.git
   ```

2. Navigate to the project root directory:
   ```bash
   cd MariaDeadbeatsSite
   ```

3. Run the Flask application:
   ```bash
   flask run
   ```

4. Your project is now running and accessible locally!

---

## **Enjoy Your MariaDeadbeats Project!**




