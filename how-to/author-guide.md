# Guide for Python Package Authors & Maintainers

:::{toctree}
:hidden:
:caption: How To Guides

Author Guide <self>
Reviewer Guide <reviewer-guide>
Editor Guide <editors-guide>
Editor-in-Chief Guide <editor-in-chief-guide>
Triage Team Guide <review-triage-team>
Peer Review Lead <peer-review-lead>
:::

```{toctree}
:hidden:
:caption: Onboarding Editors & Reviewers

Finding & Onboarding Editors <onboarding-guide>
Finding & Onboarding Reviewers <finding-reviewers>
```

Are you considering submitting a package for review with pyOpenSci? You've
come to the right place! Below you will find the steps that you need to follow
to submit a package to pyOpenSci for peer review.

## Peer review resources

:::::{grid} 1 2 3 3
:class-container: text-center
:gutter: 3

::::{grid-item}
:::{card} <i class="fa-solid fa-crosshairs"></i> Package scope
:link: ../about/package-scope
:link-type: doc
:class-card: left-aligned

Learn about the requirements and scope of packages that pyOpenSci reviews.
:::
::::

::::{grid-item}
:::{card} <i class="fa-solid fa-magnifying-glass"></i> How review works
:link: ../our-process/how-review-works
:link-type: doc
:class-card: left-aligned

We review packages openly using GitHub Issues.
:::
::::

::::{grid-item}
:::{card}  <i class="fa-solid fa-timeline"></i> Review timeline
:link: ../our-process/review-timeline
:link-type: doc
:class-card: left-aligned

Curious about the general timeline for pyOpenSci reviews?
:::
::::

::::{grid-item}
:::{card} Review Guidelines & Policies
:link: ../our-process/policies
:link-type: doc
:class-card: left-aligned

Read about our peer review policies.
:::
::::

::::{grid-item}
:::{card} <i class="fa-solid fa-handshake-angle"></i></i> Need packaging guidance?
:class-card: left-aligned

