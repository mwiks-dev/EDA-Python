import pandas as pd
import requests 
import csv

# Set up the API endpoint URL
url = 'https://randomuser.me/api/'

# Set the parameters for the API request
params = {
    'results': 1000,
    'gender': 'male'
}
# Make a GET request to the API endpoint to get the data
r = requests.get(url,params=params)
# Parse the JSON data in the response and extract the user data:
data = r.json()
users = data["results"]
# print(users)

# File to store user data
filename = 'male_users.csv'
# Print the user data
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    headers = ['ID','First Name', 'Last Name', 'Email', 'Age', 'Gender','Phone Number','D.O.B','Picture','Nationality']
    writer.writerow(headers)


    for user in users:
        user_id = user['id']
        first_name = user['name']['first']
        last_name = user['name']['last']
        email = user['email']
        age = user['dob']['age']
        gender = user['gender']
        number = user['cell']
        dob = user['dob']
        picture = user['picture']
        nat = user['nat']

        row = [user_id,first_name, last_name, email, age, gender,number,dob,picture,nat]
        writer.writerow(row)



