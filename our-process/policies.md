# Peer Review Guidelines & Policies

## Review process guidelines

pyOpenSci packages are reviewed for quality, fit, scope, documentation, and
usability. The review process is similar to a manuscript review; however, it
has a stronger focus on Python packaging best practices.

Unlike a manuscript review, our peer review process is an ongoing conversation.
Once all major issues and questions are addressed, the review editor will decide
to accept, hold, or reject the package.

Rejections are usually done early in the process, before the review process
begins. In rare cases, a package may also not be onboarded into the pyOpenSci
ecosystem after review & revision.

It is ultimately the editor’s decision on whether or not to reject the package
based on how the reviews are addressed.

## Review communication approach

Communication between authors, reviewers, and editors takes
place on GitHub. You can, however, choose to contact the editor by email if
needed.

When submitting a package, please make sure that your GitHub notification
settings are turned on for the software-submission repository to notify you
when you receive feedback on a review issue.

## Submitting your package for review in other venues

We recommend submitting your package for review with pyOpenSci before
submitting a software paper describing the package to a journal.

Review feedback may result in significant improvements and updates to your package,
including changes that could break package functionality.

Applying reviewer or editor recommendations to your package can improve your
users' experience with future versions of your package, even if your package is
already published on `PyPI` or `conda-forge`.

> Please do not submit your package for review while it or an associated
> manuscript is also under review at another venue, as this may result in
> conflicting requests for changes from two sets of reviewers.

### Publication with Journal of Open Source Software (JOSS)

If you have previously published your software package with the Journal of Open
Source Software (JOSS), you can still submit it to pyOpenSci for review. This
provides increased visibility for your package as a vetted tool within the scientific
Python ecosystem and access to our long-term maintenance support.

Since your package has already undergone a JOSS review, we have a specific,
expedited review process to streamline the submission process and save time.
Once accepted, your package will be treated like any other package in our ecosystem.

#### Expedited Review Process

We offer two pathways for packages previously reviewed by JOSS:

1. Fast-Track Review (Editor-Only):
   Your package is eligible for this fast-track review if it has been published by
   JOSS within the last year and has not undergone major changes in dependencies, design, or API
   since its JOSS publication. In this case, an editor will conduct the review by going
   through our pyOpenSci submission checklist to ensure all our specific requirements are met.

2. Expedited Review (Editor + One Reviewer):
   If your package's JOSS publication is over a year old, or if it has had major changes as described above
   since publication, it will undergo an expedited review with one editor and one external reviewer.
   The editor and reviewer will focus on any significant changes and ensure the package meets all current pyOpenSci
   standards. This approach reduces the burden of a full review while ensuring the quality of the package
   reflects its most recent version.

(coi)=

## Conflict of interest for reviews and editors

Following criteria are meant to be a guide for what constitutes a conflict of
interest (COI) for an editor or reviewer. The potential editor or reviewer has
a conflict of interest if:

- The authors with a major role are from the potential reviewer/editor’s
  institution or institutional component (e.g., department).
- Within the past three years, the potential reviewer/editor has been a
  collaborator or has had any other professional relationship with any person
  on the package who has a major role.
- The potential reviewer/editor serves as a member of the advisory board for
  the project under review.
- The potential reviewer/editor would receive a direct or indirect financial
  benefit if the package is accepted.
- The potential reviewer/editor has significantly contributed to a competitor
  project.
- There is also a lifetime COI for family members, business partners,
  thesis students/advisors, or mentors.

In the case where none of the associate editors can serve as editor, an
external guest editor will be recruited to lead the package review.

(generative-ai-policy)=
## Policy for use of generative AI / LLMs

:::{admonition} How this policy was developed
:class: important

The policy below was co-developed by the pyOpenSci community. Its goals are:

