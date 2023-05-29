# **Introduction to Software Development - Report**
Assessment Name: ISAD Final Assessment
Name: Jaxon Young
Student ID: 21549827
Practical Class: Monday 10am-12pm 314.220


### **Introduction**
I used techniques and methods that I learned in this unit, such as version control and modularity principles, to create and write functional and concise code that meets the requirements stated in the assignment specification. My software tool has two main functions; finding the season of a particular country during a particular month, and comparing a certain temperature of a city with its average temperature at 9am and/or 3pm. The code initially prompts the user to select either of these tools and then to input the necessary information (country, month etc.) which it will use to determine the output. The output is displayed in a brief sentence that gives the user the answer they are requesting. The season finding tool also displays a simple image of the season along with the short sentence.

### **Module Descriptions**
###### Module: getSeason -
Imports: country (string), month (string)
Exports: season (string), season (image)
This modules purpose is to search through a dictionary and display the season of a particular country during a particular month determined through user input which is passed as the two parameters of this module. The season is displayed as both a printed sentence showing the country, month, and season, and also as an image of the season. 

###### Module: getSeasonAU -
Imports: country (string), month(string), variation(string)
Exports: season (string), season (image)
This modules purpose is also to search through a dictionary but it is specific towards Australia. It displays the Meteorological or Noongar (selected through user input) season in Australia during a particular month. This module was separated from getSeason as it was a control flag that would cause another variable (variation) to be used in the code. The season is displayed as both a printed sentence showing the country, month, and season, and also as an image of the season. This module can be used for other countries that have different sets of seasons depending on certain factors, not just Australia.
###### Module: findTemp -
Imports: city (string), time (string), temp (float)
Exports: temperature comparison, tempDiff (float) (if difference is more than 5°C)
This modules purpose is to search through a dictionary to find the average temperature of a particular city (Perth or Adelaide) at either 9am (Perth = 18.2°C, Adelaide = 16.5°C) or 3pm (Perth = 23.0°C, Adelaide = 21.0°C) and compare it with the given temperature. The given temperature is passed as a parameter from user input along with the city and time. The result is displayed as a printed sentence stating the city, time, and whether the given temperature is above, below, or equal to the average city temperature.
If the difference is more than 5°C, then the specific value of the difference is also displayed by the system. 

###### Module: inputCheck -
Imports: message (string), options (list of strings)
Exports: inputted (string)
This modules purpose is to check if the user inputted strings for country, month, variation, choice, and city are valid. A valid input means that it is in the list of strings provided through the options parameter. The message parameter is the message provided by the system to the user to indicate what the user needs to enter. 
If the user input is invalid and not one of the options in the list of strings, then the system prompts the user to re-enter their input and type in a valid option. 
If the user input is valid, returns the user input. 
###### Module: timeCheck -
Imports: message (string), options (list of strings)
Exports: inputted (string)
This modules purpose is to check if the user inputted string for time is valid meaning it is in the list of strings provided through the options parameter. The message parameter is the message provided by the system to the user to tell the user what to enter. 
If the user input is invalid, the system prompts the user to re-enter their input and select a valid option. 
If the user input is valid, returns the user input.
###### Module: tempCheck -
Imports: temp (real)
Exports: temperature (float)
This modules purpose is to check if the user inputted real number for temperature is a valid number. This is done by changing it to a float value and returning that value.
If the number is not valid then a ValueError is raised and the system prompts the user to re-enter a valid number. 
If the number is valid, returns the number.

###### Explanantion for Module Implementation:
I have chosen to implement each of these modules as they have allowed the code to be simple but also concise and clearly separated into different functions. Each of the input checking modules (inputCheck, timecheck, and tempCheck) were separated into three different modules instead of one module because each of them had a slightly different purpose. If they were all combined into one module, then the parameters would act as control flags to allow the module to decide whether to check for a valid number or a valid string which would've caused tighter coupling between modules.
Also, by using dictionaries in getSeason and findTemp, it has created for much more readable code as it allowed for the removal of multiple, unnecessary if/else statements.

### **Modularity**
###### How To Run The Code:
Run the program in Python (python3 weather.py).
User is prompted with message to select either the season finding tool or temperature comparison tool and to enter 'S' or 'T'. 

