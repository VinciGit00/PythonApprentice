# Chapter 4- Working with Lists

## Looping an entire list

For looping all the element you use a for loop

```python
for elem in magicians:
    print(elem)
```

## For loop with range

In python is also possible to do for loop with instruction instead of iterating elements

```python
for i in range(1,5):
    print(i)
```

## Slicing a list

```python
#Copying a list
a = magicians[1:2]
#2 excluded, 3 included
a = magicians[2:3]
```

## Copying a list

```python
a = magicians[:]
```
