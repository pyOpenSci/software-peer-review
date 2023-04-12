## Peer Review Template

```
## Package Review

*Please check off boxes as applicable, and elaborate in comments below. Your review is not limited to these topics, as described in the reviewer guide*

- [ ] As the reviewer I confirm that there are no conflicts of interest for me to review this work (If you are unsure whether you are in conflict, please speak to your editor _before_ starting your review).

#### Documentation

The package includes all the following forms of documentation:

- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience in README.
- [ ] **Installation instructions:** for the development version of the package and any non-standard dependencies in README.
- [ ] **Vignette(s)** demonstrating major functionality that runs successfully locally.
- [ ] **Function Documentation:** for all user-facing functions.
- [ ] **Examples** for all user-facing functions.
- [ ] **Community guidelines** including contribution guidelines in the README or CONTRIBUTING.
- [ ] **Metadata** including author(s), author e-mail(s), a url, and any other relevant metadata e.g., in a `pyproject.toml` file or elsewhere.

Readme file  requirements
The package meets the readme requirements below:

- [ ] Package has a README.md file in the root directory.

The README should include, from top to bottom:

- [ ] The package name
- [ ] Badges for:
    - [ ] Continuous integration and test coverage,
    - [ ] Docs building (if you have a documentation website),
    - [ ] A [repostatus.org](https://www.repostatus.org/) badge,
    - [ ] Python versions supported,
    - [ ] Current package version (on PyPI / Conda).

*NOTE: If the README has many more badges, you might want to consider using a table for badges: [see this example](https://github.com/ropensci/drake). Such a table should be more wide than high. (Note that the a badge for pyOpenSci peer-review will be provided upon acceptance.)*

- [ ] Short description of package goals.
- [ ] Package installation instructions
- [ ] Any additional setup required to use the package (authentication tokens, etc.)
- [ ] Descriptive links to all vignettes. If the package is small, there may only be a need for one vignette which could be placed in the README.md file.
    - [ ] Brief demonstration of package usage (as it makes sense - links to vignettes could also suffice here if package description is clear)
- [ ] Link to your documentation website.
- [ ] If applicable, how the package compares to other similar packages and/or how it relates to other packages in the scientific ecosystem.
- [ ] Citation information

#### Usability
Reviewers are encouraged to submit suggestions (or pull requests) that will improve the usability of the package as a whole.
Package structure should follow general community best-practices. In general please consider whether:

- [ ] Package documentation is clear and easy to find and use.
- [ ] The need for the package is clear
- [ ] All functions have documentation and associated examples for use
- [ ] The package is easy to install


#### Functionality

- [ ] **Installation:** Installation succeeds as documented.
- [ ] **Functionality:** Any functional claims of the software been confirmed.
- [ ] **Performance:** Any performance claims of the software been confirmed.
- [ ] **Automated tests:**
  - [ ] All tests pass on the reviewer's local machine for the package version submitted by the author. Ideally this should be a tagged version making it easy for reviewers to install.
  - [ ] Tests cover essential functions of the package and a reasonable range of inputs and conditions.
- [ ] **Continuous Integration:** Has continuous integration setup (We suggest using Github actions but any CI platform is acceptable for review)
- [ ] **Packaging guidelines**: The package conforms to the pyOpenSci [packaging guidelines](https://www.pyopensci.org/python-package-guide).
    A few notable highlights to look at:
    - [ ] Package supports modern versions of Python and not [End of life versions](https://endoflife.date/python).
    - [ ] Code format is standard throughout package and follows PEP 8 guidelines (CI tests for linting pass)

#### For packages also submitting to JOSS

- [ ] The package has an **obvious research application** according to JOSS's definition in their [submission requirements](http://joss.theoj.org/about#submission_requirements).

*Note:* Be sure to check this carefully, as JOSS's submission requirements and scope differ from pyOpenSci's in terms of what types of packages are accepted.

The package contains a `paper.md` matching [JOSS's requirements](http://joss.theoj.org/about#paper_structure) with:

- [ ] **A short summary** describing the high-level functionality of the software
- [ ] **Authors:** A list of authors with their affiliations
- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience.
- [ ] **References:** With DOIs for all those that have one (e.g. papers, datasets, software).

#### Final approval (post-review)

- [ ] **The author has responded to my review and made changes to my satisfaction. I recommend approving this package.**

Estimated hours spent reviewing:

---

#### Review Comments


```
