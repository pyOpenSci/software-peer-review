# Guide for Authors

Before submitting your project for review with pyOpenSci, make sure that it
adheres to the standards and guidelines put forward in the [authoring guide](../authoring/index).

## Presubmission Inquiries
If you are unsure of whether your package fits within
[pyOpenSci's scope](../open-source-software-peer-review/aims-and-scope), submit
a [presubmission inquiry issue on the software-review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
repository. After you submit an inquiry, a pyOpenSci editor will provide you with
input regarding the fit of your package within the pyOpenSci ecosystem.

## Submission for Peer Review
To request peer review, start a new issue in the
[pyOpenSci/software-review](https://github.com/pyOpenSci/software-review)
repository and fill out the "Submit Software for Review" issue template. For
more information on the process and timeline for review, see
our [section on the review process](../open-source-software-peer-review/intro).

### Journal of Open Source Software (JOSS) Submission

PyOpenSci has a partnership with JOSS where our review is accepted by JOSS by
default if the package fits into the JOSS scope.

- When you submit your package for pyOpenSci review, you can opt to include a submission to JOSS after passing pyOpenSci review. In this case, your package will evaluated by JOSS through the pyOpenSci review
- To complete the JOSS submission, you will also need to craft a **paper.md** file describing the package following JOSS' standards (see below). More detail on the requirements for JOSS can be found on [their website](https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain).
- If you choose to opt into the pyOpenSci / JOSS partnership in your review, do NOT submit your package to JOSS separately. A PyOpenSci editor fill facilitate that step once you complete your review.


```{admonition} **Important**
 Acceptance to pyOpenSci does not guarantee acceptance to JOSS. In particular, JOSS doesn't accept the full variety of packages that are in scope for pyOpenSci. For example, thin API wrappers fall within  [pyOpenSci's scope](../open-source-software-peer-review/aims-and-scope) but are usually not accepted by JOSS. Be sure to review JOSS's [submission requirements](https://joss.readthedocs.io/en/latest/submitting.html#submission-requirements) before writing up a paper about your package.
```


## Presubmission Questions

If your package does not clearly fit within one of the categories outlined in
our [scope](../open-source-software-peer-review/aims-and-scope), create
a [Presubmission Inquiry issue](https://github.com/pyOpenSci/software-review/issues/new/choose)
in our software-review repo. You can use the same issue template if you have
other questions. An editor will get back to you in a few days to answer your
questions and to help determine the fit.

## Package Prep Help

If you would like help preparing your package for review, create a [Help Request issue](https://github.com/pyOpenSci/software-review/issues/new/choose) in the software-review repo. We can assign someone to help you prep your code and add things like testing, documentation, and/or continuous integration. We're happy to help. Also check out the rest of our [Packaging Guide](../authoring/overview), which may help answer some of your questions about packaging your code.
