# Workout-Tracker
A terminal based application that contacts an NLP API and asks you what workout you did, and stores it at another API.

## What was Learned:
<li>HTML headers</li>
<li>API authentication</li>
<li>API keys</li>
<li>API routing</li>
<li>Enivronmental Variables</li>
<li>POST requests</li>
<li>Data Manipulation</li>

## Technologies/Libraries & Modules used:
1. API Keys
2. Requests
3. JSON
4. HTML headers
5. Abstraction

## Thorough Explanation:
<li>The program is a terminal based application that prompts the user "what workout do you want to save".</li>
<li>Once user inputs a workout the program saves that input and uses it as a prompt with headers to contact the Nutritionix NLP API: https://trackapi.nutritionix.com/v2/natural/exercise</li>
<li>The program uses the NLP API to convert any "human language" that was inputted into storable data that we can use to save the users workout.</li>
<li>When a response is made the program manipulates the JSON data to adjust it to the Sheety API and its parameters, once data has been clensed the Sheety API is contacted using headers to save the data.<br> Sheety API: https://api.sheety.co/c832e12ed4e7ab21b7eac7fca901bdf3/workoutTracker/workouts</li>
