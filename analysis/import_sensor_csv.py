import csv
import sqlite3
from pathlib import Path


CSV_FILE = Path("SENSOR8.CSV")      #Read CSV data from this file*
DATABASE_FILE = Path("sensor_data.db")      #Create and open the database_file 


def create_table(cursor):       #Create a table in the database_file with all these data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_readings (
            time_ms INTEGER,
            temperature_c REAL,
            humidity_percent REAL,
            alert_status TEXT,
            checksum INTEGER
        );
    """)


def clear_existing_data(cursor):       #Delete old data before we import new CSV data
    cursor.execute("DELETE FROM sensor_readings;")


def import_csv(cursor):         #Import data from CSV into database_file line by line
    with CSV_FILE.open("r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:      #Insert data into corresponding columns
            cursor.execute("""
                INSERT INTO sensor_readings (
                    time_ms,
                    temperature_c,
                    humidity_percent,
                    alert_status,
                    checksum
                )
                VALUES (?, ?, ?, ?, ?);
            """, (
                int(row["time_ms"]),
                float(row["temperature_c"]),
                float(row["humidity_percent"]),
                row["alert_status"],
                int(row["checksum"])
            ))


def main():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    create_table(cursor)
    clear_existing_data(cursor)
    import_csv(cursor)

    connection.commit()
    connection.close()

    print("CSV data imported successfully.")
    print(f"Database created: {DATABASE_FILE}")


if __name__ == "__main__":
    main()