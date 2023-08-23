import requests
from datetime import datetime

time_now = datetime.now()
GENDER = "male"
WEIGHT_KG = 72.6
HEIGHT = 193.63
AGE = 21

APP_ID = "e672490b"
API_KEY = "9b4b244b3993c6e2d01b0644ba99ddf8"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell me which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
    "query": exercise_input,
}

# How to use NLPs to store data
response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
# print(result["exercises"][0])

time_now = str(time_now).split(".")[0].split(" ")
# print(time_now)

sheety_endpoint = "https://api.sheety.co/c832e12ed4e7ab21b7eac7fca901bdf3/workoutTracker/workouts"

info = {
    "workout": {
        "date": time_now[0],
        "time": time_now[1],
        "exercise": result["exercises"][0]["name"].upper(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"],
    }
}

auth = {
    "Authorization": "Bearer 3298RYGBiuv9834fvbiuLF4wbfl4W7B"
}

# How to write to Sheet
response = requests.post(url=sheety_endpoint, json=info, headers=auth)
response.raise_for_status()
# result = response.json()
# print(result)
