import os

hosts = ["8.8.8.8", "192.168.1.1"]  # Google DNS & local router

for host in hosts:
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is reachable")
    else:
        print(f"{host} is not reachable")
