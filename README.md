# Dependency Structures

## What

This is a Python library implementing the algorithms from the book 'Dependency Structures and Lexicalized Grammars' by Marco Kuhlmann.

### 'Dependency Structures and Lexicalized Grammars' by Marco Kuhlmann

- ISSN 0302-9743
- ISBN-10 3-642-14567-1 Springer Berlin Heidelberg New York
- ISBN-13 978-3-642-14567-4 Springer Berlin Heidelberg New York

## Unicode Error on Windows

### Symptom

Python errors with an `UnicodeEncodeError`. E.g. something like: `UnicodeEncodeError: 'charmap' codec can't encode character '\u2013' in position
445: character maps to <undefined>`.

### Solution

Use Python 3.6 or newer. [Source](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep528).

If this is absolutely not an option, check this [Stackoverflow answer](https://stackoverflow.com/questions/31685841/unicodeencodeerror-with-windows-console-in-python-3#31686890).
