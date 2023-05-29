import sys
import io
import weather
import unittest
import matplotlib.pyplot as plt

class TestWeather(unittest.TestCase):
    def setUp(self):
        plt.ion()
        self.savedSTDIN = sys.stdin
        self.savedSTDOUT = sys.stdout

    def tearDown(self):
        plt.ioff()
        sys.stdin = self.savedSTDIN
        sys.stdout = self.savedSTDOUT

    def testInputCheck1(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("hello\nhi\n")          #ADD CORRECTION INPUT TO TABLES
        self.assertEqual(weather.inputCheck("", ["Hi", "Goodbye"]), "Hi")
    def testInputCheck2(self):                            #ADD MESSAGES AT END
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("Young\n")
        self.assertEqual(weather.inputCheck("", ["Jaxon", "Young"]), "Young") #add case sensitive stuff

    def testTimeCheck1(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9am\n3pm\n")
        self.assertEqual(weather.timeCheck("", ["9pm", "3pm"]), "3pm")
    def testTimeCheck2(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9am\n")
        self.assertEqual(weather.timeCheck("", ["9am", "3pm"]), "9am")
    
    def testTempCheck1(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("nine eight two seven\n9827")
        self.assertEqual(weather.tempCheck(""), 9827.0)
    def testTempCheck2(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9827\n")
        self.assertEqual(weather.tempCheck(""), 9827.0)

    def testGetSeason(self):
        countries = ["Spain", "Japan", "Mauritius", "Malaysia", "Sri Lanka"]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        expectedSeasons = {
                "Spain": {
                "December": "Winter",
                "January": "Winter",
                "February": "Winter",
                "March": "Spring",
                "April": "Spring",
                "May": "Spring", 
                "June": "Summer",
                "July": "Summer", 
                "August": "Summer", 
                "September": "Autumn",
                "October": "Autumn", 
                "November": "Autumn",
            },
        "Japan": {
                "December": "Winter",
                "January": "Winter",
                "February": "Winter",
                "March": "Spring", 
                "April": "Spring", 
                "May": "Spring", 
                "June": "Summer",
                "July": "Summer",
                "August": "Summer", 
                "September": "Autumn",
                "October": "Autumn",
                "November": "Autumn",
            },
        "Mauritius": {
                "May": "Autumn",
                "June": "Winter", 
                "July": "Winter", 
                "August": "Winter", 
                "September": "Winter",
                "October": "Spring", 
                "November": "Spring", 
                "December": "Summer", 
                "January": "Summer", 
                "February": "Summer", 
                "March": "Summer",
                "April": "Summer", 
            },
        "Malaysia": {
                "December": "Northeast Monsoon",
                "January": "Northeast Monsoon",
                "February": "Northeast Monsoon", 
                "May": "Southeast Monsoon", 
                "September": "Southeast Monsoon", 
                "March": "Inter-monsoon", 
                "April": "Inter-monsoon", 
                "June": "Inter-monsoon",
                "July": "Inter-monsoon", 
                "August": "Inter-monsoon", 
                "October": "Inter-monsoon", 
                "November": "Inter-monsoon", 
            },
        "Sri Lanka": {
                "December": "Northeast Monsoon",
                "January": "Northeast Monsoon", 
                "February": "Northeast Monsoon",
                "May": "Southeast Monsoon", 
                "September": "Southeast Monsoon", 
                "March": "Inter-monsoon", 
                "April": "Inter-monsoon", 
                "June": "Inter-monsoon", 
                "July": "Inter-monsoon", 
                "August": "Inter-monsoon", 
                "October": "Inter-monsoon", 
                "November": "Inter-monsoon",
            }
        }
        
        for country in countries:
            for month in months:
                with self.subTest(country=country, month=month):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    season = weather.getSeason(country, month)
                    sys.stdout = self.savedSTDOUT

                    expectedSeason = expectedSeasons[country][month]
                    self.assertEqual(capOut.getvalue().strip(), f"During {month} in {country} the season is {expectedSeason}.")
    

    def testGetSeasonAU(self):
        countries = ["Australia"]
        variations = ["M", "N"]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        expectedSeasons = {
        "Australia": {
            "M": {
                "December": "Summer",
                "January": "Summer",
                "February": "Summer",
                "March": "Autumn",
                "April": "Autumn",
                "May": "Autumn",
                "June": "Winter",
                "July": "Winter",
                "August": "Winter",
                "September": "Spring",
                "October": "Spring",
                "November": "Spring",
            },
            "N": {
                "December": "Birak",
                "January": "Birak",
                "February": "Bunuru",
                "March": "Bunuru",
                "April": "Djeran",
                "May": "Djeran",
                "June": "Makuru",
                "July": "Makuru",
                "August": "Djilba",
                "September": "Djilba",
                "October": "Kambarang",
                "November": "Kambarang",
            }
        }}
        for country in countries:
            for variation in variations:
                for month in months:
                    with self.subTest(country=country, month=month):
                        capOut = io.StringIO()
                        sys.stdout = capOut
                        season = weather.getSeasonAU(country, month, variation)
                        sys.stdout = self.savedSTDOUT

                        expectedSeason = expectedSeasons[country][variation][month]
                        self.assertEqual(capOut.getvalue().strip(), f"During {month} in {country} the season is {expectedSeason}.")


if __name__ == '__main__':
    unittest.main()
