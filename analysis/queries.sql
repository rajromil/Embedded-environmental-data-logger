#Count total sensor records
SELECT COUNT(*) AS total_records
FROM sensor_readings;

#Calculate average temperature and humidity
SELECT AVG(temperature_c) AS average_temperature, AVG(humidity_percent) AS average_humidity
FROM sensor_readings;

#Find minimum and maximum temperature
SELECT MIN(temperature_c) AS min_temperature, MAX(temperature_c) AS max_temperature
FROM sensor_readings;

#Count high-temperature alert events
SELECT COUNT(*) AS alert_count
FROM sensor_readings
WHERE alert_status = 'ON';

#Count records by alert status
SELECT alert_status, COUNT(*) AS record_count
FROM sensor_readings
GROUP BY alert_status;

#List the top 5 highest temperature readings
SELECT time_ms, temperature_c, humidity_percent, alert_status
FROM sensor_readings
ORDER BY temperature_c DESC
LIMIT 5;

#Find readings above the temperature threshold
SELECT time_ms, temperature_c, humidity_percent, alert_status
FROM sensor_readings
WHERE temperature_c >= 25.0
ORDER BY time_ms ASC;

#Filter out likely invalid temperature readings
SELECT COUNT(*) AS valid_records
FROM sensor_readings
WHERE temperature_c BETWEEN 10.0 AND 40.0;

#Average temperature and humidity after filtering invalid readings
SELECT 
    AVG(temperature_c) AS cleaned_average_temperature,
    AVG(humidity_percent) AS cleaned_average_humidity
FROM sensor_readings
WHERE temperature_c BETWEEN 10.0 AND 40.0;