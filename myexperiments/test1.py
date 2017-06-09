import infermedica_api
from config_api import api

print(api.info())

# Introduction
print("="*10)
print("Your Personal Doctor")
print("="*10)

# Create diagnosis object with initial patient information.
# Note that time argument is optional here as well as in the add_symptom function
request = infermedica_api.Diagnosis(sex='male', age=35)
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

# description of symptoms (we also can access list of symptoms using symptoms_list() method)
#print("%"*8)
#print("Symptoms details:")
#s1 = api.symptom_details(s_id[0])
#print(s1)
#print(len(api.symptoms_list()))
#print("%"*8)

#request.set_pursued_conditions(['c_33', 'c_49'])  # Optional

# call diagnosis
request = api.diagnosis(request)

# Access question asked by API
#print(request.question)
#Ask a question based on symptoms
print("-"*8)
print(request.question.text)  # actual text of the question
print("-"*8)
#print(request.question.items)  # list of related evidences with possible answers
#print(request.question.items[0]['id'])
#print(request.question.items[0]['name'])
#print(request.question.items[0]['choices'])  # list of possible answers
#print(request.question.items[0]['choices'][1]['id'])  # answer id
print("-"*8)
print(request.question.items[0]['choices'][0]['label'])  # answer label
print("-"*8)
print("\n")
# Access list of conditions with probabilities
#print(request.conditions)
print("Diagnosis Results:")
print("*"*8)
print("It is possibly the following condition according to the mentioned symptoms")
#print(request.conditions[0]['id'])
#print(request.conditions[0]['name'])
#print(request.conditions[0]['probability'])
print("{} with probability being {}".format(request.conditions[0]['name'], request.conditions[0]['probability']))
#print(api.condition_details(request.conditions[0]['id']))
#print(len(api.conditions_list()))
print("*"*8)


#print(request.symptoms)
#print(request)
