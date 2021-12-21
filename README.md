# Dependency Structures Algorithms

This is a Python library implementing the algorithms from the book 'Dependency Structures and Lexicalized Grammars' by Marco Kuhlmann.

For one algorithm form the book's chapter 4, there is a significantly easier version in Figure 1 in the paper Treebank Grammar Techniques for Non-Projective Dependency Parsing. The library implements the paper's version.

For testing and showcasing, we use annotated dependency structures from Universal Dependencies.

## License

TODO: _Decide on a good license, in accordance with the guidelines and regulations of our institution._

## Sources

### Book 'Dependency Structures and Lexicalized Grammars'

by Marco Kuhlmann

Springer-Verlag Berlin Heidelberg

published in 2010

- ISSN 0302-9743
- ISBN-10 3-642-14567-1 Springer Berlin Heidelberg New York
- ISBN-13 978-3-642-14567-4 Springer Berlin Heidelberg New York
- eBook ISBN 978-3-642-14568-1

Find it on [Springer](https://link.springer.com/book/10.1007/978-3-642-14568-1).

### Paper 'Treebank Grammar Techniques for Non-Projective Dependency Parsing'

by Marco Kuhlmann and Giorgio Satta

in Proceedings of the 12th Conference of the European Chapter of the ACL, pages 478–486, Athens, Greece, 30 March – 3 April 2009. c©2009 Association for Computational Linguistics

Find it on [ACL Anthology](https://aclanthology.org/E09-1055.pdf).

### Universal Dependencies

Treebanks from [Universal Depndencies](https://universaldependencies.org/).

## Contributors

TODO: _check with privacy guidelines of our institutions what exactly we can list here (right now a public GitHub repository) and/or get necessary consent_

### Contact

TODO: _add contact?_

## Troubleshooting

Tested on Windows 10.

### Symptom

Python errors with an `UnicodeEncodeError`. E.g. something like: `UnicodeEncodeError: 'charmap' codec can't encode character '\u2013' in position
445: character maps to <undefined>`.

### Solution

Use Python 3.6 or newer. [Source](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep528).

If this is absolutely not an option, check this [Stackoverflow answer](https://stackoverflow.com/questions/31685841/unicodeencodeerror-with-windows-console-in-python-3#31686890).
