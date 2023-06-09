#
# weather.py - production code for ISAD Assignment
#  
import matplotlib.pyplot as plt
import matplotlib.image as img

def inputCheck(message, options):
    """
    Checks if user input for country, month, variation, choice, and city are valid (one of the options in a list).
    If not, user is prompted to select a valid option.
    """
    while True:
        inputted = input(message).title()
        if inputted in options:
            return inputted
        print("Invalid selection. Please enter a valid option.")

def timeCheck(message, options):
    """
    Checks if user input for time is either 9am or 3pm.
    If not, user is prompted to enter a valid time.
    """
    while True:
        inputted = input(message)
        if inputted in options:
            return inputted
        print("Invalid selection. Please enter a valid time.")

def tempCheck(message):
    """
    Checks if user input for temperature is a valid number.
    If not, user is prompted to enter a valid number.
    """
    while True:
        inputted = input(message)
        try:
            temperature = float(inputted)
            return temperature
        except ValueError:
            print("Invalid temperature. Please enter a valid number.")

def getSeason(country, month):
    """
    Displays the name and an image of the season in a given country during
    a given month from user input by using a dictionary.
    If the country is Australia, either the meteorological or Noongar season is displayed based on user input. 
    """
    seasonDict = {
        "Spain": {
                "December": ["Winter", "winter.png"],
                "January": ["Winter", "winter.png"],
                "February": ["Winter", "winter.png"],
                "March": ["Spring", "spring.png"],
                "April": ["Spring", "spring.png"],
                "May": ["Spring", "spring.png"],
                "June": ["Summer", "summer.png"],
                "July": ["Summer", "summer.png"],
                "August": ["Summer", "summer.png"],
                "September": ["Autumn", "autumn.png"],
                "October": ["Autumn", "autumn.png"],
                "November": ["Autumn", "autumn.png"],
            },
        "Japan": {
                "December": ["Winter", "winter.png"],
                "January": ["Winter", "winter.png"],
                "February": ["Winter", "winter.png"],
                "March": ["Spring", "spring.png"],
                "April": ["Spring", "spring.png"],
                "May": ["Spring", "spring.png"],
                "June": ["Summer", "summer.png"],
                "July": ["Summer", "summer.png"],
                "August": ["Summer", "summer.png"],
                "September": ["Autumn", "autumn.png"],
                "October": ["Autumn", "autumn.png"],
                "November": ["Autumn", "autumn.png"],
            },
        "Mauritius": {
                "May": ["Autumn", "autumn.png"],
                "June": ["Winter", "winter.png"],
                "July": ["Winter", "winter.png"],
                "August": ["Winter", "winter.png"],
                "September": ["Winter", "winter.png"],
                "October": ["Spring", "spring.png"],
                "November": ["Spring", "spring.png"],
                "December": ["Summer", "summer.png"],
                "January": ["Summer", "summer.png"],
                "February": ["Summer", "summer.png"],
                "March": ["Summer", "summer.png"],
                "April": ["Summer", "summer.png"],
            },
        "Malaysia": {
                "December": ["Northeast Monsoon", "monsoon.png"],
                "January": ["Northeast Monsoon", "monsoon.png"],
                "February": ["Northeast Monsoon", "monsoon.png"],
                "May": ["Southeast Monsoon", "monsoon.png"],
                "September": ["Southeast Monsoon", "monsoon.png"],
                "March": ["Inter-monsoon", "inter-monsoon.png"],
                "April": ["Inter-monsoon", "inter-monsoon.png"],
                "June": ["Inter-monsoon", "inter-monsoon.png"],
                "July": ["Inter-monsoon", "inter-monsoon.png"],
                "August": ["Inter-monsoon", "inter-monsoon.png"],
                "October": ["Inter-monsoon", "inter-monsoon.png"],
                "November": ["Inter-monsoon", "inter-monsoon.png"],
            },
        "Sri Lanka": {
                "December": ["Northeast Monsoon", "monsoon.png"],
                "January": ["Northeast Monsoon", "monsoon.png"],
                "February": ["Northeast Monsoon", "monsoon.png"],
                "May": ["Southeast Monsoon", "monsoon.png"],
                "September": ["Southeast Monsoon", "monsoon.png"],
                "March": ["Inter-monsoon", "inter-monsoon.png"],
                "April": ["Inter-monsoon", "inter-monsoon.png"],
                "June": ["Inter-monsoon", "inter-monsoon.png"],
                "July": ["Inter-monsoon", "inter-monsoon.png"],
                "August": ["Inter-monsoon", "inter-monsoon.png"],
                "October": ["Inter-monsoon", "inter-monsoon.png"],
                "November": ["Inter-monsoon", "inter-monsoon.png"],
            }
        }
    season, image = seasonDict[country].get(month)
    image = img.imread(image)
    plt.imshow(image)
    print(f"\nDuring {month} in {country} the season is {season}.")
    plt.axis('off')
    plt.show()
    return season

