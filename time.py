
# Prompt the user to input the current time in hours (0-23) and store it as a string
currentTimeStr = input("What is the current time (in hours 0-23)?")

# Prompt the user to input the number of hours to wait and store it as a string
waitTimeStr = input("How many hours do you want to wait?")

# Convert the current time from a string to an integer
currentTimeInt = int(currentTimeStr)

# Convert the wait time from a string to an integer
waitTimeInt = int(waitTimeStr)


finalTimeInt = (currentTimeInt + waitTimeInt) % 24

# Print the final time
print(finalTimeInt)
