#
# weather.py - production code for ISAD Assignment
#  
import matplotlib.pyplot as plt
import matplotlib.image as img

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
                image = img.imread("summer.png")
                plt.imshow(image)
            elif month == "March" or month == "April" or month == "May":
                season = "Autumn"
                image = img.imread("autumn.png")
                plt.imshow(image)
            elif month == "June" or month == "July" or month == "August":
                season = "Winter"
                image = img.imread("winter.png")
                plt.imshow(image)
            else:
                season - "Spring"
                image = img.imread("spring.png")
                plt.imshow(image)

        elif variation == "Noongar":
            if month == "December" or month == "January":
                season = "Birak"
                image = img.imread("birak.png")
                plt.imshow(image)
            elif month == "February" or month == "March":
                season = "Bunuru"
                image = img.imread("bunuru.png")
                plt.imshow(image)
            elif month == "April" or month == "May":
                season = "Djeran"
                image = img.imread("djeran.png")
                plt.imshow(image)
            elif month == "June" or month == "July":
                season = "Makuru"
                image = img.imread("makuru.png")
                plt.imshow(image)
            elif month == "August" or month == "September":
                season = "Dijiba"
                image = img.imread("djilba.png")
                plt.imshow(image)
            else:
                season = "Kambarang"
                image = img.imread("kambarang.png")
                plt.imshow(image)
                
            
    elif country == "Spain" or country == "Japan":
        if month == "December" or month == "January" or month == "February":
            season = "Winter"
            image = img.imread("winter.png")
            plt.imshow(image)
        elif month == "March" or month == "April" or month == "May":
            season = "Spring"
            image = img.imread("spring.png")
            plt.imshow(image)
        elif month == "June" or month == "July" or month == "August":
            season = "Summer"
            image = img.imread("summer.png")
            plt.imshow(image)
        else:
            season = "Autumn"
            image = img.imread("autumn.png")
            plt.imshow(image)

    elif country == "Mauritius":
        if month == "May":
            season = "Autumn"
            image = img.imread("autumn.png")
            plt.imshow(image)
        elif month == "June" or month == "July" or month == "August" or month == "September":
            season = "Winter"
            image = img.imread("winter.png")
            plt.imshow(image)
        elif month == "October":
            season = "Spring"
            image = img.imread("spring.png")
            plt.imshow(image)
        else:
            season = "Summer"
            image = img.imread("summer.png")
            plt.imshow(image)

    elif country == "Malaysia" or country == "Sri Lanka":
        if month == "December" or month == "January" or month == "February":
            season = "Northeast Monsoon"
            image = img.imread("monsoon.png")
            plt.imshow(image)
        elif month == "May" or month == "September":
            season = "Southeast Monsoon"
            image = img.imread("monsoon.png")
            plt.imshow(image)
        else:
            season = "Inter-monsoon"
            image = img.imread("inter-monsoon.png")
            plt.imshow(image)
    
    print(f"\nDuring {month} in {country} the season is {season}.")
    plt.axis('off')
    plt.show()







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


    