* Acknowledgment of and transparency around the widespread use of Generative AI tools with a focus on Large Language Models (LLMs) in Open Source.
* Protect peer review efficiency: Ensure human review of any LLM-generated contributions to a package to protect editor and reviewer volunteer time in our peer review process.
* Raise awareness of challenges that Generative AI tools present to the scientific (and broader) open source community.
[Please see this GitHub issue for a discussion of the topic.](https://github.com/pyOpenSci/software-peer-review/issues/331)
:::

### Disclosure of generative AI use in pyOpenSci reviewed packages

* When you submit a package to pyOpenSci, please disclose any use of LLMs (Large Language Models) in your package’s generation by checking the appropriate boxes on our software submission form. Disclosure should generally include what parts of your package were developed using LLM tools.
  * Please also disclose this use of Generative AI tools in your package's `README.md` file and in any modules where generative AI contributions have been implemented.
* We require that all aspects of your package have been reviewed carefully by a human on your maintainer team. Please ensure all text and code have been carefully checked for bias, bugs, and issues before submitting to pyOpenSci.
* Your acknowledgment of using Generative AI will not impact the success of your submission unless you have blindly copied text and code into your package without careful review and evaluation of its accuracy, and for any systemic bias.
* If the review team (comprised of the editor and reviewers) determines that the code and text in the package are too challenging to review, they can decide to pause and/or discontinue the review following this policy’s guidelines.

Below is the checklist that you will need to respond to in our submission form:

```{include} ../appendices/gen-ai-checklist.md
```

## Review timelines and on-hold reviews

At any time, an author can choose to have their submission put on hold
(the editor applies the `on-hold` label to the GitHub issue). The `on-hold`
status will be revisited every 3 months. If after one year there has been
no movement on the review, the issue will be closed.

(post-review-process)=

## After acceptance: package ownership and maintenance

Package authors are expected to maintain and develop their software and
retain
ownership of it after acceptance into pyOpenSci, according to the peer review
agreement acknowledged upon submission. This maintenance commitment should
last for at least two years. The pyOpenSci team will not interfere with
day-to-day tool maintenance unless someone in the community is explicitly added as
a project collaborator.

If you need to step down from maintaining your accepted pyOpenSci package,
please promptly notify the pyOpenSci Editor-in-Chief or Software Review Lead.
pyOpenSci will collaborate with you to either:

- Find a new maintainer or
- Archive the tool, depending on what best suits your specific scientific
  Python package.

We will reach out to our package maintainers each year to verify the
package is actively maintained and to see if there are any updates we can
highlight through our social channels.

### Maintenance tracking

pyOpenSci is building a system to track package metrics and activity,
including issues, pull requests, and dates of the last release and last commit
to the package repository. Activity is defined as a repository commit, pull
request, or release.

We will flag packages that haven't been updated within a 1-year/12-month time
period based on activity. Packages with no activity after 12 months will be
flagged. At that time, a pyOpenSci editorial team member will contact the package
maintainers to evaluate the maintenance status of their package.

(archive-process)=

### Package maintenance and maintainer responsiveness

If, after one year, package maintainers are unresponsive to requests for
package fixes or messages from the pyOpenSci team, we will initiate
discussions about the package's ongoing inclusion within the pyOpenSci
ecosystem.

In cases where the community heavily uses a package, we may
collaborate with the community to identify reasonable next steps, such as
assisting in finding a new maintainer. If a solution for the ongoing package
maintenance of your package is not found, the package will be archived within
the pyOpenSci ecosystem. [See section on archiving below.](package-archive)

If a sub-community decides to fork and maintain the package, we are open to
working with the new maintainers to register the newly forked package within
our ecosystem. The original package will be archived with a link to the new
fork.

We will also add a note to any blogs written that highlight your tool, that
the package is no longer maintained.

### Quality commitment

pyOpenSci strives to develop and promote high-quality research software. To
ensure that your software meets our criteria, we review all of our submissions
as part of the Software Peer Review process. We expect that you will continue
to maintain a package that has been accepted continually.

Despite our best efforts to support contributed software, errors are the
responsibility of individual maintainers. Buggy, unmaintained software may
be removed from our suite at any time. We also ask maintainers that they get
in touch with us if they do need to step down from maintaining a tool.

### Requesting Package Removal from the pyOpenSci Ecosystem

In the unlikely scenario that a contributor of a package requests removal of
their package from our ecosystem, we retain the right to offer the last/most
recently released version of that package in our ecosystem for archival
purposes only.

(package-archive)=
### Archiving a package

If a package appears to be no longer maintained, we will mark it as
archived, which moves the package from our
[main package listing](https://www.pyopensci.org/python-packages.html#all-packages)
to our [archived packaging](https://www.pyopensci.org/python-packages.html#archived-packages)
listing section.

To archive a pyOpenSci-approved package, add the
[archive label](https://github.com/pyOpenSci/software-submission/issues?q=label%3Aarchived)
to the original review issue. Once this label is applied to the issue, the
website will automatically update to reflect this status. If at any point
in the future, an archived package undergoes active maintenance again, this
label can be removed from the issue to move the package back to an active
status.

We opt to archive inactive packages rather than remove them to preserve the
history and contributions of the software, ensuring that others can still
access and learn from it. This approach maintains the integrity of the
scientific record and allows for potential future reactivation or forking
of the project. By archiving rather than removing, we provide a clear
status of the package while keeping its legacy intact for reference and
educational purposes.
