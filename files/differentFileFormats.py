import json 
# person = {
#     'first_name' : 'Mark',
#     'last_name' : 'abc',
#     'age' : 27,
#     'address': {
#         "streetAddress": "21 2nd Street",
#         "city": "New York",
#         "state": "NY",
#         "postalCode": "10021-3100"
#     }
# }

# person_json = json.dumps(person , indent=4)

# with open('person.json','w') as f:
#     f.write(person_json)

with open('person.json' , 'r') as f:
    content = json.load(f)

print(content , type(content))