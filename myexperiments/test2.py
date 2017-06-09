import infermedica_api
from config_api import api

import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--sex", required=True,
	help="patient gender")
ap.add_argument("-a", "--age", type=int, default=21,
	required=True, help="# age of the patient")
ap.add_argument("-n", "--name", required=False,
        help="name of the patient")

args = vars(ap.parse_args())


#print(api.info())

# Introduction
print("="*10)
print("Your Personal Doctor")
print("="*10)


# Create diagnosis object with initial patient information.
# Note that time argument is optional here as well as in the add_symptom function
request = infermedica_api.Diagnosis(sex=args["sex"], age=args["age"])

# making a list of symptoms
s_id = ['s_1','s_12','s_18']
# variables for possible answers
p = 'present'
a = 'absent'
u = 'unknown'

state = [p,p,a]

request.add_symptom(s_id[0], state[0])
request.add_symptom(s_id[1], state[1])
request.add_symptom(s_id[2], state[2])


# call diagnosis
request = api.diagnosis(request)


# Question
print("-"*8)
print(request.question.text)  # actual text of the question
print("-"*8)

#Answer
print("-"*8)
print(request.question.items[0]['choices'][0]['label'])  # answer label
print("-"*8)
print("\n")

#Diagnosis Result
print("Diagnosis Results:")
print("*"*8)
print("It is possibly the following condition according to the mentioned symptoms")
print("{} with probability being {}".format(request.conditions[0]['name'], request.conditions[0]['probability']))
print("*"*8)

