# Chapter 10- files and exceptions

How to resolve exceptions in Python. They are similar to Java classes.

It’s useful to learn exceptions because because in this way your Python script will never crash

# Files

With files you can manage lot of data very quickly

## Reading an entire file

We will start with a simple .txt file like this:

```
3.14
8977
2643
```

To read a file you will first need to open it with the method open(). The method needs the name of the file you want read. The file is closed when the with digit is finished.

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)
```

To specify a specific directory:

```python
with open("text_files/pi_digits.txt") as file_object:
```

![image.jpg](Chapter%2010-%20files%20and%20exceptions%2053e0627de943473d85c22eb1ae887881/image.jpg)

For larger files (like 1 million lines) the code does not change.

## Writing to a file

### Working to an empty file

```python
#Writing to a file
#filename.txt is the name of the file
with open("filename.txt", 'w') as file_object:
    file_object.write(contents[0:1])
```

### Writing multiple lines

```python
#Writing multiple lines
with open("filename2.txt", 'w') as file_object:
    #First line of the file
    file_object.write("Line1\n")
    #Second line of the file
    file_object.write("Line2")
```

# Exceptions

Exceptions are used to manage errors. If you write code to handle errors the code will continue running. Exceptions are handled with try-except module. Exceptions are used to prevent crashes

## Handling the ZeroDivisionError Exception

```python
try:
    print(5/0)
except:
    print("Division by 0 is not allowed")
```

## File not found exception

```python

```
