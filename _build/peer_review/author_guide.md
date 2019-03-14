---
redirect_from:
  - "/peer-review/author-guide"
title: 'Guide for Authors'
prev_page:
  url: /peer_review/peer_review_proc
  title: 'Review Process and Guidelines'
next_page:
  url: /peer_review/reviewer_guide
  title: 'Guide for Reviewers'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Guide for Authors

## Code Style

pyOpenSci encourages authors to consult [PEP 8](https://www.python.org/dev/peps/pep-0008/) for information on how to style your code.

## Packaging Guide

The [first section of this guidebook](../packaging/packaging_guide) has info for creating and packaging your Python project for review and release. The guide also includes info on the basic requirements for pyOpenSci: testing, continuous integration, documentation, etc.

We also have a [section](../maintenance/release) about releasing your package on PyPI, but we encourage you to wait until after the pyOpenSci review process has finished before uploading to PyPI. This makes it easier to incorporate changes/suggestions from the reviews.

PyPI also has a [short tutorial](https://packaging.python.org/tutorials/packaging-projects/) on how to package a Python project for easy installation.  

## Presubmission 
If you are unsure if your package fits within pyOpenSci's [scope](aims_scope), you're encouraged to open a presubmission inquiry issue on the [software-review](https://github.com/pyOpenSci/software-review) repository.

## Submission for Peer Review
To request peer review, start a new issue in the [pyOpenSci/software-review](https://github.com/pyOpenSci/software-review) repository and fill out the "Submit Software for Review" issue template. For more information on the process and timeline for review, see our [section on the review process](peer_review_proc).

### JOSS Submission
- If you would like, your package can be submitted to the Journal of Open-Source Software (JOSS) after passing pyOpenSci review. In this case, the package will evaluated by JOSS based on the pyOpenSci review and the paper accompanying your package (see below).
- If you choose to have your package submitted to JOSS after review, it should include a paper.md file describing the package. More detail on JOSS’s requirements can be found at [their website](https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain).
- **Important note:** Acceptance to pyOpenSci does not guarantee acceptance to JOSS. In particular, JOSS doesn't accept all the types of packages that pyOpenSci does. For example, thin API wrappers fall within pyOpenSci's [scope](aims_scope) but are usually not accepted by JOSS. Be sure to review JOSS's [submission requirements](https://joss.readthedocs.io/en/latest/submitting.html#submission-requirements) before writing up a paper about your package.
- If you choose this option you should not submit your package to JOSS separately. 
