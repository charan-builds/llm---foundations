import json
name = "Charan"
data = {
    "age": 20,
    "current status": "student",
    "hobbies":
        {
            "morning": ["playing","reading"],
            "evening": ["coding","exercising"]
        }
}

#accesing python dictionary values
print(data["hobbies"]["morning"])

# this line converts python dictionary to json string
json_str = json.dumps(data)

print(json_str)
#To verify the type of json_str
#json strng need to be always in string format
print(type(json_str))
with open("data.json","w") as json_file:
    json.dump(data,json_file,indent = 2)   
print("data written to json file successfully")



# convert json string back to python dictionary
python_dict = json.loads(json_str)
print(python_dict)
#To verify the type of python_dict  
print(type(python_dict))

