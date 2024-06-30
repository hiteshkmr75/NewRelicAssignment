# New Relic Data Push Script

This Python script collects system metrics (CPU and memory usage) on a macOS machine and pushes the data to New Relic as custom metrics.

## Prerequisites

1. **Python 3**: Ensure you have Python 3 installed on your system.
   ```sh
   brew install python

2. **Install Required Libraries:** 
    pip3 install psutil requests

3. **Environment Variables:**
    export NEW_RELIC_API_KEY='your_api_key_here'

## Running the Script
    
    python3 NewRelicDataMonitor.py

## Validating Data in New Relic

To query the data in New Relic and ensure that it includes the application name, you can use the following NRQL query:

SELECT average(`Custom/CPUUsage`), average(`Custom/MemoryUsage`)
FROM Metric
WHERE appName = 'MonitorMyMachinePerformance'
SINCE 1 hour ago

