import subprocess
import os

directory = os.path.dirname(os.path.abspath(__file__))

smarthome_script = os.path.join(directory, 'smarthome.sh')

try:
    subprocess.run(['bash', smarthome_script], check=True)
    print("smarthome.sh executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing smarthome.sh: {e}")

docker_compose_file = os.path.join(directory, 'docker-compose.yaml')

try:
    subprocess.run(['docker-compose', '-f', docker_compose_file, 'up', '-d'], check=True)
    print("Docker Compose executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error running Docker Compose: {e}")
