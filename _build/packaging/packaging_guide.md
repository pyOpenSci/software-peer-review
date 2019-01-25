---
redirect_from:
  - "/packaging/packaging-guide"
title: 'Before Review - Packaging Guide'
prev_page:
  url: /intro
  title: 'Home'
next_page:
  url: /peer_review/review_intro
  title: 'Peer Review Process'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Packaging Guide 

This section provides guidelines and tips for creating a Python package to submit for peer-review.

## Overview
pyOpenSci packages must:
- Have a clear README.
- Contain full documentation for any user-facing functions.
- Have a test suite that covers the major functionality of the package.
- Use continuous integration.
- Use an OSI approved software license.

Do not be intimidated if you haven't created a Python package before. We have a template and guidelines to help you meet all of these requirements! Below, we'll also go into more detail on each of the requirements.

## Project Template
To help you package your project, we provide a template "cookiecutter" repository. You don't have to use the template as a starting point, but it may help if you are not experienced with setting up tests, documentation, and continuous integration.

### Template Instructions
- We are still building the template. To be filled in later.
github.com/pyOpenSci/cookiecutter-pyopensci


## Requirements
### README
All packages should have a README.md in their root directory. The README should include, from top to bottom:

- The package name
- Badges for continuous integration and test coverage, the badge for pyOpenSci peer-review once it has started (see below), a repostatus.org badge, and any other badges. If the README has many more badges, you might want to consider using a table for badges, see this example, that one and that one. Such a table shoud be more wide than high.
- Short description of goals of package, with descriptive links to all vignettes (rendered, i.e. readable, cf the documentation website section) unless the package is small and there’s only one vignette repeating the README.
- Installation instructions
- Any additional setup required (authentication tokens, etc)
- Brief demonstration usage
- If applicable, how the package compares to other similar packages and/or how it relates to other packages
- Citation information


### Documentation
All external package functions, classes, and methods should be fully documented with examples. 


### Testing
- All packages should have a test suite that covers major functionality of the package. The tests should also cover the behavior of the package in case of errors.

- It is good practice to write unit tests for all functions, and all package code in general, ensuring key functionality is covered. Test coverage below 75% will likely require additional tests or explanation before being sent for review.

- We recommend using pytest for writing tests, but you can use other tools. Strive to write tests as you write each new function. This serves the obvious need to have proper testing for the package, but allows you to think about various ways in which a function can fail, and to defensively code against those.

- Consider using tox to test your package with multiple versions of Python 2 and 3.

* Once you've set up CI, use your package's code coverage report (cf [this section of our book](https://ropensci.github.io/dev_guide/ci.html#coverage)) to identify untested lines, and to add further tests.


### Continuous Integration
All pyOpenSci packages must use some form of continuous integration.

- For Linux and Mac OSX, we suggest Travis CI.
- For Windows, we suggest AppVeyor CI.
- In many cases, you will want CI for all platforms. Different continuous integration services will support builds on different operating systems. Packages should have CI for all platforms when they contain:

    - Compiled code

    - Java dependencies

    - Dependencies on other languages

    - Packages with system calls

    - Text munging such as getting people’s names (in order to find encoding issues).

    - Anything with file system / path calls

    - In case of any doubt regarding the applicability of these criteria to your package, it’s better to add CI for all platforms, and most often not too much hassle.

### License
pyOpenSci projects should use an open source software license that is approved by the Open Software Initiative (OSI). OSI's website has a [list of popular licenses](https://opensource.org/licenses), and GitHub has a [handy tool](https://choosealicense.com/) for choosing a license. 

## Other recommendations
### Code Style
pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

### Linting
An automatic linter (e.g. flake8) can help ensure your code is clean and free of syntax errors. These can be integrated with your CI.



