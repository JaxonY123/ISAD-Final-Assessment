#
# weather.py - production code for ISAD Assignment
#  
import matplotlib.pyplot as plt
import matplotlib.image as img

def getSeason(country, month):
    """
    Displays the name and an image of the season in a given country during
    a given month.
    """
    if country == "Australia":
        if variation == "M":
            if month in ["December", "January", "February"]:
                season = "Summer"
                image = img.imread("summer.png")
                plt.imshow(image)
            elif month in ["March", "April", "May"]:
                season = "Autumn"
                image = img.imread("autumn.png")
                plt.imshow(image)
            elif month in ["June", "July", "August"]:
                season = "Winter"
                image = img.imread("winter.png")
                plt.imshow(image)
            else:
                season = "Spring"
                image = img.imread("spring.png")
                plt.imshow(image)

        elif variation == "N":
            if month in ["December", "January"]:
                season = "Birak"
                image = img.imread("birak.png")
                plt.imshow(image)
            elif month in ["February", "March"]:
                season = "Bunuru"
                image = img.imread("bunuru.png")
                plt.imshow(image)
            elif month in ["April", "May"]:
                season = "Djeran"
                image = img.imread("djeran.png")
                plt.imshow(image)
            elif month in ["June", "July"]:
                season = "Makuru"
                image = img.imread("makuru.png")
                plt.imshow(image)
            elif month in ["August", "September"]:
                season = "Dijiba"
                image = img.imread("djilba.png")
                plt.imshow(image)
            else:
                season = "Kambarang"
                image = img.imread("kambarang.png")
                plt.imshow(image)
                
            
    elif country in ["Spain", "Japan"]:
        if month in ["December", "January", "February"]:
            season = "Winter"
            image = img.imread("winter.png")
            plt.imshow(image)
        elif month in ["March", "April", "May"]:
            season = "Spring"
            image = img.imread("spring.png")
            plt.imshow(image)
        elif month in ["June", "July", "August"]:
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
        elif month in ["June", "July", "August", "September"]:
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

    elif country in ["Malaysia", "Sri Lanka"]:
        if month in ["December", "January", "February"]:
            season = "Northeast Monsoon"
            image = img.imread("monsoon.png")
            plt.imshow(image)
        elif month in ["May", "September"]:
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
    country = input("Select a country from the list above: ").title()
    while country not in countries:
        country = input("\nInvalid Selection. Please select a country from the list above: ").title()
    
    # Select month, displays list of months if invalid. 
    month = input("Enter a month: ").title()
    while month not in months:
        print("\nJanuary | February | March | April | May | June | July \n August | September | October | November | December\n")
        month = input("Invalid Selection. Please select a month from the list above: ").title()
    
    if country == "Australia":
        variation = input("Would you like the Meteorological season or the Noongar season? (M/N): ").upper()
        while variation not in ["M", "N"]:
            variation = input("Invalid selection. Select Meteorological season or Noongar season (M/N): ").upper()
    
    
    getSeason(country, month)


    


