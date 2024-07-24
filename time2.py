
# Prompt the user to input the current time and store it as a string
str_time = input("What time is it now?")

# Prompt the user to input the number of hours to wait and store it as a string
str_wait_time = input("What is the number of hours to wait? ")

# Convert the current time from a string to an integer
time = int(str_time)

# Convert the wait time from a string to an integer
wait_time = int(str_wait_time)

# Calculate the time when the alarm will go off by adding the current time and wait time, then taking the result modulo 24
time_when_alarm_go_off = (time + wait_time) % 24

# Print the time when the alarm will go off
print(time_when_alarm_go_off)
