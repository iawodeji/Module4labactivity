# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).


year = int(input('Greetings! What is your year of origin?'))
# Prompt the user to input their year of origin
if year <= 1900:
    print ("Woah, that's the past!")
# Check if the year is less than or equal to 1900
elif year > 1900 < year < 2020:
    print ("That's totally the present!")  
# Check if the year is between 1900 and 2020
  else:
    print("Far out, that's the future!!")  
# For any year 2020 or later