If 'S' is entered, then a list of countries is displayed and the user is prompted to type in one of these countries. 
If it is a valid country, the user is then prompted to enter a month. If the country is Australia, then the user is first prompted to select either the meteorological season of the Noongar season ('M' or 'N'), and then select a month.
The system then displays a brief sentence stating the country, month, and season along with an image of the season.

If 'T' is entered, then a list of cities is displayed and the user is prompted to type in one of these cities.
If it is a valid city, the user is then prompted to enter a time (9am or 3pm) and then the temperature of that city.
The system then calculates the difference of the inputted temperature and the average temperature of the city at that time and displays a brief sentence stating the city, time, and whether the inputted temperature is above or below the average temperature.
If the difference in temperature is more than 5°C, the system will display the exact difference in temperature.

###### Modularity Concepts In My Code:
My code contains important Modularity concepts such as loose coupling, high cohesion, and low redundancy.
It has loose coupling as there is very limited use of calls (only inputCheck being used in getSeason), my modules don't use too many parameters (highest parameter count is 3), my modules don't use global variables, and no control flags are used in the code.
It has high cohesion as control flags are not used in the code, my modules perform one specific task, and the modules don't use different data.
Finally, it has low redundancy as there is very limited duplicate code. Originally the code contained many if/else statements to sort through countries and months, but this was changed into a dictionary to reduce the redundancy of the code. 

###### Review Checklist I used (Yes means there is an issue):
#
| Item | Checklist Question | Yes/No | Description of Issue |
|:------:|:--------------------:|:--------:|----------------------:|  
|1.| Does the function have >6 input parameters? |
|2.| Does the code contain any control flags? |
|3. | Does the code contain any global variables? |
|4. | Does the module perform more than 1 task? |
|5. | Does the module deal with different data? |
|6. | Is there any duplicate code? |
|7. | Do any of the modules perform overlapping tasks? |
After using the review checklist when I completed the getSeason module, I realised that there was a lot of duplicate/redundant code. The module used many if/else statements to sort through each country and month to find the correct season. So, after learning about dictionaries in my programming unit, I changed the code in that module to instead use a dictionary to organise all of the data and to search through the dictionary using keys. 
This is what the module looked like originally (only a small section as the whole module is too long):


### **Black-box Test Cases**
Test Cases for getSeason module (Boundary Value Analysis) :
| Boundary | Test Data (country and months) | Expected Results |
|:--------:|:---------:|:---------------:|
|Between Winter and Spring in Spain | country = 'Spain', month = 'February' / month = 'March' | 1. Winter / 2. Spring 
|Between Spring and Summer in Spain | country = 'Spain', month = 'May' / month = 'June' | 1. Spring / 2. Summer
|Between Summer and Autumn in Spain | country = 'Spain', month = 'August' / month = 'September' | 1. Summer / 2. Autumn
|Between Autumn and Winter in Spain | country = 'Spain', month = 'November' / month = 'December' | 1. Autumn / 2. Winter
|Between Winter and Spring in Japan | country = 'Japan', month = 'February' / month = 'March' | 1. Winter / 2. Spring
|Between Spring and Summer in Japan | country = 'Japan', month = 'May' / month = 'June' | 1. Spring / 2. Summer
|Between Summer and Autumn in Japan | country = 'Japan', month = 'August' / month = 'September' | 1. Summer / 2. Autumn
|Between Autumn and Winter in Japan | country = 'Japan', month = 'November' / month = 'December' | 1. Autumn / 2. Winter
|Between Autumn and Winter in Mauritius | country = 'Mauritius', month = 'May' / month = 'June' | 1. Autumn / 2. Winter 
|Between Winter and Spring in Mauritius | country = 'Mauritius', month = 'September' / month = 'October'  | 1. Winter / 2. Spring
|Between Spring and Summer in Mauritius| country = 'Mauritius', month = 'November' /  month = 'December'  | 1. Spring / 2. Summer
|Between Summer and Autumn in Mauritius | country = 'Mauritius', month = 'April' / month = 'May'  | 1. Summer /  2. Autumn
|Between Northeast Monsoon and Inter-monsoon in Malaysia | country = 'Malaysia', month = 'February' / month = 'March' | 1. Northeast Monsoon / 2. Inter-monsoon
|Between Inter-monsoon and Southeast Monsoon in Malaysia | country = 'Sri Lanka', month = 'April' / month = 'May' | 1. Inter-monsoon / 2. Southeast Monsoon 
|Between Southeast Monsoon and Inter-monsoon in Malaysia| country = 'Sri Lanka', month = 'May' / month = 'June' | 1. Southeast Monsoon / 2. Inter-monsoon
| Between Inter-monsoon and Southeast Monsoon in Malaysia| country = 'Sri Lanka', month = 'August' / month = 'September' | 1. Inter-monsoon / 2. Southeast Monsoon
| Between Southeast Monsoon and Inter-monsoon in Malaysia | conuntry = 'Sri Lanka', month = 'September' / month = 'October' | 1. Southeast Monsoon / 2. Inter-monsoon
|Between Northeast Monsoon and Inter-monsoon in Sri Lanka | country = 'Sri Lanka', month = 'February' / month = 'March' | 1. Northeast Monsoon / 2. Inter-monsoon
|Between Inter-monsoon and Southeast Monsoon in Sri Lanka | country = 'Sri Lanka', month = 'April' / month = 'May' | 1. Inter-monsoon / 2. Southeast Monsoon 
|Between Southeast Monsoon and Inter-monsoon in Sri Lanka| country = 'Sri Lanka', month = 'May' / month = 'June' | 1. Southeast Monsoon / 2. Inter-monsoon
| Between Inter-monsoon and Southeast Monsoon in Sri Lanka| country = 'Sri Lanka', month = 'August' / month = 'September' | 1. Inter-monsoon / 2. Southeast Monsoon
| Between Southeast Monsoon and Inter-monsoon in Sri Lanka| conuntry = 'Sri Lanka', month = 'September' / month = 'October' | 1. Southeast Monsoon / 2. Inter-monsoon

