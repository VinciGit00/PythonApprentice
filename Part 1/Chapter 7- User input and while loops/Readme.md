# Chapter 7- User input and while loops

To insert input by command in python you have to use the following line:

```python
message = input("Tell me something, and I will repeat it back to you:")
```

## Using int() to accept numerical inputs

You have to do a casting from String to Int

```python
message2 = input("Print a number: ")
if (int(message2)>10):
    print("The number is greater than 10")
```

## Modulo operator

The modulo operator return the rest of the division

## While loops

```python
number = 0
while number<=5:
    print(number)
    number = number + 1
```

### Break instruction

```python
number = 0
while True:
    if(number == 5):
        break
    number = number + 1
```

## Using while loop with list and dictionaries

```python
uncorfimed_users = ["a", "b", "c"]
confirmed_users  = []

while uncorfimed_users:
    current_user = uncorfimed_users.pop()
    confirmed_users.append(current_user)
```

## Removing all instances of specific values from a list

### Removing an element from a list with a while loop

```python

```
