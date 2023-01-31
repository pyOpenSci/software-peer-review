# How pyOpenSci's open software peer review works


## Who submits packages and who runs the reviews

pyOpenSci's [suite of packages](https://www.pyopensci.org/python-packages/) are
contributed by community members with a great diversity of skills and backgrounds. This diversity
of developer backgrounds enables us to vet and promote a broad ecosystem of
high quality tools
that supports scientists across domains with a suite of different data
types and structures.

### Who reviews pyOpenSci packages?

Our peer review process is run by volunteer members of the Python scientific
community:

* Editors manage incoming package submissions. Editors also ensure
that package reviews move through the review process efficiently;
* Authors create, submit and improve their package;
* Reviewers, two per submission, examine the software code and user experience.

Our [governance documentation](https://www.pyopensci.org/governance) clarifies
the various roles that support running our peer review process.

## Software reviews are contained within [GitHub](https://www.github.com/pyOpenSci) issues

Our entire peer review process occurs on GitHub in the
[pyOpenSci software-review repository](https://www.github.com/pyopensci/software-review).

We use GitHub because:

* It is free to create an account,
* Anyone can read the review discussion without an account, making the process entirely open,
* It facilitates collaboration and supports the community around a package,
* It facilitates an open discussion between reviewers, package maintainers and the pyOpenSci volunteers,
* Numerous packages store their code bases on GitHub.

### We use GitHub issue templates and labels to organize the review steps

* We use GitHub issue templates as submission templates for new reviews and pre-submission review questions.
* We label issues to track every step of the package submission and review progress (e.g. [1/initial-editor-checks, 2/reviewers-needed, 6/pyopensci-approved](https://github.com/pyOpenSci/software-review/labels)).

```{note}
[Click here to read the review thread from a December 2022
pyOpenSci pre-submission issue.](https://github.com/pyOpenSci/software-review/issues/65) Note the conversational
tone of the pre-review. In this case the package was improved
before the formal review even began.

In the actual review process, two external reviews are important milestones. The editor will also provide the author with some feedback.
```

For more detailed overview of the peer review process, [check out our process
timeline document here.](review-timeline)