Test Cases for getSeasonAU module (Boundary Value Analysis):
| Category (country and month/s)| Test Data (country and month, and variation if Australia) | Expected Result |
|:--------:|:---------:|:---------------:|
|Between Summer and Autumn in Australia (Meteorological Season) | country = 'Australia', month = 'February' / month = 'March', variation = 'M' | 1. Summer / 2. Autumn
|Between Autumn and Winter in Australia (Meteorological Season)| country = 'Australia', month = 'May' / month = 'June', variation = 'M' | 1. Autumn / 2. Winter
|Between Winter and Spring in Australia (Meteorological Season) | country = 'Australia', month = 'August' / month = 'September', variation = 'M' | 1. Winter / 2. Spring
|Between Spring and Summer in Australia (Meteorological Season) | country = 'Australia', month = 'November' / month = 'December', variation = 'M' | 1. Spring / 2. Summer
|Between Birak and Bunuru in Australia (Noongar Season) | country = 'Australia', month = 'January' / month = 'February', variation = 'N' | 1. Birak / 2. Bunuru
|Between Bunuru and Djeran in Australia (Noongar Season)| country = 'Australia', month = 'March' / month = 'April', variation = 'N' | 1. Bunuru / 2. Djeran
|Between Djeran and Makuru in Australia (Noongar Season)| country = 'Australia', month = 'May' / month = 'June', variation = 'N' | 1. Djeran / 2. Makuru
|Between Makuru and Djilba in Australia (Noongar Season)| country = 'Australia', month = 'July' / month = 'August', variation = 'N' | 1. Makuru / 2. Djilba
|Between Djilba and Kambarang in Australia (Noongar Season)| country = 'Australia', month = 'September' / month = 'October', variation = 'N' | 1. Djilba / 2. Kambarang
|Between Kambarang and Birak in Australia (Noongar Season)| country = 'Australia', month = 'November' / month = 'December', variation = 'N' | 1. Kambarang / 2. Birak 

