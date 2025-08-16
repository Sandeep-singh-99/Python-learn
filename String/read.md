## Python Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'` is the same as `"Hello"`

You can display a string literal with the `print()` function:

```python
print("Hello")
print('Hello')
```

### Quotes Inside Quotes

You can use quotes inside a string, as long as they don't match the quotes surrouding the string:

```python
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

### Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

```python
a = "Hello"
print(a)
```

### Multiline Strings

You can assign a multiline string to a variable by using three quotes:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

Or three single quotes:

```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

**Note:** in the result, the line breaks are inserted at the same position as in the code.

### Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1])
```

### Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a `for` loop.

```python
for x in "banana":
  print(x)
```

### String Length

To get the length of a string, use the `len()` function.

```python
# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
```

### Check String

To check if a certain phrase or character is present in a string, we can use the Keyword `in`.

```python
# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)
```

Use it in an `if` statement:

```python
# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
```

### Check is NOT

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.

```python
# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
```

## Slicing Strings

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

```python
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])
```

### Slice From the Start

By leaving out the start index, the range will start at the first character:

```python
# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])
```

### Slice To The End

By leaving out the end index, the range will go to the end:

```python
# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])
```

### Negative Indexing

Use negative indexes to start the slice from the end of the string:

```python
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])
```
## Modify Strings

Python has a set of built-in methods that you can use on strings.

### Upper Case

The `upper()` method returns the string in upper case:

```python
a = "Hello, World!"
print(a.upper())
```

### Lower Case

The `Lower()` method returns the string in lower case:

```python
a = "Hello, World!"
print(a.lower())
```

### Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

The `strip()` method removes any whitespace from the beginning or the end:

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

### Replace String

The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

### Split String

The `split()` method returns a list where the text between the specified separator becomes the list iterms.

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```

## String Concatenation

