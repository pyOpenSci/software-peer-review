# Appendix: Templates

These are templates to be used by editors and reviewers. When a package is submitted, the assigned editor fills out the Editor's Template and posts it in the submission's issue thread on GitHub.

## Editor's Template

```
## Editor checks:

- [ ] **Fit**: The package meets criteria for [fit](https://www.pyopensci.org/contributing-guide/about-peer-review/aims-and-scope.html#package-categories) and [overlap](https://www.pyopensci.org/contributing-guide/about-peer-review/aims-and-scope.html#package-overlap).
- [ ] **Automated tests:** Package has a testing suite and is tested via Travis-CI or another CI service.
- [ ] **License:** The package has an OSI accepted license
- [ ] **Repository:** The repository link resolves correctly
- [ ] **Archive** (JOSS only, may be post-review): The repository DOI resolves correctly
- [ ] **Version** (JOSS only, may be post-review): Does the release version given match the GitHub release (v1.0.0)?

---

## Editor comments

---

Reviewers:
Due date:
```

## Review Template

```
## Package Review

*Please check off boxes as applicable, and elaborate in comments below. Your review is not limited to these topics, as described in the reviewer guide*

- [ ] As the reviewer I confirm that there are no conflicts of interest for me to review this work (If you are unsure whether you are in conflict, please speak to your editor _before_ starting your review).

#### Documentation

The package includes all the following forms of documentation:

- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience in README
- [ ] **Installation instructions:** for the development version of package and any non-standard dependencies in README
- [ ] **Vignette(s)** demonstrating major functionality that runs successfully locally
- [ ] **Function Documentation:** for all user-facing functions
- [ ] **Examples** for all user-facing functions
- [ ] **Community guidelines** including contribution guidelines in the README or CONTRIBUTING.
- [ ] **Metadata** including author(s), author e-mail(s), a url, and any other relevant metadata e.g., in a `setup.py` file or elsewhere.

Readme requirements
The package meets the readme requirements below:

- [ ] Package has a README.md file in the root directory.

The README should include, from top to bottom:

- [ ] The package name
- [ ] Badges for continuous integration and test coverage, a repostatus.org badge, and any other badges. If the README has many more badges, you might want to consider using a table for badges: [see this example](https://github.com/ropensci/drake). Such a table should be more wide than high. (Note that the badge for pyOpenSci peer-review will be provided upon acceptance.)
- [ ] Short description of goals of package, with descriptive links to all vignettes (rendered, i.e. readable, cf the documentation website section) unless the package is small and there’s only one vignette repeating the README.
- [ ] Installation instructions
- [ ] Any additional setup required (authentication tokens, etc)
- [ ] Brief demonstration usage
- [ ] Direction to more detailed documentation (e.g. your documentation files or website).
- [ ] If applicable, how the package compares to other similar packages and/or how it relates to other packages
- [ ] Citation information

#### Usability
Reviewers are encouraged to submit suggestions (or pull requests) that will improve the usability of the package as a whole.
Package structure should follow general community best-practices. In general please consider:

- [ ] The documentation is easy to find and understand
- [ ] The need for the package is clear
- [ ] All functions have documentation and associated examples for use


#### Functionality

- [ ] **Installation:** Installation succeeds as documented.
- [ ] **Functionality:** Any functional claims of the software been confirmed.
- [ ] **Performance:** Any performance claims of the software been confirmed.
- [ ] **Automated tests:** Tests cover essential functions of the package and a reasonable range of inputs and conditions. All tests pass on the local machine.
- [ ] **Continuous Integration:** Has continuous integration, such as Travis CI, AppVeyor, CircleCI, and/or others.
- [ ] **Packaging guidelines**: The package conforms to the pyOpenSci [packaging guidelines](https://www.pyopensci.org/contributing-guide/authoring/index.html#packaging-guide).

#### For packages co-submitting to JOSS

- [ ] The package has an **obvious research application** according to JOSS's definition in their [submission requirements](http://joss.theoj.org/about#submission_requirements).

*Note:* Be sure to check this carefully, as JOSS's submission requirements and scope differ from pyOpenSci's in terms of what types of packages are accepted.

The package contains a `paper.md` matching [JOSS's requirements](http://joss.theoj.org/about#paper_structure) with:

- [ ] **A short summary** describing the high-level functionality of the software
- [ ] **Authors:** A list of authors with their affiliations
- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience.
- [ ] **References:** with DOIs for all those that have one (e.g. papers, datasets, software).

#### Final approval (post-review)

- [ ] **The author has responded to my review and made changes to my satisfaction. I recommend approving this package.**

Estimated hours spent reviewing:

---

#### Review Comments


```

