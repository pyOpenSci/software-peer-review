# Guide for Reviewers

Please be respectful and kind to the authors in your reviews. Our [code of conduct](peer_review/coc) is mandatory for everyone involved in our review process.

## Preparing Your Review

### General Guidelines

When you are assigned to review a package, you are expected to submit your review within 3 weeks. Please contact the editor directly or in the submission thread to inform them about possible delays. 

To review a package, please begin by copying our [review template](appendices/templates#review-template) and using it as a high-level checklist. In addition to checking off the minimum criteria, we ask that you provide general comments addressing the following:
- Does the code comply with general principles in the [Mozilla reviewing guide](https://mozillascience.github.io/codeReview/review.html)?
- Does the package comply with the [pyOpenSci packaging guide](packaging/packaging_guide)?
- Are there improvements that could be made to the code style?
- Is there code duplication in the package that should be reduced?
- Are there user interface improvements that could be made?
- Are there performance improvements that could be made?
- Is the documentation (installation instructions/vignettes/examples/demos) clear and sufficient? Does it use the principle of *multiple points of entry* i.e. takes into account the fact that any piece of documentation may be the first encounter the user has with the package and/or the tool/data it wraps?
- Were functions and arguments named to work together to form a common, logical programming API that is easy to read, and autocomplete?
- If you have your own relevant data/problem, work through it with the package. You may find rough edges and use-cases the author didn't think about.

### Examples of Past Reviews

**Note**: Because pyOpenSci is new, we do not have examples from our review process yet. For now, this section is taken from the excellent [rOpenSci guidebook](https://ropensci.github.io/dev_guide/reviewerguide.html#experience-from-past-reviewers). Our review process is based on theirs. We will update with pyOpenSci-specific information in the future.

It might be helpful to consult some previous reviews and read about the experiences of other reviewers. In general you can find submission threads of onboarded packages here. Here are a few chosen examples of reviews (note that your reviews do not need to be as long as these examples):


* `rtika` [review 1](https://github.com/ropensci/software-review/issues/191#issuecomment-367166658) and [review 2](https://github.com/ropensci/software-review/issues/191#issuecomment-368254623)

* `NLMR` [review 1](https://github.com/ropensci/software-review/issues/188#issuecomment-368042693) and [review 2](https://github.com/ropensci/software-review/issues/188#issuecomment-369310831)

* `bowerbird` [pre-review comment](https://github.com/ropensci/software-review/issues/139#issuecomment-322713737), [review 1](https://github.com/ropensci/software-review/issues/139#issuecomment-342380870), [review 2](https://github.com/ropensci/software-review/issues/139#issuecomment-342724843).

* `rusda` [review](https://github.com/ropensci/software-review/issues/18#issuecomment-120445737) (from before we had a review template)

You can read blog posts written by reviewers about their experiences [via this link](https://ropensci.org/tags/reviewer/). In particular, in [this blog post by Mara Averick](https://ropensci.org/blog/2017/08/22/first-package-review/) read about the "naive user" role a reviewer can take to provide useful feedback even without being experts of the package's topic or implementation, by asking themselves _"What did I think this thing would do? Does it do it? What are things that scare me off?"_. In [another blog post](https://ropensci.org/blog/2017/09/08/first-review-experiences/) Verena Haunschmid explains how she alternated between using the package and checking its code.

As both a former reviewer and package author [Adam Sparks](https://adamhsparks.github.io/) [wrote this](https://twitter.com/adamhsparks/status/898132036451303425) "[write] a good critique of the package structure and best coding practices. If you know how to do something better, tell me. It’s easy to miss documentation opportunities as a developer, as a reviewer, you have a different view. You’re a user that can give feedback. What’s not clear in the package? How can it be made more clear? If you’re using it for the first time, is it easy? Do you know another R package that maybe I should be using? Or is there one I’m using that perhaps I shouldn’t be? If you can contribute to the package, offer."


### Feedback on the Process

We welcome any feedback and/or questions about the review process! We encourage you to open an issue on our [governance repository](https://github.com/pyOpenSci/governance).

## Submitting the Review
- When your review is complete, paste it as a comment into the package software-review issue.
- Additional comments are welcome in the same issue. We hope that package reviews will work as an ongoing conversation with the authors as opposed to a single round of reviews typical of academic manuscripts.
- You may also submit issues or pull requests directly to the package repo if you choose, but if you do, please comment about them and link to them in the software-review repo comment thread so we have a centralized record and text of your review.
- Please include an estimate of how many hours you spent on your review afterwards.

## Review Follow-Up
Authors should respond within 2 weeks with their changes to the package in response to your review.  At this stage, we ask that you respond as to whether the changes sufficiently address any issues raised in your review. We encourage ongoing discussion between package authors and reviewers, and you may ask editors to clarify issues in the review thread as well.

