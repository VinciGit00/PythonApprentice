# Chapter 3 - Lists

A list is a collection of items in a particular order

## Definition of a list

```python
bycles = ["trek", "bianchi", "cannondale", "specialized"]
```

## Accessing an element of a list

In python you start to count the element from 0

```python
bycles[0]
bycles[1]
bycles[2]
```

## Accessing to the last element of a list

using -1 in the square brackets allows to access to the last element in the list

```python
bycles[-1]
```

## Changing, adding and remove element in lists

Lists are usually dynamic, so you can change the values during the life of the script

## Modifying element to a list

```python
bycles[1] = "New name"
```

## Adding an element to the list

### Append at the end of the list

```python
bycles.append("appended element")
```

### Inserting an element to the list

```python
#First element = index of the list
bycles.insert(0, "inserted element")
```

## Removing an element from the list

```python
del bycles[0]
```

### Removing an element by the value

```python
bycles.remove("bianchi")
```

## Pop

When you use pop you take the element and after you delete the element from the list.

It is possible to use pop for just an element or all the list

### pop one element

```python
variable = bycles.pop(0)
```

### pop all the list

```python

newlist = bycles.pop()
```

## Sorting lists

### Ascendant

```python
bycles.sort()
```

### Descendant

```python
bycles.sort(reverse=True)
```

## Length of a list

```python
size = len(bicycles)
```
