#
# weather.py - production code for ISAD Assignment
#  
import matplotlib.pyplot as plt
import matplotlib.image as img

def inputCheck(message, options):
    while True:
        inputted = input(message).title()
        if inputted in options:
            return inputted
        print("Invalid selection. Please enter a valid option.")

def getSeason(country, month):
    """
    Displays the name and an image of the season in a given country during
    a given month.
    """
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
                "August": ["Dijiba", "djilba.png"],
                "September": ["Dijiba", "djilba.png"],
                "October": ["Kambarang", "kambarang.png"],
                "November": ["Kambarang", "kambarang.png"],
            }
        },
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
                "December": ("Northeast Monsoon", "monsoon.png"),
                "January": ("Northeast Monsoon", "monsoon.png"),
                "February": ("Northeast Monsoon", "monsoon.png"),
                "May": ("Southeast Monsoon", "monsoon.png"),
                "September": ("Southeast Monsoon", "monsoon.png"),
                "March": ("Inter-monsoon", "inter-monsoon.png"),
                "April": ("Inter-monsoon", "inter-monsoon.png"),
                "June": ("Inter-monsoon", "inter-monsoon.png"),
                "July": ("Inter-monsoon", "inter-monsoon.png"),
                "August": ("Inter-monsoon", "inter-monsoon.png"),
                "October": ("Inter-monsoon", "inter-monsoon.png"),
                "November": ("Inter-monsoon", "inter-monsoon.png"),
            },
        "Sri Lanka": {
                "December": ("Northeast Monsoon", "monsoon.png"),
                "January": ("Northeast Monsoon", "monsoon.png"),
                "February": ("Northeast Monsoon", "monsoon.png"),
                "May": ("Southeast Monsoon", "monsoon.png"),
                "September": ("Southeast Monsoon", "monsoon.png"),
                "March": ("Inter-monsoon", "inter-monsoon.png"),
                "April": ("Inter-monsoon", "inter-monsoon.png"),
                "June": ("Inter-monsoon", "inter-monsoon.png"),
                "July": ("Inter-monsoon", "inter-monsoon.png"),
                "August": ("Inter-monsoon", "inter-monsoon.png"),
                "October": ("Inter-monsoon", "inter-monsoon.png"),
                "November": ("Inter-monsoon", "inter-monsoon.png"),
            }
        }
    if country == "Australia":
        variation = inputCheck("Would you like the Meteorological season or the Noongar season? (M/N): ", ["M", "N"])
        season, image = seasonDict[country][variation].get(month)
    else:
        season, image = seasonDict[country].get(month)

    image = img.imread(image)
    plt.imshow(image)
    print(f"\nDuring {month} in {country} the season is {season}.")
    plt.axis('off')
    plt.show()



if __name__ == "__main__":
    countries = ["Australia", "Spain", "Japan", "Mauritius", "Malaysia",
                 "Sri Lanka"]
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    
    print("\n=========================== SEASON FINDER ============================\n")
    print("Australia | Spain | Japan | Mauritius | Malaysia | Sri Lanka".center(70))
    print("\n======================================================================\n")
   
    country = inputCheck("Select a country from the list above: ", countries) 
    month = inputCheck("Enter a month: ", months) 
    
    getSeason(country, month)


    


