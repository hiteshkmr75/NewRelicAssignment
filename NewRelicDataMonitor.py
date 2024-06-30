import psutil
import time
import requests
import os

# Function to collect system metrics
def collect_data():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }

# Function to push data to New Relic
def push_data_to_new_relic(data):
    api_key = os.getenv('NEW_RELIC_API_KEY')
    url = 'https://metric-api.newrelic.com/metric/v1'
    app_name = 'MonitorMyMachinePerformance'

    payload = [{
        "metrics": [
            {
                "name": "Custom/CPUUsage",
                "type": "gauge",
                "value": data["cpu_usage"],
                "timestamp": int(time.time()),
                "attributes": {
                    "appName": app_name
                }
            },
            {
                "name": "Custom/MemoryUsage",
                "type": "gauge",
                "value": data["memory_usage"],
                "timestamp": int(time.time()),
                "attributes": {
                    "appName": app_name
                }
            }
        ]
    }]

    headers = {
        "Api-Key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 202:
        print("Successfully sent data to New Relic")
    else:
        print(f"Failed to send data to New Relic: {response.status_code}, {response.text}")

# Main loop to collect and send data every minute
if __name__ == "__main__":
    while True:
        data = collect_data()
        push_data_to_new_relic(data)
        time.sleep(60)  # Sleep for 60 seconds
