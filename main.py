import socket
import datetime
import os
from time import sleep

#Varible
attempts = 0
success = 0
fails = 0
log_status = False

current_time = datetime.datetime.now()
time_start = f"{current_time.hour}-{current_time.minute}-{current_time.second}_{current_time.day}-{current_time.month}-{current_time.year}"
log_file_name = f"connection_log_{time_start}.txt"

def test_connection():
    try:
        socket.create_connection(('Google.com', 80))
        return True
    except OSError:
        return False

## Main
delay = int(input("How much delay do you want between every update (in seconds): "))
print(f"Checks on if you are connected to an Internet connection will happen every {delay} second(s)")
print()

log_request = input("Do you want to create a log file (Yes/No): ")
if log_request in ["Yes", "yes", "y", "Y"]:
    log_status = True
    print(f"Log file created: '{log_file_name}'")
else:
    print("No log file will be created.")
print()
print()

while True:
    if log_status == True:
        log_file = open(log_file_name, "a")
    current_time = datetime.datetime.now()
    time = f"{current_time.hour}:{current_time.minute}:{current_time.second} {current_time.day}/{current_time.month}/{current_time.year}"

    if test_connection() == True:
        output =  f"[{time}] >> Connected"
        print(output)
        success += 1
        if log_status == True:
            log_file.write(f'\n{output}')

    if test_connection() == False:
        output = f"[{time}] >> Not Connected"
        print(output)
        fails += 1
        if log_status == True:
            log_file.write(f'\n{output}')

    if log_status == True:
        log_file.close()
    attempts += 1

    sleep(delay)