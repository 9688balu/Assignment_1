import psutil
import time


def monitor_cpu(threshold=80):
    print("Monitoring CPU usage... Press Ctrl+C to stop.")
    try:
        while True:
            # Get CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                 print(f"CPU Usage: {cpu_usage}%")

            time.sleep(1)  # delay before next check

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    monitor_cpu(threshold=80)
