# Guide for Reviewers

```{epigraph}
Thank you for taking the time to review a package for pyOpenSci and for contributing
to making open source scientific software easier to use by the community! If you
have any questions about the review process, feel free to reach out to one of
our editors or to post a question on our [discourse forum](https://pyopensci.discourse.group/).
```

Please be respectful and kind to the authors in your reviews. Our
[code of conduct](https://www.pyopensci.org/governance/CODE_OF_CONDUCT.html) is mandatory for everyone involved in our
review process.

## A guide for new reviewers

Thank you for considering reviewing for pyOpenSci. We welcome reviewers
from a diversity of background and with varying levels of Python technical
expertise.

Some of the basic things that we look for in a review include:

* Familiarity with using the Python programming language.
* Ability to evaluate a Python package for usability and documentation quality.
* Ability to provide a technical review of Python package structure and code quality / approach to solving the problems that the package seeks to address.

We like to have a mix of technical and usability focus in our reviews so it's ok if you don't have all of the above skills!

```{admonition} New to package review? We offer mentorship!
:class: note

If you are interested in peer review but have never reviewed before,
we offer a mentorship program where we will pair you up with someone
who has more experience reviewing code. From this experience you can
learn more and empower yourself with code review skills. Software review skills
are generally useful in data science, so they are skills worth investing in!
```

## Get Started With Your Review
As a new reviewer you should start by installing the package that you are
reviewing locally to test it out.

To install the package, you can either:

* fork the package repository and install it in
development/ editable mode `pip install -e .`
* or you can install it directly from `pip` or `conda-forge`.

```{important}
Be sure
that the version that you are reviewing aligns with the version
submitted by the author. The package version can
be found at the top of the review issue. In the example below you can
see that `pyrolite` version 0.2.5
was submitted for review.

That is the version that you should install!

```

Example header of a peer review submission issue on GitHub:

```
Submitting Author: Name (@morganjwilliams)
Package Name: pyrolite
One-Line Description of Package: A set of tools for getting the most from your geochemical data.
Repository Link: https://github.com/morganjwilliams/pyrolite
Version submitted: 0.2.5
Editor: @lwasser
```

### General Guidelines For Reviewing A Python Package for PyOpenSci

```{note}
If you are submitting a review, we appreciate submission within 3 weeks of
accepting a review. Please contact the editor directly or in the submission
thread to inform them about possible delays.
```

To review a package, please begin by copying our
review template (see below) and using it as a
high-level checklist.

```{include} ../appendices/review-template.md
```

### Other review guidelines to consider

In addition to checking off the minimum criteria specified
in the review template, please also provide general comments addressing the following:

- Is the code well written and efficient?
  * Are there improvements that could be made to the code style?
  * Is there code duplication in the package that should be reduced?
  * Are there performance improvements that could be made?
  * Are functions and arguments named to work together to form a common, logical programming API that is easy to read, and autocomplete?

* Does the package comply with the pyOpenSci packaging guide](https://www.pyopensci.org/python-package-guide)?

* Are there user interface improvements that could be made?
* Is the documentation (installation instructions/vignettes/examples/demos) clear and sufficient?
    * Does the documentation use the principle of *multiple points of entry* i.e. takes into account the fact that any piece of documentation may be the first encounter the user has with the package and/or the tool/data it wraps?

If you have your own relevant data/problem that you could use the package to solve, work through it with the package. You may find rough edges and use-cases the author didn't think about.

## Submit your review
* When your review is complete, paste it as a comment into the package software-review issue.
* Additional comments are welcome in the same issue. We hope that package reviews will work as an ongoing conversation with the authors as opposed to a single round of reviews typical of academic manuscripts.
* You may also submit issues or pull requests directly to the package repo if you choose, but if you do, please comment about them and link to them in the software-review repo comment thread so we have a centralized record and text of your review.
* Please include an estimate of how many hours you spent on your review afterwards.

## Review follow-Up
Authors should respond within 2 weeks with their changes to the package in response to your review. At this stage, we ask that you respond as to whether the changes sufficiently address any issues raised in your review. We encourage ongoing discussion between package authors and reviewers, and you may ask editors to clarify issues in the review thread as well.


### Examples of Past pyOpenSci Reviews

It might be helpful to consult some previous reviews and read about the
experiences of other reviewers. In general you can find submission threads of
onboarded packages here. Here are a few chosen examples of reviews (note that
your reviews do not need to be as long as these examples):

* `MovingPandas` [review 1](https://github.com/pyOpenSci/software-review/issues/18#issuecomment-579520816) and [review 2](https://github.com/pyOpenSci/software-review/issues/18#issuecomment-581752433)

* `Pandera` [review 1](https://github.com/pyOpenSci/software-review/issues/12#issuecomment-527622205) and [review 2](https://github.com/pyOpenSci/software-review/issues/12#issuecomment-531491008)

## Lessons Learned from rOpenSci
You can read blog posts written by reviewers about their experiences [via this link](https://ropensci.org/tags/reviewer/). In particular, in [this blog post by Mara Averick](https://ropensci.org/blog/2017/08/22/first-package-review/) read about the "naive user" role a reviewer can take to provide useful feedback even without being experts of the package's topic or implementation, by asking themselves _"What did I think this thing would do? Does it do it? What are things that scare me off?"_. In [another blog post](https://ropensci.org/blog/2017/09/08/first-review-experiences/) Verena Haunschmid explains how she alternated between using the package and checking its code.

As both a former reviewer and package author [Adam Sparks](https://adamhsparks.com) [wrote this](https://twitter.com/adamhsparks/status/898132036451303425) "[write] a good critique of the package structure
and best coding practices. If you know how to do something better, tell
me. It’s easy to miss documentation opportunities as a developer, as a
reviewer, you have a different view. You’re a user that can give
feedback. What’s not clear in the package? How can it be made more
clear? If you’re using it for the first time, is it easy? Do you know
another `R` package that maybe I should be using? Or is there one I’m
using that perhaps I shouldn’t be? If you can contribute to the package,
offer."

### Feedback on the pyOpenSci open peer review process

We welcome any feedback and/or questions about the review process! We encourage you to post any issues, feedback or questions in our [Discourse forum](https://pyopensci.discourse.group/c/review-process/7).