def getSeasonAU(country,month,variation):
    seasonDict = {
        "Australia": {
            "M": {
                "December": ["Summer", "summer.png"],
                "January": ["Summer", "summer.png"],
                "February": ["Summer", "summer.png"],
                "March": ["Autumn", "autumn.png"],
                "April": ["Autumn", "autumn.png"],
                "May": ["Autumn", "autumn.png"],
                "June": ["Winter", "winter.png"],
                "July": ["Winter", "winter.png"],
                "August": ["Winter", "winter.png"],
                "September": ["Spring", "spring.png"],
                "October": ["Spring", "spring.png"],
                "November": ["Spring", "spring.png"],
        },
            "N": {
                "December": ["Birak", "birak.png"],
                "January": ["Birak", "birak.png"],
                "February": ["Bunuru", "bunuru.png"],
                "March": ["Bunuru", "bunuru.png"],
                "April": ["Djeran", "djeran.png"],
                "May": ["Djeran", "djeran.png"],
                "June": ["Makuru", "makuru.png"],
                "July": ["Makuru", "makuru.png"],
                "August": ["Djilba", "djilba.png"],
                "September": ["Djilba", "djilba.png"],
                "October": ["Kambarang", "kambarang.png"],
                "November": ["Kambarang", "kambarang.png"],
            }
        }}
    season, image = seasonDict[country][variation].get(month)
    image = img.imread(image)
    plt.imshow(image)
    print(f"\nDuring {month} in {country} the season is {season}.")
    plt.axis('off')
    plt.show()
    return season

        

def findTemp(city,time,temp):
    """
    Compares a user inputted temperature with the average temperature 
    of a city at either 9am or 3pm using a dictionary.
    If the difference in temperature is greater than 5, the value of the difference is shown.
    """
    avgTemps = {
            "Perth": {
                "9am": 18.2,
                "3pm": 23.0
                },
            "Adelaide": {
                "9am": 16.5,
                "3pm": 21.0
                }
            }
    avgTemp = avgTemps[city][time]
    tempDiff = round(temp - avgTemp, 2)

    if temp < avgTemp:
        word = "below"
    elif temp > avgTemp:
        word = "above"

    if abs(tempDiff) > 5:
        print(f"\nThe temperature in {city} at {time} is {abs(tempDiff)}°C {word} the average temperature ({avgTemp}°C).")
    elif 0 < abs(tempDiff) <= 5:
        print(f"\nThe temperature in {city} at {time} is {word} the average temperature ({avgTemp}°C).")
    else:
        print(f"\nThe temperature in {city} at {time} is equal to the average temperature ({avgTemp}°C).")




if __name__ == "__main__":
    
    choice = inputCheck("Would you like to find the season of a country during a certain month, or compare the temperature of a city with it's average temperature? (S/T): ", ["S","T"])
    
    if choice == "S":
        countries = ["Australia", "Spain", "Japan", "Mauritius", "Malaysia",
                 "Sri Lanka"]
        months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    
        print("\n=========================== SEASON FINDER ============================\n")
        print("Australia | Spain | Japan | Mauritius | Malaysia | Sri Lanka".center(70))
        print("\n======================================================================\n")
   
        country = inputCheck("Select a country from the list above: ", countries) 
        month = inputCheck("Enter a month: ", months) 
        
        if country == "Australia":
            variation = inputCheck("Would you like the Meteorological season or the Noongar season? (M/N): ", ["M", "N"])
            getSeasonAU(country, month, variation)
        else:
            getSeason(country, month)
    
    elif choice == "T":
        cities = ["Perth", "Adelaide"]
        times = ["9am", "3pm"]
        
        print("\n====================== TEMPERATURE COMPARISON ========================\n")
        print("Perth | Adelaide".center(70))
        print("\n======================================================================\n")

        city = inputCheck("Select a city from the list above: ", cities)
        time = timeCheck("Select a time (9am or 3pm): ", times) 
        temp = tempCheck("Enter the temperature (°C): ")

        findTemp(city,time,temp)

    


