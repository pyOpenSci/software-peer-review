# Using git pre-commit hook

Git pre-commit hook is an useful tool that checks your code automatically when you run a `git commit` and,
if it fails, the `git commit` is canceled.

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

