#READ MODE

# f = open("25.demo.txt", "r")
# data = f.read()

# # #IF we have to read on a particular character

# data = f.read(5)
# print(data)

# print(data)
# print(type(data))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()

#//////////////////////////////////////////////////////////////////////////////

#Write Mode

# f = open("demo.txt", "w")

# f.write("I want to learn javascript tomorrow. 1708")
# f.write("Currently I am Persuing The Btech From Global College")
# f.write("Yash Mishra")
# f.close()

#///////////////////////////////////////////////////////////////////////////////

#Append Mode
# f = open("demo.txt", "a")

# f.write("Then I'll move to reactJS\n After that nodeJS")

# f.close()

# f = open("sample.txt","w") #If a file can't exists then this way we can create a new file
# f.close()

# f = open("yash.txt", "w")
# f.close()

#///////////////////////////////////////////////////
# f = open("demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()

#///////////////////////////////////////////////////////////
#With Syntax
# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("sample.txt","w") as f:
#     data = f.write("new data")
#     print(data)    

# import os 

# os.remove("sample.txt")#Deleting a Particular File



