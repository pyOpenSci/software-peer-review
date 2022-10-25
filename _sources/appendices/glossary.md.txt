# Glossary

The following are common terms in the scientific python community and their
definitions for reference.

* **branch**: A parallel copy of your GitHub repo. Use branches to write code and make changes that you don't want to affect the live version of your package. When you're ready, you can merge the changes back to the "main" branch. More info [here](https://help.github.com/articles/about-branches/).
* **continuous integration**: The practice of automatically building and testing a project's source code as changes are made by developers. This helps identify bugs before they become a bigger problem. Travis CI is an example of a continuous integration service.
* **code coverage**: A measure of the fraction of lines in a project's code that are run during testing. 100% coverage means that every line of code is executed during the tests.
* **commit**: Saving a change (or changes) to git. Via git, each save/commit is given a unique ID, which lets you easily revert to a previous save/commit.
* **documentation**: Text and/or images that accompany code to explain how it works and how to use it.
* **docstring**: A miniature piece of documentation within the source code, usually documenting a specific function, class, or other piece of code.
* **linting/linter**: A linter is a program that you can run on your code to identify potential errors. There are many linters for Python, e.g. flake8.
* **module**: A file containing Python code. Modules can define functions, classes, and more, and can be imported by other Python code to use those defined objects. Some files are meant to be run directly instead of imported. These are "scripts".
* **open source**: In simple terms, software for which the source code is freely available and can be modified and redistributed. What meets the standard of "open source" can be controversial, but the Open Source Initiative has a more thorough set of [guidelines](https://opensource.org/osd-annotated).
* **slug**: A short title, containing only letters, numbers, underscores, and hyphens. For example, a slug might replace spaces with underscores. Your package's "slug" is a handy shorthand.
* **software license**: Contains the terms of use, modification, and distribution for a piece of software. Open source licenses generally grant freedom to modify and share software, but sometimes there are specific conditions. Read more from [OSI](https://opensource.org/licenses).
* **testing**: Code tests check units of code to make sure that they are producing the expected result. For example, if you have a function "sum_nums" that sums numbers, you could write a test that makes sure that sum_nums(2, 2) == 4. Writing full tests helps to avoid bugs as you are writing or modifying your code.
* **version control**: A system that keeps track of changes to files over time, allowing you to revert to a previous version if needed. For example, Git is the version control system that GitHub is built on.
