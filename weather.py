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


    


