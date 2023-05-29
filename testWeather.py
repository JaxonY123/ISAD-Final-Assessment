import sys
import io
import weather
import unittest

class TestWeather(unittest.TestCase):
    def setUp(self):
        self.savedSTDIN = sys.stdin
        self.savedSTDOUT = sys.stdout

    def tearDown(self):
        sys.stdin = self.savedSTDIN
        sys.stdout = self.savedSTDOUT

    def testInputCheck1(self):
        sys.stdin = io.StringIO("hello\nhi\n")          #ADD CORRECTION INPUT TO TABLES
        self.assertEqual(weather.inputCheck("", ["Hi", "Goodbye"]), "Hi")
    def testInputCheck2(self):                            #ADD MESSAGES AT END
        sys.stdin = io.StringIO("Young\n")
        self.assertEqual(weather.inputCheck("", ["Jaxon", "Young"]), "Young") #add case sensitive stuff

    def testTimeCheck1(self):
        sys.stdin = io.StringIO("9am\n3pm\n")
        self.assertEqual(weather.timeCheck("", ["9pm", "3pm"]), "3pm")
    def testTimeCheck2(self):
        sys.stdin = io.StringIO("9am\n")
        self.assertEqual(weather.timeCheck("", ["9am", "3pm"]), "9am")
    
    def testTempCheck1(self):
        sys.stdin = io.StringIO("nine eight two seven\n9827")
        self.assertEqual(weather.tempCheck(""), 9827.0)
    def testTempCheck2(self):
        sys.stdin = io.StringIO("9827\n")
        self.assertEqual(weather.tempCheck(""), 9827.0)

    def testGetSeason(self):
        countries = ["Spain", "Japan", "Mauritius", "Malaysia", "Sri Lanka"]
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        expectedSeason = {
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

        capOut = io.StringIO()
        sys.
if __name__ == '__main__':
    unittest.main()