[If you want to learn more about packaging best practices, you can check out our packaging guide.](https://www.pyopensci.org/python-package-guide)
:::
::::

:::::

Before you begin this process, [please be sure to read the review process guidelines](../our-process/policies).

```{note}
**Before you consider submitting to us, please consider the following:**

1. Please be sure that you have time to devote to making changes to your
package. During review, you will receive feedback from an editor and two reviewers. Changes could
take time. Please consider this before submitting to us. You can read more about the timeline to make changes in our [peer review policies page](../our-process/policies).
2. A diverse group of volunteer editors and reviewers leads peer review.
Please be considerate when engaging with everyone online.
```

## 1. Do you plan to continue to maintain your package?

One of the goals of pyOpenSci is to maintain a curated list of
community-approved, maintained, and vetted tools that support open science workflows.

As such, we review packages that will be useful to the community
and maintained over time. While we understand that burnout is real,
and you may move on in the future to other projects, we ask that you commit
to maintaining your package for at least 1-2 years after the review process
is complete.

If that maintenance commitment is too much, you might consider submitting
your package to a journal that is more focused on publication only.

### Who should submit the package for review?

If you have a team of people maintaining your package, please be sure
that the submitting author is the person who "owns" or leads that maintenance.
That person will become the long-term point of contact
for pyOpenSci.

- Please also include the names of all maintainers on the project
  as we also want to ensure that everyone working on the project receives full credit
  for their effort.

```{note}
If your package is more of a tool to support a specific workflow that
either:
* may not be maintained long term or
* may be so specific that it won't have a user base outside of your lab or work environment

please consider submitting it directly to a publisher like the
Journal of Open Source Software (JOSS). A publisher like JOSS has less
emphasis on long-term software maintenance and focuses more on
publication quality and citation/credit.
```

## 2. Does Your Package Meet Packaging Requirements?

Before submitting your project for review with pyOpenSci, make sure that
your package meets all of the requirements listed in the editor checks (see below).
We use these checks as a baseline for all submissions and pre-submissions to
pyOpenSci.

If you have questions about any of the elements listed below, you can
check out our [pyOpenSci Python packaging guide](https://www.pyopensci.org/python-package-guide) which includes an overview discussion of best practices
for Python packaging, including discussions of:

- Tools that you can use to create your package
- Tools for creating and publishing documentation.
- Resources for creating files such as the README file, code of conduct, contributing guide, and more.

```{include} ../appendices/editor-in-chief-checks.md

```

```{hint}
**Do you have questions about Python packaging or our peer review process?**

[Post your question(s) in our Discourse forum under `coding-help`](https://pyopensci.discourse.group/c/coding-help/10). We will do our best to help you with questions
surrounding:

* Package structure
* Setting up continuous integration
* `PyPI` and `conda` publication
* Getting started with test suites
* Creating and publishing documentation
* Anything related to our peer review process.

Also, check our [Packaging Guide](https://www.pyopensci.org/python-package-guide).
This guide includes:

* a [beginner-friendly tutorial](https://www.pyopensci.org/python-package-guide/tutorials/create-python-package.html) for creating pure Python packages
* [An overview of the packaging tool ecosystem
that you can use to create a high-quality
Python package.](https://www.pyopensci.org/python-package-guide/package-structure-code/python-package-build-tools.html)
```

## 3. Is Your Package in Scope for pyOpenSci?

Next, check to see if your package falls within the topical and technical scope of pyOpenSci. If you aren't
sure about whether your package fits within pyOpenSci's scope (below), submit
a [presubmission inquiry issue on the software-review](https://github.com/pyOpenSci/software-review/issues/new?assignees=&labels=0%2Fpresubmission&template=presubmission-inquiry.md&title=)
repository. After you submit an inquiry, a pyOpenSci editor will provide feedback regarding the fit of your package for pyOpenSci review. This can take
up to a week.

Our current categories for determining package scope are below:

<!-- colors https://github.com/pydata/pydata-sphinx-theme/blob/main/src/pydata_sphinx_theme/assets/styles/variables/_color.scss-->

```{button-link} ../about/package-scope.html
:color: primary
:class: sd-rounded-pill
Click here to view our technical and domain scope requirements.
```

## 4. Submit Your Package for Peer Review

To submit your package for peer review, you can
open an issue in our [pyopensci/software-review repo](https://github.com/pyOpenSci/software-review/issues/new/choose/)
repository and fill out the [Submit Software for Review](https://github.com/pyOpenSci/software-submission/issues/new?template=submit-software-for-review.md) issue template.

## 5. Editor-in-Chief Reviews Package for Scope and Minimal Infrastructure Criteria

Once the issue is opened, our editor-in-chief and an editor from our editorial board will review your submission within
**2 weeks** and respond with next steps. The editor may request that you make updates
to your package to meet minimal criteria before review. They may also reject your
package if it does not fall within our scope.

```{button-link} ../how-to/editor-in-chief-guide.html#editor-checklist-template
:color: primary
:class: sd-rounded-pill
Click here to view the editor checks that will be used to evaluate your package.
```

## 6. The Review Begins

If your package meets the minimal criteria for being
reviewed, it may then be given to an editor with appropriate domain experience
to manage the review process. That editor will assign 2-3 reviewers to review your
package. Reviewers will be asked to provide review feedback as comments on your
issue within **3 weeks**. Reviewers can also open issues in your package repository.
We prefer issues that link back to the review as they document changes made to your
package that were triggered by our review process.

## 7. Response to Reviews

You should respond to reviewers’ comments within **2 weeks** of the
last-submitted review. You can make updates to your package at any time. We
encourage ongoing conversations between authors and reviewers. See the
[guide for package reviewers](reviewer-guide.md) for more details about reviewers' engagement with package
maintainers during a review.

## 8. Acceptance into pyOpenSci

Once the reviewers are happy with the changes that you've made to the package, the
editor will review everything and accept your package into the pyOpenSci ecosystem.
Congratulations! You are almost done!

## My Package is Approved, Now What?

Congratulations on being accepted into the pyOpenSci community of maintainers!
Once your package is approved, a few things will happen:

1. We will ask you to ensure that your package is being tracked/archived using
   Zenodo. You will then create a tagged release representing the version of the
   package accepted by pyOpenSci.
1. We will ask you to add the pyOpenSci badge [![pyOpenSci Peer Reviewed](https://pyopensci.org/badges/peer-reviewed.svg)](https://github.com/pyOpenSci/software-review/issues/issue-number) to the
   top of your **README.md** file.
1. We will promote your package on our social media channels!
1. We will invite you to write a blog on our website spotlighting your package. The blogs our maintainers write are among the most popular content on the website!

If you'd like to submit your package to JOSS, you can do so now. Remember that JOSS will accept our review as theirs, so **you DO NOT need to go through another review**. Read more below.

### Journal of Open Source Software (JOSS) Submission

pyOpenSci has a [partnership with JOSS](JOSS), where our review is accepted by JOSS by
default if the package fits into the JOSS scope.

- When you submit your package for pyOpenSci review, you can opt to include a
  submission to JOSS after passing pyOpenSci review. In this case, your package
  will be evaluated by JOSS through the pyOpenSci review
- To complete the JOSS submission, you will also need to craft a **paper.md**
  file describing the package following JOSS' standards (see below). More details on the requirements for JOSS can be found on [their website](https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain).
- If you choose to opt into the pyOpenSci/JOSS partnership in your review,
  you DO NOT need to go through a second review with JOSS. JOSS accepts our review
  as theirs. Please start a review process with JOSS and reference the pyOpenSci
  review issue where your package was accepted. Make sure
  that you let the JOSS editor know that we have already accepted your package. The JOSS editor will review your paper. Once your package is accepted, you will be given a JOSS cross-ref-enabled DOI and badge to display on your README file.

```{note}
Acceptance to pyOpenSci does not guarantee acceptance to JOSS. In particular,
JOSS doesn't accept the full variety of packages that are in scope for
pyOpenSci. For example, thin API wrappers fall within
[pyOpenSci's scope](../about/package-scope) but
are usually not accepted by JOSS. Be sure to review JOSS's
[submission requirements](https://joss.readthedocs.io/en/latest/submitting.html#submission-requirements)
before writing up a paper about your package.
```

## Post review - welcome to the pyOpenSci community

Congratulations! Once your package has been accepted into the pyOpenSci ecosystem, you'll be invited to join our [community Slack](https://join.slack.com/t/pyopensci/shared_invite/zt-39qitgkqb-gZTIo79xCJhS5kSxW1yNfg) where you can connect with other package maintainers, get help with maintenance questions, and stay updated on community developments.

### Ongoing support from pyOpenSci

We're committed to supporting you throughout your package's maintenance journey:

**Annual check-ins**: We'll reach out each year to see how your package is doing and learn about any updates we can help highlight through our blog, social media, or newsletter.

**Community resources**: Take advantage of our Slack community to connect with other maintainers, share experiences, and get advice on common maintenance challenges. We're also building additional resources and tools to help package maintainers succeed.

**Maintenance assistance**: If you have specific maintenance challenges, our Slack community is a great place to ask questions. There is a lot of packaging and community expertise in our vibrant community!

### When you need help or want to step down

Life changes and priorities shift. If maintaining your package becomes challenging, please reach out to us. We're here to help, and we have several options:

- **Finding co-maintainers or new maintainers**: If you are interested, we can try to connect you with community members interested in contributing to or taking over maintenance of your package.
- **Package archival**: If maintenance isn't sustainable, we can work together [to archive your package](https://www.pyopensci.org/python-packages.html#archived-packages).

If the package is archived, we will remove it from our curated list
of vetted tools.

### Maintenance policies

For detailed information about our maintenance expectations, annual check-in process, and archival procedures, please take a look at our [post-review process documentation](post-review-process). Remember, you maintain full ownership of your package. We're here to support you, not interfere with your development process.

:::{tip}
We will [follow our package archive process to determine whether your package should be archived.](archive-process)
:::
