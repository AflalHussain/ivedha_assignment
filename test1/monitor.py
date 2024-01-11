import subprocess
import socket
import json
import datetime

def check_service_status(service_name):
    try:
        # Run 'systemctl is-active' to check if the service is active
        result = subprocess.run(['systemctl', 'is-active', service_name], capture_output=True, text=True, check=True)
        return result.stdout.strip() == 'active'
    except subprocess.CalledProcessError:
        return False

def create_json_object(service_name, status, host_name):
    return {
        "service_name": service_name,
        "service_status": "UP" if status else "DOWN",
        "host_name": host_name
    }

def main():
    services_to_check = ['httpd', 'rabbitmq', 'postgresql']

    host_name = socket.gethostname()

    for service in services_to_check:
        status = check_service_status(service)
        create_json_object(service, status, host_name)

        timestamp = datetime.now()
        status_files_dir = "status_files"
        output_file = f"{status_files_dir}/{service_name}-status-{timestamp}.json"
        with open(output_file, 'w') as file:
            json.dump(json_objects, file, indent=2)

        print(json.dumps(json_objects, indent=2))

if __name__ == "__main__":
    main()
