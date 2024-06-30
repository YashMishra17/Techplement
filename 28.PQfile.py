with open("practice.txt","w") as f:
    f.write("Hi Everyone\nwe are learning file I/O\nusing JAVA\nI like programming in JAVA")


#1.WAF that replace all occurrence of "Java" with "Python" in above File. 
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data=data.replace("JAVA","PYTHON")
# print(new_data)  

# with open("practice.txt","w") as f:
#     f.write(new_data)

#//////////////////////////////////////////////////////////////

#2.Search if the word "Learning" exits in the file or not.(by using function)
# def check_for_word():    
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found") 
# check_for_word() 

#//////////////////////////////////////////////////////////////////////////////

#3.WAF to find in which line of the file does the words "learning" occur first Print -1 if word not found
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1

# print(check_for_line())

#4. From a file containing numbers seperated by comma , print the count of even numbers.
# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]    
    
#////////////////////////////////////////////////////////////////////////////////////

#1.WAF that replace all occurrence of "Java" with "Python" in above File. 

with open("practice.txt","r") as f:
    data = f.read()   

new_data = data.replace("JAVA", "PYTHON")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

