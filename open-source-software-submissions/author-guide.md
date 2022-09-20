# pyOpenSci Review Guide for Python Open Source Package Authors

So you are considering submitting a package for review with pyOpenSci? You've 
come to the right place. 

## 1. Does Your Package Meet Packaging Requirements?
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

## 2. Is Your Package in Scope for pyOpenSci?
Next, check to see if your package falls into the scope of pyOpenSci. If you aren't 
sure about whether your package fits within
[pyOpenSci's scope](../open-source-software-peer-review/aims-and-scope), submit
a [presubmission inquiry issue on the software-review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
repository. After you submit an inquiry, a pyOpenSci editor will get back to you 
with input regarding the fit of your package for pyOpenSci review. This can take 
up to a week. 

## 3. Presubmission Questions

If your package does not clearly fit within one of the categories outlined in
our [scope](../open-source-software-peer-review/aims-and-scope), create
a [Presubmission Inquiry issue](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
in our software-review repo. You can use the same issue template if you have
other questions. An editor will get back to you in a few days to answer your
questions and to help determine the fit.

```{include} ../scope.md

YOU
```

```{note} 
Before you consider submitting to us please consider the following:

1. Please be sure that you have time to devote to making changes to your 
package. You may get feedback from an editor and two reviewers. Changes could 
take time. Please consider this before submitting to us.
2. Peer review is lead by a diverse group of volunteer editors and reviewers. 
Please be considerate when engaging with everyone online.  
```

## 4. Submit Your Package for Peer Review
To submit your package for peer review, you can 
open an issue in our [pyopensci/software-review repo](https://github.com/pyOpenSci/software-review/issues/new/choose/issues/new/choose)
repository and fill out the [Submit Software for Review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=1%2Feditor-checks%2C+New+Submission%21&template=submit-software-for-review.md&title=) issue template. 

## 5. Editor in Chief Reviews Package for Scope and Minimal Infrastructure Criteria
Once the issue is opened, an editor will review your submission within 
**2 weeks** and respond with next steps. The editor may request that you make updates
to your package to meet minimal criteria before review. They also may reject your 
package if it does not fall within our scope. 

## 6. The Review Begins
If your package meets minimal criteria for being 
reviewed it may then be given to an editor with appropriate domain experience 
to run the review. That editor will assign 2-3 reviewers to review your 
package. Reviewers will be asked to provide review feedback  as comments on your 
issue within **3 weeks**. Reviewers also can open issues in your package repository. 
We prefer issues that link back to the review as they document changes made to your 
package that were triggered by our review process.

## 7. Response to Reviews
You should respond to reviewers’ comments within **2 weeks** of the 
last-submitted review. You can make updates to your package at any time. We 
encourage ongoing conversations between authors and reviewers. See the 
reviewing guide for more details.

## 8. Acceptance into pyOpenSci
Once the reviewers are happy with changes that you've made to the package, the
editor will review everything and accept your package into the pyOpenSci ecosystem.
Congratulations! You are almost done!

## My Package is Approved, Now What?

- **Package Approval** Once your package is approved, a few things will happen:
1. We will give you instructions on how to add your package to the pyOpenSci 
website. This will give your package more visibility in the community as a vetted pyOpenSci tool.
2. We will ask you to add the pyOpenSci badge <TODO add image of badge> to your 
README.md file.
3. We will promote your package on our twitter channel!
4. If you wish to go on to submit your package to JOSS, this is when you'd start 
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
[pyOpenSci's scope](../open-source-software-peer-review/aims-and-scope) but 
are usually not accepted by JOSS. Be sure to review JOSS's 
[submission requirements](https://joss.readthedocs.io/en/latest/submitting.html#submission-requirements) 
before writing up a paper about your package.
```
