# pyOpenSci Review Guide for Python Open Source Package Authors

Are you considering submitting a package for review with pyOpenSci? You've 
come to the right place!

Below you will find the steps that you need to follow to submit a package 
to pyOpenSci for peer review. 

Before you begin this process, [please be sure to read the review process guidelines](../about-peer-review/policies-guidelines).

## 1. Do you plan to continue to maintain your package?
One of the goals of pyOpenSci is to maintain a curated list of 
community-approved, maintained and vetted tools that support open science workflows. 

As such we review packages that will be useful to the community
and maintained over time. While we understand that burnout is real,
and you may move on in the future to other projects, we ask that you commit
to maintaining your package for at least 1-2 years. 

If that maintenance commitment is too much, you might consider submitting 
your package to another Journal.

If you need to step from maintaining your package, please let us know
in advance. We will try to help you either.

* Find a new maintainer to take over your project or
* Sunset your package.

If the package is sunsetted we will remove it from our curated list 
of vetted tools. 

### Who should submit the package for review?

If you have a team of people maintaining your package, please be sure
that the submitting author is the person who "owns" or leads that maintenance. That person will become the long term point of contact 
for pyOpenSci.

```{note}
If your package is more of a tool to support a specific workflow that 
either may not be maintained long term or that may be so specific that 
it won't have a broad user base, you might consider submitting it 
directly to the Journal of Open Source Software (JOSS). 
```


## 2. Does Your Package Meet Packaging Requirements?
Before submitting your project for review with pyOpenSci, make sure that it
follows the standards and guidelines outlined in the 
[Python packaging guide](../authoring/index).

```{note}
**Package Prep Help - Can we actually support this now??**

If you would like help preparing your package for review, create 
a [Help Request issue](https://github.com/pyOpenSci/software-review/issues/new/choose) 
in the software-review repo. We can assign someone to help you prep your code 
and add things like testing, documentation, and/or continuous integration. We're 
happy to help. Also check out the rest of our [Packaging Guide](../authoring/overview), which may help answer some of your questions about packaging your code.
```

## 3. Is Your Package in Scope for pyOpenSci?
Next, check to see if your package falls into the scope of pyOpenSci. If you aren't 
sure about whether your package fits within pyOpenSci's scope (below), submit
a [presubmission inquiry issue on the software-review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
repository. After you submit an inquiry, a pyOpenSci editor will get back to you 
with input regarding the fit of your package for pyOpenSci review. This can take 
up to a week. 

```{include} ../scope.md
```

```{note} 
**Before you consider submitting to us please consider the following:**

1. Please be sure that you have time to devote to making changes to your 
package. You may get feedback from an editor and two reviewers. Changes could 
take time. Please consider this before submitting to us. You can read more about the timeline to make changes in our [peer review policies page](../about-peer-review/policies-guidelines).
2. Peer review is lead by a diverse group of volunteer editors and reviewers. 
Please be considerate when engaging with everyone online. 
```

## 4. Presubmission Questions

If your package does not clearly fit within one of the categories outlined in
our [scope](../about-peer-review/aims-and-scope), create
a [Presubmission Inquiry issue](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
in our software-review repo. You can use the same issue template if you have
other questions. An editor will get back to you in a few days to answer your
questions and to help determine the fit.

## 5. Submit Your Package for Peer Review
To submit your package for peer review, you can 
open an issue in our [pyopensci/software-review repo](https://github.com/pyOpenSci/software-review/issues/new/choose/issues/new/choose)
repository and fill out the [Submit Software for Review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=1%2Feditor-checks%2C+New+Submission%21&template=submit-software-for-review.md&title=) issue template. 

## 6. Editor in Chief Reviews Package for Scope and Minimal Infrastructure Criteria
Once the issue is opened, an editor will review your submission within 
**2 weeks** and respond with next steps. The editor may request that you make updates
to your package to meet minimal criteria before review. They also may reject your 
package if it does not fall within our scope. 

## 7. The Review Begins
If your package meets minimal criteria for being 
reviewed it may then be given to an editor with appropriate domain experience 
to run the review. That editor will assign 2-3 reviewers to review your 
package. Reviewers will be asked to provide review feedback  as comments on your 
issue within **3 weeks**. Reviewers also can open issues in your package repository. 
We prefer issues that link back to the review as they document changes made to your 
package that were triggered by our review process.

## 8. Response to Reviews
You should respond to reviewers’ comments within **2 weeks** of the 
last-submitted review. You can make updates to your package at any time. We 
encourage ongoing conversations between authors and reviewers. See the 
reviewing guide for more details.

## 9. Acceptance into pyOpenSci
Once the reviewers are happy with changes that you've made to the package, the
editor will review everything and accept your package into the pyOpenSci ecosystem.
Congratulations! You are almost done!

## My Package is Approved, Now What?

Congratulations on being accepted into the pyOpenSci community of maintainers!
Once your package is approved, a few things will happen:

1. We will ask you to ensure that your package is being tracked / archived using 
Zenodo. You will then want to created a tagged release representing the version of the 
package accepted by pyOpenSci.
2 We will ask you to add the pyOpenSci badge [![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/issue-number) to the 
top of your README.md file.
1. We will ask you to add your package to the [pyOpenSci website](https://www.pyopensci.org/contributors/). This will give 
your package more visibility in the community as a vetted pyOpenSci tool.
    * We also will ask you (and those who reviewed your package) to add yourself to our list of contributors as a maintainer!
1. We will promote your package on our twitter channel!
2. If you wish to go on to submit your package to JOSS, this is when you'd start 
that process. 

### Journal of Open Source Software (JOSS) Submission

PyOpenSci has a partnership with JOSS where our review is accepted by JOSS by
default if the package fits into the JOSS scope.

- When you submit your package for pyOpenSci review, you can opt to include a 
submission to JOSS after passing pyOpenSci review. In this case, your package 
will evaluated by JOSS through the pyOpenSci review
- To complete the JOSS submission, you will also need to craft a **paper.md** 
file describing the package following JOSS' standards (see below). More detail on the requirements for JOSS can be found on [their website](https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain).
- If you choose to opt into the pyOpenSci / JOSS partnership in your review, 
you do NOT need to go through a second review with JOSS. JOSS accepts our review
for theirs. Please just start a review process with JOSS and reference the pyOpenSci
review issue that you have been working within for your review with us. Make sure
that you let the JOSS editor know that we have already accepted you. They will use 
our review for their process and fast track you through their review! 

```{note} 
Acceptance to pyOpenSci does not guarantee acceptance to JOSS. In particular, 
JOSS doesn't accept the full variety of packages that are in scope for
pyOpenSci. For example, thin API wrappers fall within
[pyOpenSci's scope](../about-peer-review/aims-and-scope) but 
are usually not accepted by JOSS. Be sure to review JOSS's 
[submission requirements](https://joss.readthedocs.io/en/latest/submitting.html#submission-requirements) 
before writing up a paper about your package.
```
