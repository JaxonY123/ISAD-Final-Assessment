#
# weather.py - production code for ISAD Assignment
#  

def getSeason(country, month):
    """
    Displays the name and a graphic of the season in a given country during
    a given month.
    """
    season = ""
    if country == "Australia":
        pass
    elif country == "Spain" or country == "Japan":
        if month == "December" or month == "January" or month == "February":
            season = "Winter"
        elif month == "March" or month == "April" or month == "May":
            season = "Spring"
        elif month == "June" or month == "July" or month == "August":
            season = "Summer"
        else:
            season = "Autumn"

    elif country == "Mauritius":
        if month == "May":
            season = "Autumn"
        elif month == "June" or month == "July" or month == "August" or month == "September":
            season = "Winter"
        elif month == "October":
            season = "Spring"
        else:
            season = "Summer"

    elif country == "Malaysia" or country == "Sri Lanka":
        if month == "December" or month == "January" or month == "February":
            season = "Northeast Monsoon"
        elif month == "May" or month == "September":
            season = "Southeast Monsoon"
        else:
            season = "Inter-monsoon"
    print(season)

if __name__ == "__main__":
    # Valid countries and months
    countries = ["Australia", "Spain", "Japan", "Mauritius", "Malaysia",
                 "Sri Lanka"]
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    
    # Select country from given list
    print("\n====================== SEASON FINDER =======================\n")
    print("Australia | Spain | Japan | Mauritius | Malaysia | Sri Lanka")
    print("\n============================================================\n")
    country_choice = input("Select a country from the list above: ")
    while country_choice not in countries:
        country_choice = input("\nInvalid Selection. Please select a country from the list above: ")
    
    month_choice = input("Enter a month: ")
    while month_choice not in months:
        print("\nJanuary | February | March | April | May | June | July \n August | September | October | November | December\n")
        month_choice = input("Invalid Selection. Please select a month from the list above: ")
    


    


