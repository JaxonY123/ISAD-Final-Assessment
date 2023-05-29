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

    def testInputCheck(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("hello\n")
        self.assertEqual(weather.inputCheck("", ["Hello", "Goodbye"]), "Hello")
        sys.stdin = io.StringIO("hello\nhi\n")          #ADD CORRECTION INPUT TO TABLES
        self.assertEqual(weather.inputCheck("", ["Hi", "Goodbye"]), "Hi")

    def testTimeCheck(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9am\n")
        self.assertEqual(weather.timeCheck("", ["9am", "3pm"]), "9am")
        sys.stdin = io.StringIO("9am\n9pm\n")
        self.assertEqual(weather.timeCheck("", ["9pm", "3pm"]), "9pm")
    
    def testTempCheck1(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("9827\n")
        self.assertEqual(weather.tempCheck(""), 9827.0)
        sys.stdin = io.StringIO("nine eight two seven\n9827")
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
                    with self.subTest(country=country, month=month, variation=variation):
                        capOut = io.StringIO()
                        sys.stdout = capOut
                        weather.getSeasonAU(country, month, variation)
                        sys.stdout = self.savedSTDOUT

                        expectedSeason = expectedSeasons[country][variation][month]
                        self.assertEqual(capOut.getvalue().strip(), f"During {month} in {country} the season is {expectedSeason}.")

    def testFindTempPerth9am(self):
        # Perth BVA Temperatures at 9am
        tempsP9am = [13.19,13.2,18.19,18.2,18.2,18.21,23.2,23.21]
        expectedOutputs = [f"The temperature in Perth at 9am is 5.01°C below the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is below the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is below the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is equal to the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is equal to the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is above the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is above the average temperature (18.2°C).",
                          f"The temperature in Perth at 9am is 5.01°C above the average temperature (18.2°C)."]
        
        for i in range(len(tempsP9am)):
                with self.subTest(tempsP9am=tempsP9am, expectedOutputs=expectedOutputs):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    weather.findTemp('Perth', '9am', tempsP9am[i])
                    sys.stdout = self.savedSTDOUT
                    
                    expectedOutput = expectedOutputs[i]
                    self.assertEqual(capOut.getvalue().strip(), expectedOutput)
       
    def testFindTempPerth3pm(self):
        # Perth BVA Temperatures at 3pm
        tempsP3pm = [17.99,18,22.99,23,23,23.01,28,28.01]
        expectedOutputs = [f"The temperature in Perth at 3pm is 5.01°C below the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is below the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is below the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is equal to the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is equal to the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is above the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is above the average temperature (23.0°C).",
                          f"The temperature in Perth at 3pm is 5.01°C above the average temperature (23.0°C)."]

        for i in range(len(tempsP3pm)):
                with self.subTest(tempsP3pm=tempsP3pm, expectedOutputs=expectedOutputs):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    weather.findTemp('Perth', '3pm', tempsP3pm[i])
                    sys.stdout = self.savedSTDOUT

                    expectedOutput = expectedOutputs[i]
                    self.assertEqual(capOut.getvalue().strip(), expectedOutput)

    def testFindTempAdelaide9am(self):
        # Adelaide BVA Temperatures at 9am
        tempsA9am = [11.49,11.5,16.49,16.5,16.5,16.51,21.5,21.51]
        expectedOutputs = [f"The temperature in Adelaide at 9am is 5.01°C below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is equal to the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is equal to the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is above the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is above the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is 5.01°C above the average temperature (16.5°C)."]

        for i in range(len(tempsA9am)):
                with self.subTest(tempsA9am=tempsA9am, expectedOutputs=expectedOutputs):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    weather.findTemp('Adelaide', '9am', tempsA9am[i])
                    sys.stdout = self.savedSTDOUT

                    expectedOutput = expectedOutputs[i]
                    self.assertEqual(capOut.getvalue().strip(), expectedOutput)
    def testFindTempAdelaide9am(self):
        # Adelaide BVA Temperatures at 9am
        tempsA9am = [11.49,11.5,16.49,16.5,16.5,16.51,21.5,21.51]
        expectedOutputs = [f"The temperature in Adelaide at 9am is 5.01°C below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is below the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is equal to the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is equal to the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is above the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is above the average temperature (16.5°C).",
                          f"The temperature in Adelaide at 9am is 5.01°C above the average temperature (16.5°C)."]

        for i in range(len(tempsA9am)):
                with self.subTest(tempsA9am=tempsA9am, expectedOutputs=expectedOutputs):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    weather.findTemp('Adelaide', '9am', tempsA9am[i])
                    sys.stdout = self.savedSTDOUT

                    expectedOutput = expectedOutputs[i]
                    self.assertEqual(capOut.getvalue().strip(), expectedOutput)
    
    def testFindTempAdelaide3pm(self):
        # Adelaide BVA Temperatures at 3pm
        tempsA3pm = [15.99,16,20.99,21,21,21.01,26,26.01]
        expectedOutputs = [f"The temperature in Adelaide at 3pm is 5.01°C below the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is below the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is below the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is equal to the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is equal to the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is above the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is above the average temperature (21.0°C).",
                          f"The temperature in Adelaide at 3pm is 5.01°C above the average temperature (21.0°C)."]

        for i in range(len(tempsA3pm)):
                with self.subTest(tempsA3pm=tempsA3pm, expectedOutputs=expectedOutputs):
                    capOut = io.StringIO()
                    sys.stdout = capOut
                    weather.findTemp('Adelaide', '3pm', tempsA3pm[i])
                    sys.stdout = self.savedSTDOUT

                    expectedOutput = expectedOutputs[i]
                    self.assertEqual(capOut.getvalue().strip(), expectedOutput, f"{tempsA3pm[i]}")

                    
                

if __name__ == '__main__':
    unittest.main()