Test Cases for inputCheck module (Equivalence Partitioning):
| Category | Test Data (input and options) (message doesn't make a difference) | Expected Result |
|:--------:|:---------:|:---------------:|
| Input not in list of options | input = "hello", options = ["hi", "goodbye"] | system prints invalid message and asks user to re-enter
| Input is in list of options | input = "young", options = ["Jaxon", "Young"] | returns "Young"

Test Cases for timeCheck module (Equivalence Partitioning):
| Category | Test Data (input and options) (message doesn't make a difference) | Expected Result |
|:--------:|:---------:|:---------------:|
| Input not in list of options | input = "9am", options = ["9pm", "3pm"] | system prints invalid message and asks user to re-enter
| Input is in list of options | input = "9am", options = ["9am", "3pm"] | returns "9am"

Test Cases for tempCheck module (Equivalence Partitioning):
| Category | Test Data (temp) | Expected Result |
|:--------:|:---------:|:---------------:|
| Input is not a valid number | temp = "nine eight two seven" | system prints invalid message and asks user to re-enter
| Input is a valid number | temp = "9827" | returns "9827.0"

Test Cases for findTemp module (Boundary Value Analysis):
| Boundary | Test Data (city, time, temperature) | Expected Results |
|:--------:|:---------:|:---------------:|
|Between temperature below average temperature by more than 5°C and temperature below average temperature by less than/equal to 5°C at 9am in Perth. | city = 'Perth', time = '9am', temperature = 13.19 / temperature = 13.2 | statement saying exact difference / statement not saying exact difference (just below)
|Between temperature below average temperature by less than/equal to 5°C and temperature equal to average temperature at 9am in Perth. | city = 'Perth', time = '9am', temperature = 18.19 / temperature = 18.2 | statement not saying exact difference (just below) / statement saying equal to average temperature
| Between temperature equal to average temperature and temperature above average temperature by less than/equal to 5°C at 9am in Perth | city = 'Perth', time = '9am', temperature = 18.2 / temperature = 18.21 | statement saying equal to average temperature / statement not saying exact difference (just above)
| Between temperature above average temperature by less than/equal to 5°C and temperature above average temperature by more than 5°C at 9am in Perth | city = 'Perth', time = '9am', temperature = 23.2 / temperature = 23.21 | statement not saying exact difference (just above) / statement saying exact difference
|Between temperature below average temperature by more than 5°C and temperature below average temperature by less than/equal to 5°C at 3pm in Perth. | city = 'Perth', time = '3pm', temperature = 17.99 / temperature = 18 | statement saying exact difference / statement not saying exact difference (just below)
|Between temperature below average temperature by less than/equal to 5°C and temperature equal to average temperature at 3pm in Perth. | city = 'Perth', time = '3pm, temperature = 22.99 / temperature = 23 | statement not saying exact difference (just below) / statement saying equal to average temperature
| Between temperature equal to average temperature and temperature above average temperature by less than/equal to 5°C at 3pm in Perth | city = 'Perth', time = '3pm', temperature = 23 / temperature = 23.01 | statement saying equal to average temperature / statement not saying exact difference (just above)
| Between temperature above average temperature by less than/equal to 5°C and temperature above average temperature by more than 5°C at 3pm in Perth | city = 'Perth', time = '3pm', temperature = 28 / temperature = 28.01 | statement not saying exact difference (just above) / statement saying exact difference
|Between temperature below average temperature by more than 5°C and temperature below average temperature by less than/equal to 5°C at 9am in Adelaide. | city = 'Adelaide', time = '9am', temperature = 11.49 / temperature = 11.5 | statement saying exact difference / statement not saying exact difference (just below)
|Between temperature below average temperature by less than/equal to 5°C and temperature equal to average temperature at 9am in Adelaide. | city = 'Adelaide', time = '9am', temperature = 16.49 / temperature = 16.5 | statement not saying exact difference (just below) / statement saying equal to average temperature
| Between temperature equal to average temperature and temperature above average temperature by less than/equal to 5°C at 9am in Adelaide | city = 'Adelaide', time = '9am', temperature = 16.5 / temperature = 16.51 | statement saying equal to average temperature / statement not saying exact difference (just above)
| Between temperature above average temperature by less than/equal to 5°C and temperature above average temperature by more than 5°C at 9am in Adelaide | city = 'Adelaide', time = '9am', temperature = 21.5 / temperature = 21.51 | statement not saying exact difference (just above) / statement saying exact difference
|Between temperature below average temperature by more than 5°C and temperature below average temperature by less than/equal to 5°C at 3pm in Adelaide. | city = 'Adelaide', time = '3pm', temperature = 15.99 / temperature = 16 | statement saying exact difference / statement not saying exact difference (just below)
|Between temperature below average temperature by less than/equal to 5°C and temperature equal to average temperature at 3pm in Adelaide. | city = 'Adelaide', time = '3pm', temperature = 20.99 / temperature = 21 | statement not saying exact difference (just below) / statement saying equal to average temperature
| Between temperature equal to average temperature and temperature above average temperature by less than/equal to 5°C at 3pm in Adelaide | city = 'Adelaide', time = '3pm', temperature = 21 / temperature = 21.01 | statement saying equal to average temperature / statement not saying exact difference (just above)
| Between temperature above average temperature by less than/equal to 5°C and temperature above average temperature by more than 5°C at 3pm in Adelaide | city = 'Adelaide', time = '3pm', temperature = 26 / temperature = 26.01 | statement not saying exact difference (just above) / statement saying exact difference


### **White-box Test Cases**

Test Cases for inputCheck module:
| Path | Test Data (input and options) (message doesn't make a difference)| Expected Result |
|:--------:|:---------:|:---------------:|
| Enters the while loop and enters the 'if' | input = "hello\n", options = ["Hello", "Goodbye"] | returns "Hello"
| Enters the while loop and doesn't enter the 'if' (until the second input) | input = "hello\nhi\n", options = ["Hi", "Goodbye"] | system prints invalid message and while loop repeats and then returns "Hi"

Test Cases for timeCheck module:
| Path | Test Data (input and options) (message doesn't make a difference) | Expected Result |
|:--------:|:---------:|:---------------:|
| Enters the while loop and enters the 'if' | input = "9am\n", options = ["9am", "3pm"] | returns "9am"
| Enters the while loop and doesn't enter the 'if' (until the second input) | input = "9am\n9pm\n", options = ["9pm", "3pm"] | system prints invalid message and while loop repeats and then returns "9pm"

Test Cases for tempCheck module:
| Path | Test Data (temp) | Expected Result |
|:--------:|:---------:|:---------------:|
| Enters while loop and 'try' statement success | temp = "12\n" | returns 12.0 |
| Enters while loop and exception occurs (success after second input)| temp = "twelve\n12\n" | system prints invalid message and while loop repeats and then returns 12.0
### **Test Implementation and Execution**
I used python unittest to do my code testing. 
I have setUp and tearDown modules which are used before and after each test module to create a copy of the original sys.stdin and sys.stdout before each test and reset it back to its original state after each test. This is done so any captured output or input is removed in between each test so that it doesn't interfere with the next one.

###### testInputCheck -
I tested the inputCheck module through a white box testing method. I used simulated input to test if the input will only be returned if it is a valid option from a list of strings. My first test used the simulated input "hello\n" with the valid options being ["Hello", "Goodbye"], this resulted in "Hello" being immediately returned (becomes capitalised because .title() function is used in the production code). That test is an example of the first path; entering the while loop and the 'if' statement. My second test used the simulated input "hello\nhi\n" with the valid options being ["Hi", "Goodbye"], this resulted in the first input being invalid and an 'invalid' message displaying and the user being prompted to input another string, then the second input "hi" was valid so the system returns "Hi". This test is an example of the second path; entering the while loop and not entering the 'if' statement straight away.


###### testTimeCheck -
I also tested the timeCheck module through a white box testing method. Similarly to testInputCheck, I used simulated input to test if the input will only be returned if it is a valid option from a list of strings. My first test used the simulated input "9am\n" with the valid options being ["9am", "3pm"]. thsi resulted in "9am" being immediately returned. This test shows the first path of the code; entering the while loop and the 'if' statement. My second test used the simulated input "9am\n9pm\n" with the valid options being ["9pm", "3pm"], this resulted in the first input being invalid and an 'invalid' message displaying and the user being prompted to input a new time, this is when hte second simulated input "9pm" was inputted which was valid causing the system to return "9pm". This test is an example of the second path; entering the while loop and not entering the 'if' statement straight away.


###### testTempCheck -
I also tested the tempCheck module through a white box testing method. I used simulated input to test if the input will only be returned if it is a valid number that can become a float. My first test used the simulated input "9827\n" which is a valid number and was converted to a float, returning "9827.0". This is an example of the first path of the code; entering the while loop and 'try' statement success. My second test used the simulated input "nine eight two seven\n9827\n", the first input is not a valid number as it is a string and therefore can't be converted to a float so the system displays an 'invalid number' message and prompts the user to re-enter their number. The second simulated input, however, is a valid number so it is converted to a float, returning "9827.0". This is an example of the second path of the code; entering the while loop and an exception occuring. 


###### testGetSeason -
getSeason was tested by creating a list of all the countries in the module and a list of all the months along with a dictionary containing all the information of the expected season of a country during each month. The code then used nested loops to go through every country and every month in the lists and pass them as parameters to the getSeason function while capturing the output . This output was then asserted to be equal to the expected output which was found by searching the dictionary of expected seasons (this was all done using subTests).

###### testGetSeasonAU -
getSeasonAU was also tested by creating a list of the countries (only Australia in this version of code), list of variations (Meteorological/Noongar), and a list of months along with a dictionary containing the information of the expected season of Australia during a certain month (both Meteorological and Noongar seasons). The code then used nested loops to go through each variation and each month with Australia as the country and then these values are passed as parameters to the getSeasonAU function while capturing the output. This output was then asserted to be equal to the expected output which was found by searching the dictionary for the expected season (this was all done using subTests).

###### testFindTemp -
findTemp was tested by first splitting up each part into different sections (this was done to make it more simple to code). Four sections; Perth 9am, Perth 3pm, Adelaide 9am, Adelaide 3pm. They were all tested using the same method. A list of temperatures created using the Boundary Value Analysis technique was made, and then a list of the expected outputs for each of these temperatures. The code then uses a for loop to go through each temperature value and is passed as a parameter to the findTemp function capturing the output. The output is then asserted to be equal to the corresponding expected output (this was also done using subTests).

### **Version Control**

### **Ethics**
###### How Can a Lack of Ethics and Professionalism Result in Harmful Effects (relating to my code):
A lack of ethics and/or professionalism can result in harmful effects if this code were used in a large software project as it has the capability to provide people with misinformation if it's not carefully coded. For example, a developer rushes the production code because he wants to get home early to watch T.V. while knowing that he entered average temperature data from 20 years ago. This impactful mistake could negatively effect all users of the software. By providing out of date information and advertising as up-to-date, it spreads misinformation. People could be looking into having a holiday in a different country and using this software to check the current temperature compared to the average temperature may misguide them and cause them to think a country's climate is better or worse than it actually is, persuading their decision to have a holiday there or not. The spreading of misinformation in a large software project would also be illegal and would likely result in the company who created the code getting sued or shut down. So this shows how a small ethical mistake due to laziness can cause massive disruptions to the company and all stakeholders of the code.
###### ACS Guidelines:
1.2.1 The Primacy of Public Interest -
By following this ACS guideline, many ethical problems can be avoided as the main principle of this guideline is to put the public's interest before all personal, private, and sectional interests. This essentially means that developers should prioritise the interests of the stakeholders of the code over their own. If the developer in the example above had followed this guideline, they wouldn't have slacked off and left work earlier than they should've. That developer should've put the public's interest over his own and instead of not properly completing the code to go home and watch T.V., he should've double checked the code and got it code reviewed by someone else before going home to ensure that the code is up to standard and meets the stakeholders requirements. 

1.2.3 Honesty -
By also following this ACS guideline, many ethical problems can also be avoided due to the fact that this guideline promotes the idea of being honest with everyone and to not break the trust of the public or any stakeholders. This ensures that all workers/developers will be upfront about any issues they are having instead of hiding them or lying about them which directly helps everyone involved in the production of the code and all stakeholders that are affected by the software. Referring to the example earlier, if that developer was honest, he wouldn't have entered incorrect information in the first place, but even if he did do it by accident, he would've been honest about it and informed the necessary people to let them know about his mistake. Instead, he pretended like everything was fine and left to go home which is a huge ethical and professionalism issue. 

### **Discussion**
I believe my project went fairly well but it could have gone better. My initial planning can definitely be improved as it was very limited for this assessment. I overlooked critical points that caused me to backtrack through a lot of my code such as the fact that I should have used a dictionary in my code originally instead of many 'if' statements. These mistakes were very time consuming and caused me to have to unnecessarily have to go back and change multiple sections of code. I also could've done more research beforehand on methods that would speed up the production of the main code and testing code. I ended up having to research and watch tutorials to teach myself how to do certain things while I was in the middle of creating my code, if I had done this beforehand, I would've been prepared and ready to write my code in larger increments instead of small steps. But overall, I believe my software turned out satisfactory as it meets the requirements and works as intended.