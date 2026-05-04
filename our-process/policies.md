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
place on GitHub. However, you may contact the editor by email if
needed.

When submitting a package, please make sure that your GitHub notification
settings are turned on for the software-submission repository to notify you
when you receive feedback on a review issue.

(submission-volume)=

## Submission volume and maintainer overlap

To protect our volunteer peer review team and ensure quality reviews for all
packages, we have policies regarding the volume of simultaneous submissions.

### Unique point of contact requirement

Each submission to pyOpenSci should have one point of contact per package.
Each person listed as a point of contact may have only one submission under
review at a time.

This policy ensures that:

- Review feedback receives appropriate attention from maintainers.
- Maintainers don't become overwhelmed managing multiple concurrent reviews.
- Our volunteer reviewers and editors can focus their efforts effectively.

### Multiple submissions with overlapping maintainer teams

If multiple packages are submitted simultaneously with overlapping maintainer
teams, we will evaluate our volunteer reviewer capacity and may request
staggered submissions to ensure quality review for all packages and to protect
the time and availability of our volunteer editorial team.

We recognize that some situations may warrant exceptions to these guidelines.
For example, two closely related packages that would benefit from review by
the same editorial team may be handled together. All policies may have
exceptions under the discretion of the editors, and decisions will be made by
the Editor-in-Chief based on reviewer capacity and the specific circumstances
of the submission.

## Submitting your package for review in other venues

If you are considering submitting your package to a software journal, you may want to submit to us first because our review may result in significant updates to your package. If you are considering submitting your package to a scientific journal which focuses on the methods, then we encourage you to
**submit to the journal first**. A package that has already gone through a rigorous journal
review typically has a longer development history, more established use cases, and has already
undergone deeper scientific and methodological scrutiny than pyOpenSci alone can provide.
pyOpenSci's focus is on the Python packaging ecosystem and software best practices, and a
package that arrives with that foundation in place makes for a stronger submission.

Once your package has been published (or accepted) by a journal, you can submit to pyOpenSci.
If the publication covers the package's core methodology, you may be eligible for our
[fast-track review pathway](publication-fast-track).

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

:::{note}
**Submitting to JOSS after pyOpenSci review:**

While pyOpenSci's scope may be more flexible than JOSS in certain areas (such as
package size requirements), packages must still meet JOSS's specific criteria to
be eligible for JOSS fast-track submission. If your package is accepted by pyOpenSci
but does not meet JOSS requirements (e.g., minimum lines of code), it will not be
eligible for JOSS fast-track review. See our [package scope guidelines](package-size-effort)
for more details.
:::

(publication-fast-track)=
## Fast-track review for packages with an associated peer-reviewed publication

If your package has an associated peer-reviewed publication—such as a journal article—that covers
the primary domain methodology or algorithm implemented by the package, it may be eligible for a
**fast-track review** with one reviewer instead of the usual two.

The rationale is that the domain and algorithmic components have already been vetted through
the publication's peer review. pyOpenSci review then focuses on packaging quality,
documentation, and adherence to our standards.

:::{note}
**Policy change:** Previously, pyOpenSci declined to review packages whose core method or algorithm
had not yet been vetted by the scientific community, since pyOpenSci is not a journal and cannot
review novel science itself. This fast-track pathway extends our scope: packages whose method *has*
been peer-reviewed and published can now be reviewed under this streamlined process. For these
packages, journal review naturally comes first — and that ordering is expected and encouraged.
See the [analytics and statistics scope section](analytics-statistics-scope) for more detail.
:::

### Eligibility

Your package may be eligible for fast-track review if:

- It has an associated peer-reviewed publication that covers the primary method or algorithm
  it implements.
- The publication is directly relevant to the core scientific functionality of the package.

:::{note}
Accepted publication venues and any additional eligibility criteria are still being finalized.
There is no fixed list of qualifying journals — in general, any credible, quality peer-reviewed
venue is acceptable. Common examples include [SoftwareX](https://www.sciencedirect.com/journal/softwarex)
and [JOSS](https://joss.theoj.org/). The final decision on eligibility rests with the
pyOpenSci Editor-in-Chief. If you believe your package qualifies, note this in your
pre-submission inquiry or submission.
:::

### What fast-track means

In a standard pyOpenSci review, two reviewers are assigned: typically one with domain-specific
scientific expertise and one focused on software usability, packaging, and infrastructure. For
packages with an associated peer-reviewed publication, the domain/scientific component has
already been externally vetted.

Under this pathway:

- **One reviewer** (rather than two) will review the package, focusing on software quality,
  usability, documentation, and pyOpenSci packaging standards — the role that does not require
  deep domain expertise.
- The reviewer is **not** expected to deeply evaluate the underlying scientific method or algorithm,
  which has already been covered by the associated publication. However, they should perform a
  cursory check to verify that the methods implemented in the package appear consistent with
  what is described in the publication.
- The editor conducts their standard checks as usual.

Issues using this pathway are labeled `publication-fast-track` to signal the modified
review scope.

### Including publication details in your submission

If your package has an associated publication, include the following front matter in your
submission issue to help editors assess eligibility:

```yaml
publication:
  title:
  doi:
  journal:
```

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

- Acknowledgment of and transparency around the widespread use of Generative AI tools, with a focus on Large Language Models (LLMs) in Open Source development.
- Ensure an equitable balance of effort in the peer review process: Authors acknowledge that a human has carefully reviewed parts of the package that are AI-generated. Generated material should be in a state that minimizes review time. Our reviewers are not responsible for correcting errors in machine-generated content.
- Disclosure allows reviewers and editors to make informed decisions around the types of packages that they wish to review code for.
- Raise awareness of challenges that Generative AI tools present to the scientific (and broader) open source community.

[Please see this GitHub issue for a discussion of the topic.](https://github.com/pyOpenSci/software-peer-review/issues/331)
:::

### Disclosure of generative AI use in pyOpenSci reviewed packages

- When you submit a package to pyOpenSci, please disclose any use of LLMs (Large Language Models) in your package's development by checking the appropriate box and describing your use of generative AI in its development and/or maintenance on our software submission form. Disclosure should include what parts of your package were developed using Generative AI tools.
  - Please also disclose this use of Generative AI tools in your package's `README.md` file and in any modules where generative AI contributions have been implemented.
- We require that all aspects of your package have been reviewed carefully by a human on your maintainer team. Please ensure all text and code have been carefully checked for bugs and issues before submitting to pyOpenSci.
- Your acknowledgment of using Generative AI will not prejudice the success of your submission. However, a reviewer can and will ask you to revisit your package's content if it appears that sections have been copied and pasted from other sources without human review.
- If the review team (comprised of the editor and reviewers) determines that the code and text in the package are too challenging to review, they can decide to pause and/or discontinue the review following this policy’s guidelines.

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
