# Chapter 6- Dictionaries

## Definition of a dictionary

```python
alien_0 = {'color': 'green', 'points': 4}
```

## Accessing to an element of a dictionary

```python
print(alien_0['color'])
```

## Adding new elements

```python
alien_0['x_position'] = 0
alien_0['y_position'] = 1
```

## Starting with an empty dictionary

### Adding an element to the dictionary

```python
alien = {}
alien['x_position'] = 2
alien['y_position'] = 1
```

## Using .get() to Access Value

When you use .get() you pass as first element the key of the value you want find, as second parameter (optional) you pass the message you want appear when the search failed

```python
print_value = alien.get('x_position', "No points")
print(print_value)
# Return 2

print_value2 = alien.get('z_position', "No points find")
print(print_value2)
# Return No points find
```

## Looping the elements through the keys

```python
for key, value in user_0.items():
    print("key: "+str(key))
    print("value: "+str(value))
```

## Looping all and only the keys of a dictionary

```python
for key in user_0.keys():
    print(key)
```

## Looping all the values of a dictionary

```python
#Looping all the values of a dictionary
for values in user_0.values():
    print(values)
```

## Sorting a dictionary

```python
sorted_dictionary = sorted(user_0)
```

## List in a dictionary

### Example of a list in a dictionary

```python
pizza = {
    'crust' : "thick",
    'toppings': ['mushrooms', "extra cheese"]
}
```

To explore a dictionary with list inside you have to do a double loop

```python
for key, value in pizza.items():
    print(key)
    print(len(value))
    for elem in value:
        print(elem)
```

Problem: when you have a not list it return a different dimension

Solution: change the structure of the dictionary

```python
pizza = {
    'crust' : ["thick"],
    'toppings': ['mushrooms', "extra cheese"]
}

for key, value in pizza.items():
    print(key)
    for elem in value:
        print(elem)
```

## A dictionary in a dictionary

### Example

```python
users = {
    'aentsein': {
        "first" : "albert",
        "last" : "einstein",
        "location" : "princeton"
    },
    'mcurie': {
        "first" : "marie",
        "last" : "curie",
        "location" : "paris"
    }
}
```

## Iteration of a dictionary in a dictionary

## Iteration of dictionary in a dictionary

You have to use a double for loop to iterate all the elements in the dictionary in a dictionary

```python
for values in users.values():
    for key, elem in values.items():
        if key== "first":
            print(elem)
```
