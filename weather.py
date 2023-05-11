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
        variation = input("Would you like the Meteorological season or the Noongar season? ")
        if variation == "Meteorological":
            if month == "December" or month == "January" or month == "February":
                season = "Summer"
            elif month == "March" or month == "April" or month == "May":
                season = "Autumn"
            elif month == "June" or month == "July" or month == "August":
                season = "Winter"
            else:
                season - "Spring"
        elif variation == "Noongar":
            if month == "December" or month == "January":
                season = "Birak"
            elif month == "February" or month == "March":
                season = "Bunuru"
            elif month == "April" or month == "May":
                season = "Djeran"
            elif month == "June" or month == "July":
                season = "Makuru"
            elif month == "August" or month == "September":
                season = "Dijiba"
            else:
                season = "Kambarang"
                
            
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
    
    print(f"\nDuring {month} in {country} the season is {season}.")







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
    country = input("Select a country from the list above: ")
    while country not in countries:
        country = input("\nInvalid Selection. Please select a country from the list above: ")
    
    # Select month, displays list of months if invalid. 
    month = input("Enter a month: ")
    while month not in months:
        print("\nJanuary | February | March | April | May | June | July \n August | September | October | November | December\n")
        month = input("Invalid Selection. Please select a month from the list above: ")
    
    
    getSeason(country, month)


    


