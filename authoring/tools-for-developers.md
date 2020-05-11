# Tools for developers

This section presents some useful tools that can be very helpful for the development workflow.


## Code linters

Code linters are tools that analyze source code and identify programming errors, stylistic errors,
invalid typing, wrong or missing docstrings, etc.

Linters are often either run directly from the command-line, or they can be run as
a part of many modern code editors to give you automatic feedback about your code
structure as you write it.

Some linters that could help you to keep your code in good shape are:

- [flake8](https://flake8.pycqa.org/en/latest/)
- [mypy](http://mypy-lang.org/)
- [numpydoc](https://numpydoc.readthedocs.io/en/latest/)
- [pydocstyle](https://github.com/PyCQA/pydocstyle)


## Code stylers

Code stylers are tools that fix styling issues in a file, formatting it automatically.
Code *styling* is different from code *linting* because it doesn't change the functionality
of your code at all, it *only* changes how it looks. 
Using an automatic formatting tool helps to keep the source code within specification
and also helps review workflow. While stylers might cause your code to look differently
than you would have chosen, many projects have adopted them in order to have a single
code style that is consistent across projects.

Some popular code stylers are:

- [black](https://github.com/psf/black)
- [isort](https://github.com/timothycrosley/isort)


## Git pre-commit hook

Git pre-commit hook is a useful tool that checks your code automatically when you run a `git commit` and,
if it fails, the `git commit` is canceled. This is often used to make sure
that the changes to your code match a particular style, or that there are no
code linting errors.

For example, if you want that `git commit` checks if your code matches the PEP8 specification,
you can configure a git flake8 pre-commit hook:

```yaml
# file: .pre-commit-config.yaml
# see: https://flake8.pycqa.org/en/latest/user/using-hooks.html
repos:
  - repo: https://gitlab.com/pycqa/flake8
    rev: '3.7.9'
    hooks:
    -   id: flake8

```
This file specifies a hook that will be triggered automatically before each `git commit`,
in this case, it specifies a flake8 using version `3.7.9`.

Before you can see any change, first you should install `pre-commit` library. 
One way to do it is using `pip` or `conda`:

```sh
pip install pre-commit

# or

conda install -c conda-forge pre-commit
```

Now, you can install your pre-commit hook using `pre-commit install`, and it will create the hook based on
the file `.pre-commit-config.yaml`.

Before each `git commit` command, in this case, git will run `flake8` and, if it fails, the `commit` will be canceled.


## What git pre-commit hook should I use?

The git pre-commit hook you should use, depends on the project needs or the team needs.
Some pre-commit hooks you can find useful would be:

- [flake8](https://flake8.pycqa.org/en/latest/user/using-hooks.html)
- [mypy](https://github.com/pre-commit/mirrors-mypy)
- [black](https://black.readthedocs.io/en/stable/version_control_integration.html)
- [isort](https://github.com/pre-commit/mirrors-isort)

If you want more information about `pre-commit`, check out its [documentation](https://pre-commit.com/).
