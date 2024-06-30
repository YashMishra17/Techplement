# info = {
#     "key" : "value",
#     "name": "yash mishra",
#     "age" : 21,
#     "is_adult" :True,
#     "marks" : 94.4,
#     "subject": ["python", "C", "java"],#list
#     "topics":("dict", "set")#tuples
# }
# print(type(info))
# info["name"] = "shri ram" #overwrite
# info["surname"] = "mishra"
# info["marks"] = 98.8
# print(info)

#Dictionary Methods
# print(info.keys())
# print(list(info.keys()))
# print(tuple(info.keys()))
# print(info.values())
# print(info.items())
# print(list(info.items()))
# print(tuple(info.items()))
# pairs = list(info.items())
# print(pairs[0])





# null_dict = {}
# null_dict["name"] = "Yash Mishra"
# print(null_dict)

# Nested Dictionary
# student = {
#     "name" : "Yash Mishra",
#     "subject" : {
#         "phy" : 95,
#         "chem" : 98,
#         "math" : 94
#     }
# }
# print(type(student))
# print(student)
# print(student["subject"])
# print(student["subject"] ["phy"])
# print(student["subject"] ["chem"])
# print(student["subject"] ["math"])

# print(student["name"]) #1.method
# print(student.get("name")) #2.method is always preferable
# print(student.get("subject"))

# #if we write name2 in first and second method then firstmethod will return error and second method will return 'none'
# #print(student["name2"]) 
# print(student.get("name2"))

# student.update({"city" : "Jabalpur"})
# print(student)

# ///////////////////////////////////////////////////////////////////////////

# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(dict.keys())

# print(dict.values())

# print(dict.items())

# print(list(dict.keys()))

# print(tuple(dict.values()))

# print(dict.get("brand"))

# dict.update({"Age" : "60"})
# print(dict)