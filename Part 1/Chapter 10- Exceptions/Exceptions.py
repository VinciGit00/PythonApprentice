#Handling the ZeroDivisionError Exception
try: 
    print(5/0)
except: 
    print("Division by 0 is not allowed")

#File not found exception
try:
    with open("filename.txt") as file_object:
         contents = file_object.read()
except:
    print("file not found")