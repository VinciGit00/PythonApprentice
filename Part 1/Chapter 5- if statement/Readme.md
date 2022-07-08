# Chapter 5- if statement

## Example of if clause

```python
cars = ["audi", "bmw", "subaru", "toyota"]

for elem in cars:
    if(elem == "audi"):
        print("The car is an audi")
    else:
        print("The car is not an audi")
```

## Numeric comparison

```python
for elem in numericalList:
    if elem == 1:
        print("The number is equal to one")
```

## Checking multiple conditions

### and condition

```python
for elem in numericalList:
    if elem > 1 and elem <3:
        print("The number is equal to 2")
```

### or condition

```python
for elem in numericalList:
    if elem == 1 or elem == 3:
        print("The number is equal to 1 or to 3")
```

## Cascade conditions

```python
for elem in numericalList:
    if elem == 1:
        print("The number is equal to 1")
    elif elem == 3:
        print("The number is equal to 3")
```
