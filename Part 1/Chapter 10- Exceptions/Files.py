
from fileinput import filename


with open('pi_digits.txt') as file_object:
    contents = file_object.read()

#print(contents)

#For selecting lines
print(contents[0:3])

#Writing to a file
#filename.txt is the name of the file
with open("filename.txt", 'w') as file_object:
    file_object.write(contents[0:1])

#Writing multiple lines
with open("filename2.txt", 'w') as file_object:
    #First line of the file
    file_object.write("Line1\n")
    #Second line of the file
    file_object.write("Line2")

