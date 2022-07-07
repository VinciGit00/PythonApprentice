# Chapter 2- variables

## Introduction

In this chapter we talk about printing “hello world”

```python
print("Helllo world")

#Using a variable
message = "Helllo world"
print(message)
```

## Strings

A string is a series of characters

```python

String = "This is a string"
```

### .tittle()

This command makes the first lutter upper and the others lower

- Example

```python
name = "ada lovelace"
print(name.title())
```

This script print “Ada Lovelace”

### .lower()

This command makes all the letters upper

```python
print(name.upper())
```

### .upper()

This command makes all the letters lower

```python
print(name.lower())
```

### Concatenation of Strings

There are 2 possible methods of concatenation

```python
#First method of concatenation
#f means format
full_name = f"{first_name} {second_name}"

print(full_name)

#Second method of concatenation
full_name2 = first_name+" "+second_name
```

## Numbers

### Integers

Numbers without floating point

- Operations

```python
a = 2
b = 3

#Operations
c = a+b
d = a-b
e = a*b
f = a/b
```

### Floats

Numbers with floating point

Python auto choose which format the number is.

<aside>
💡 When you make a division the format is always float

</aside>

### Long numbers

For long number you can use underscore

```python
big_number = 14_000_000_000
```

### Multiple assignement

In python is possible to make possible assignement for multiple variables

```python
x,y,z = 1 , 2, 3
```

### Casting when you print

```python
print("x = "+str(x))
```
