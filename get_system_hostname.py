import socket

def get_system_hostname():
  try:
    hostname = socket.gethostname()
    print(f"System Hostname: {hostname}")
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  get_system_hostname()