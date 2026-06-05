# A guide for first-time reviewers

Thank you for taking the time to review a package for pyOpenSci! This supplement to the [main reviewer guide](https://www.pyopensci.org/software-peer-review/how-to/reviewer-guide.html) covers three topics — linting, documentation, and Sphinx — that first-time reviewers often find unfamiliar. You don't need to be an expert in any of these areas to give a useful review. We welcome reviewers from a diversity of backgrounds and with varying levels of Python experience.

---

## Linting and code style

Checking for consistent, readable code.

A linter is a tool that automatically scans source code for style issues, formatting inconsistencies, and common errors — without running the code. Think of it as a spell-checker for Python. pyOpenSci asks that packages follow standard [PEP 8](https://peps.python.org/pep-0008/) formatting rules as closely as possible, though we don't require a specific tool to enforce this. What we look for is consistency and readability across the codebase.

> **Why this matters**
> Consistent style makes code easier to read and maintain for the whole community. Linters also catch real bugs — undefined variables, unused imports, and unreachable code are all things they flag. You can read more about pyOpenSci's expectations in the [packaging guide's code style section](https://www.pyopensci.org/python-package-guide/package-structure-code/code-style-linting-format.html).

### Common tools you'll see in pyOpenSci packages

- **ruff** — A fast, modern linter and formatter gaining wide adoption in the scientific Python community. ([docs.astral.sh/ruff](https://docs.astral.sh/ruff/))
- **flake8** — Checks PEP 8 rules and common errors. Long-established and still widely used. ([flake8.pycqa.org](https://flake8.pycqa.org/))
- **black** — An opinionated auto-formatter. If a project uses black, formatting style is non-negotiable. ([black.readthedocs.io](https://black.readthedocs.io/))
- **pre-commit** — Runs linters automatically before each commit. A good sign a project takes code quality seriously. ([pre-commit.com](https://pre-commit.com/))

### What to look for as a reviewer

As a reviewer, you don't need to run the linter yourself. Here's what to check:

- Does the repo include a linting config? Look for `pyproject.toml`, `.flake8`, or `ruff.toml`.
- Does CI (GitHub Actions or similar) run the linter automatically on pull requests?
- Is the same linting tool used consistently across the whole project?
- Are there obvious style issues — very long lines, inconsistent spacing, or imports out of order?

> **Keep in mind**
> pyOpenSci does not require a specific linting tool — just consistency and readability. If a package uses a non-standard tool, that's fine as long as it works and is clearly configured. You can flag it as a question rather than a blocker.

### Example configuration

```toml
# Example: ruff config in pyproject.toml
[tool.ruff]
line-length = 88
select = ["E", "F", "W"]
```

```yaml
# Example: pre-commit hook running ruff
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff
```

---

## Documentation

Docstrings, READMEs, and user-facing guides.

Documentation is as important to the success of a Python open source package as the code itself. If users can't understand how to use a package in their workflows, they won't use it. In the pyOpenSci review, we look for documentation that supports both new users and potential contributors. You can read pyOpenSci's full documentation expectations in the [packaging guide's documentation section](https://www.pyopensci.org/python-package-guide/documentation/index.html).

### Levels of documentation to evaluate

- **README** — Is there a clear description of what the package does, who it's for, and how to install it? This is often the first thing a user encounters.
- **Installation instructions** — Can a new user install and run the package without asking for help? Try following the instructions yourself.
- **Docstrings** — Do all public functions, classes, and methods have docstrings that describe what they do, their parameters, and their return values?
- **Tutorials or vignettes** — Are there worked examples showing the package being used on a realistic problem? These are especially important for scientific tools.
- **API reference** — Is there documentation listing all public functions and classes, ideally auto-generated from the docstrings?
- **Contributing guide** — Is there guidance for potential contributors on how to submit bug reports, fixes, or new features?

> **Docstring formats**
> Python docstrings can be written in different styles — the most common in scientific Python are [NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html) and [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). The style used is less important than whether a consistent style is used throughout and whether the content is accurate and complete.

### Example: NumPy-style docstring

```python
# NumPy-style docstring — common in scientific Python
def calculate_ndvi(red, nir):
    """
    Calculate the Normalized Difference Vegetation Index.

    Parameters
    ----------
    red : array-like
        Red band reflectance values.
    nir : array-like
        Near-infrared band reflectance values.

    Returns
    -------
    ndarray
        NDVI values in the range [-1, 1].
    """
```

pyOpenSci also recommends that documentation follow the principle of *multiple points of entry* — each page of documentation should make sense on its own, because any page may be the first thing a user encounters.

### Further reading

- [User-facing documentation guide](https://www.pyopensci.org/python-package-guide/documentation/write-user-documentation/get-started.html) — pyOpenSci packaging guide
- [NumPy docstring format](https://numpydoc.readthedocs.io/en/latest/format.html) — numpydoc documentation
- [Google docstring format](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) — Google Python style guide

---

## Sphinx

Building and hosting documentation.

Sphinx is the most widely used tool in the scientific Python ecosystem for turning docstrings and written guides into a polished documentation website. If you've browsed docs on *readthedocs.io*, you've likely seen Sphinx output. While pyOpenSci doesn't require Sphinx — tools like [MkDocs](https://www.mkdocs.org/) are also acceptable — it's by far the most common choice. You can read more in the [pyOpenSci Sphinx guide](https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/sphinx-python-package-documentation-tools.html).

### Key Sphinx concepts

- **conf.py** — The main config file. Sets the theme, extensions, and project metadata. Lives in the `docs/` folder.
- **autodoc / autoapi** — Extensions that pull docstrings directly from source code so the API reference stays in sync automatically.
- **MyST parser** — An extension that lets authors write Sphinx docs in Markdown instead of reStructuredText (RST). Increasingly common. ([myst-parser.readthedocs.io](https://myst-parser.readthedocs.io/))
- **Read the Docs** — A hosting service that builds and deploys Sphinx docs automatically on each commit. Look for a `.readthedocs.yaml` in the repo root. ([readthedocs.org](https://readthedocs.org/))

### What to look for as a reviewer

As a reviewer you won't need to build the docs locally. Here's what to check:

- Is there a `docs/` folder with a `conf.py` and at least one index file?
- Does the project have a live documentation site linked from the README or repository?
- Does the live site render without broken pages, missing API entries, or obvious build errors?
- Is `sphinx.ext.autodoc` or `autoapi` used so the API reference is generated from docstrings?
- Are CI build logs free of Sphinx warnings about broken cross-references or missing docstrings?

> **Common issue to flag**
> If a public function appears in the source code but is missing from the API docs site, it usually means the docstring is absent or the function isn't included in the `autodoc` directives. This is worth raising as a review comment — it's a common oversight and easy for the author to fix.

### Example configuration

```python
# A minimal docs/conf.py
extensions = [
    "sphinx.ext.autodoc",   # pulls docstrings into the API reference
    "sphinx.ext.napoleon",  # supports NumPy and Google style docstrings
    "myst_parser",          # lets you write docs in Markdown
]
html_theme = "pydata_sphinx_theme"
```

### Further reading

- [Using Sphinx to build Python package documentation](https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/sphinx-python-package-documentation-tools.html) — pyOpenSci packaging guide
- [Tools to build and host your documentation](https://www.pyopensci.org/python-package-guide/documentation/hosting-tools/intro.html) — pyOpenSci packaging guide
- [Sphinx documentation](https://www.sphinx-doc.org/en/master/) — sphinx-doc.org
- [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/) — an alternative to autodoc for generating API docs
