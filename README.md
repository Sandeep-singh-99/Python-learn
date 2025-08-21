# Python

## Table of Contents

- [Python Built-in Data Types](#python-built-in-data-types)
- [Random Number](#random-number)
- [Python String](./String/read.md#python-strings)
  - [Slicing Strings](./String/read.md#slicing-strings)
  - [Modify Strings](./String/read.md#modify-strings)
  - [String Concatenation](./String/read.md#string-concatenation)
  - [Format Strings](./String/read.md#format-strings)
  - [Escape Characters](./String/read.md#escape-characters)
  - [Strings Methods](./String/read.md#strings-methods)
- [Python Lists](./Python%20Lists/read.md#Lists)

## Python Built-in Data Types

In Programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:


 - Text Type: `str`<br><br>
 - Numeric Types: `int`, `float`, `complex`<br><br>
 - Sequence Types: `list`, `tuple`, `range`<br><br>
 - Mapping Type: `dict`<br><br>
 - Set Types: `set`, `frozenset`<br><br>
 - Boolean Type: `bool`<br><br>
 - Binary Types: `bytes`, `bytearray`, `memoryview`<br><br>
 - None Type: `NoneType`<br><br>

 ## Random Number

Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers:

```python
import random

print(random.randrange(1,10))
```