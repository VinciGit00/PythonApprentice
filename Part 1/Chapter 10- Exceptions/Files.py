
from fileinput import filename


with open('pi_digits.txt') as file_object:
    contents = file_object.read()

#print(contents)

#For selecting lines
print(contents[0:3])

#Writing to a file
with open("filename.txt", 'w') as file_object:
    file_object.write(contents[0:1])