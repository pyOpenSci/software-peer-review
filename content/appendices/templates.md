# Appendix: Templates

These are templates to be used by editors and reviewers. When a package is submitted, the assigned editor fills out the Editor's Template and posts it in the submission's issue thread on GitHub.

## Editor's Template
```
### Editor checks:

- [ ] **Fit**: The package meets criteria for [fit](https://pyopensci.github.io/dev_guide/peer_review/aims_scope.html#package-categories) and [overlap](https://pyopensci.github.io/dev_guide/peer_review/aims_scope.html#package-categories).
- [ ] **Automated tests:** Package has a testing suite and is tested via Travis-CI or another CI service.
- [ ] **License:** The package has an OSI accepted license
- [ ] **Repository:** The repository link resolves correctly
- [ ] **Archive** (JOSS only, may be post-review): The repository DOI resolves correctly
- [ ] **Version** (JOSS only, may be post-review): Does the release version given match the GitHub release (v1.0.0)?

---

#### Editor comments

---

Reviewers:
Due date:
```


## Review Template
```
### Package Review

*Please check off boxes as applicable, and elaborate in comments below.  Your review is not limited to these topics, as described in the reviewer guide*

- [ ] As the reviewer I confirm that there are no conflicts of interest for me to review this work (If you are unsure whether you are in conflict, please speak to your editor _before_ starting your review).

#### Documentation

The package includes all the following forms of documentation:

- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience in README
- [ ] **Installation instructions:** for the development version of package and any non-standard dependencies in README
- [ ] **Vignette(s)** demonstrating major functionality that runs successfully locally
- [ ] **Function Documentation:** for all exported functions in R help
- [ ] **Examples** for all exported functions in R Help that run successfully locally
- [ ] **Community guidelines** including contribution guidelines in the README or CONTRIBUTING, and DESCRIPTION with `URL`, `BugReports` and `Maintainer`.

>##### For packages co-submitting to JOSS
>
>- [ ] The package has an **obvious research application** according to [JOSS's definition](http://joss.theoj.org/about#submission_requirements)
>
>The package contains a `paper.md` matching [JOSS's requirements](http://joss.theoj.org/about#paper_structure) with:
>
>- [ ] **A short summary** describing the high-level functionality of the software
>- [ ] **Authors:**  A list of authors with their affiliations
>- [ ] **A statement of need** clearly stating problems the software is designed to solve and its target audience.
>- [ ] **References:** with DOIs for all those that have one (e.g. papers, datasets, software).

#### Functionality

- [ ] **Installation:** Installation succeeds as documented.
- [ ] **Functionality:** Any functional claims of the software been confirmed.
- [ ] **Performance:** Any performance claims of the software been confirmed.
- [ ] **Automated tests:** Unit tests cover essential functions of the package and a reasonable range of inputs and conditions. All tests pass on the local machine.
- [ ] **Packaging guidelines**: The package conforms to the pyOpenSci packaging guidelines

#### Final approval (post-review)

- [ ] **The author has responded to my review and made changes to my satisfaction. I recommend approving this package.**

Estimated hours spent reviewing:

---

#### Review Comments


```

## Review Request Template

Editors may make use of the e-mail template below in recruiting reviewers:

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

[reviewers guide]: https://pyopensci.github.io/dev_guide/peer_review/reviewer_guide.html
[packaging guide]: https://pyopensci.github.io/dev_guide/packaging/packaging_guide.html
[template]: https://pyopensci.github.io/dev_guide/appendices/templates.html#review-template


## Approval Comment Template
```
Approved! Thanks <author(s) GitHub username(s)> for submitting and <reviewers' GithHub usernames> for your reviews! <optional: smiling cat emoji à la Scott>

To-dos:
- [ ] Transfer the repo to our "pyOpenSci" GitHub organization under "Settings" in your repo.  I have invited you to a team that should allow you to do so.  You'll be made admin once you do.
- [ ] Fix any links in badges for CI and coverage to point to the pyOpenSci URL. For Appveryor projects, you should still use your personal Appveyor account. After transfer of your repo to the "pyOpenSci" GitHub organization the badge should be `[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/pyOpenSci/pkgname?branch=master&svg=true)](https://ci.appveyor.com/project/individualaccount/pkgname)`.

<IF JOSS>
- [ ] Activate Zenodo watching the repo
- [ ] Tag and create a release so as to create a Zenodo version and DOI
- [ ] Submit to JOSS using the Zenodo DOI.  We will tag it for expedited review.
<IF JOSS/>

We've started putting together a gitbook with our best practice and tips, [this chapter](https://pyopensci.github.io/dev_guide/maintenance/maintenance_intro.html) starts the 3rd section that's about guidance for after onboarding. Please tell us what could be improved, the corresponding repo is [here](https://github.com/pyOpenSci/dev_guide).
```