## Review Request Template

Editors may make use of the e-mail template below in recruiting reviewers:

```
Dear [REVIEWER],

Hi, this is [EDITOR]. [FRIENDLY BANTER]. I'm writing to ask if you would be willing to review a package for pyOpenSci. As you probably know, pyOpenSci conducts peer review of Python packages contributed to our collection in a manner similar to journals.

The package, [PACKAGE] by [AUTHOR(S)], does [FUNCTION]. You can find it on GitHub here: [REPO LINK]. We conduct our open review process via GitHub as well, here: [ONBOARDING ISSUE]

If you accept, note that we ask reviewers to complete reviews in three weeks. (We’ve found it takes a similar amount of time to review a package as an academic paper.)

Our [reviewers guide] details what we look for in a package review, and includes links to example reviews. Our standards are detailed in our [packaging guide], and we provide reviewer [template] for you to use. Please make sure you do not have a conflict of interest preventing you from reviewing this package. If you have questions or feedback, feel free to ask me.

{IF APPLICABLE: The authors have also chosen to jointly submit their package to the Journal of Open Source Software, so this package includes a short `paper.md` manuscript describing the software that we ask you include in your review.}

Are you able to review? If you can not, suggestions for alternate reviewers are always helpful. If I don't hear from you within a week, I will assume you are unable to
review at this time.

Thank you for your time.

Sincerely,

[EDITOR]
```

[reviewers guide]: https://www.pyopensci.org/contributing-guide/peer-review-guides/reviewer-guide.html
[packaging guide]: https://www.pyopensci.org/contributing-guide/authoring/index.html#packaging-guide
[template]: https://www.pyopensci.org/contributing-guide/appendices/templates.html#review-template


## Editor Approval Comment Template
```
----------------------------------------------
🎉 <package-name-here> has been approved by pyOpenSci! Thank you <maintainer-name-here> for submitting <package-name> and many thanks to <reviewer-names-here> for reviewing this package! 😸  

There are a few things left to do to wrap up this submission:
- [ ] Add the badge for pyOpenSci peer-review to the README.md of <package-name-here>. The badge should be `[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/issue-number)`
- [ ] Add <package-name> to the pyOpenSci website. <maintainer-name>, please open a pr to update [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/packages.yml): to add your package and name to the list of contributors
- [ ] <reviewers-and-maintainers> if you have time and are open to being listed on our website, please add yourselves to [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/contributors.yml) via a pr so we can list you on our website as contributors!

<IF JOSS SUBMISSION>
This package is going to move on to JOSS for review. I believe @arfon will ask you to implement the items below but let's let him chime in here first!
- [ ] Activate Zenodo watching the repo
- [ ] Tag and create a release so as to create a Zenodo version and DOI
- [ ] Submit to JOSS using the Zenodo DOI. We will tag it for expedited review.

<IF JOSS SUBMISSION/>

All -- if you have any feedback for us about the review process please feel free to share it here. We are always looking to improve our process and our documentation in the [contributing-guide](https://www.pyopensci.org/contributing-guide). We have also been updating our documentation to improve the process so all feedback is appreciated!
```

## Generic new member template

A template for inviting others to join the pyOpenSci community calls and otherwise
get engaged.

```
< short greeting />

I'm writing to see if you'd be interested in participating with pyOpenSci, a new community around improving the quality of software in the scientific python stack.

pyOpenSci provides resources, mentoring, and documentation for making scientific python packages more useful and maintainable. It builds off of the successful rOpenSci model, with a Python flavor. It primarily coordinates a review process by which experienced developers in the scientific python ecosystem can provide feedback and suggestions to other (usually fairly small) packages.

You've been in the scientific Python community for some time now, and I think you'd be a great part of the pyOpenSci community. Would you be interested in joining us? Participation can be as small or large as you wish - for example, you could submit your own package for review in pyOpenSci, offer to be a reviewer of someone else's package, or begin attending pyOpenSci planning meetings as we build and refine our processes. We'd just be happy to have you around :-)

< short goodbye />
```
