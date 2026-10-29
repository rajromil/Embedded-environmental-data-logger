import sqlite3
from pathlib import Path


DATABASE_FILE = Path("sensor_data.db")


def run_query(cursor, title, query):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


def main():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

    run_query(cursor, "Total sensor records", """SELECT COUNT(*) AS total_records FROM sensor_readings;""")

    run_query(cursor, "Average temperature and humidity", """SELECT AVG(temperature_c) AS average_temperature, AVG(humidity_percent) AS average_humidity FROM sensor_readings;""")

    run_query(cursor, "Minimum and maximum temperature", """SELECT MIN(temperature_c) AS min_temperature, MAX(temperature_c) AS max_temperature FROM sensor_readings;""")

    run_query(cursor, "High-temperature alert count", """SELECT COUNT(*) AS alert_count FROM sensor_readings WHERE alert_status = 'ON';""")

    run_query(cursor, "Records grouped by alert status", """SELECT alert_status, COUNT(*) AS record_count FROM sensor_readings GROUP BY alert_status;""")

    run_query(cursor, "Top 5 highest temperature readings", """SELECT time_ms, temperature_c, humidity_percent, alert_status FROM sensor_readings ORDER BY temperature_c DESC LIMIT 5;""")

    run_query(cursor, "Readings above temperature threshold", """SELECT time_ms, temperature_c, humidity_percent, alert_status FROM sensor_readings WHERE temperature_c >= 25.0 ORDER BY time_ms ASC;""")

    connection.close()


if __name__ == "__main__":
    main()