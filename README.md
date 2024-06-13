# Anomaly Detection

- Implemented Daily and Overall Humidity Calculations:
  - Developed a MapReduce program using MRJob to process a dataset of sensor readings, calculating daily average humidity for each sensor, followed by the overall average humidity across all days for each sensor.
- Anomaly Detection Based on Threshold Gap:
  - Designed a detection mechanism to identify anomalies by computing the gap between the daily and overall average humidity for each sensor. Identified and reported readings where this gap exceeded a predefined threshold `T`.
- Sorted and Formatted Output:
  - Ensured the output was structured correctly, listing the station name, date, and gap in a tab-separated format. Results were sorted alphabetically by station name and then by date in descending order, facilitating easy analysis and interpretation.
