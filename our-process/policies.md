# Peer Review Guidelines & Policies

## Review process guidelines

[pyOpenSci](https://www.pyopensci.org) packages are reviewed for quality, fit,
scope, documentation, and usability. The review process is similar to a
manuscript review; however, it has a stronger focus on Python packaging best
practices.

Unlike a manuscript review, our peer review process is an ongoing conversation.
Once all major issues and questions are addressed, the review editor will
decide to accept, hold, or reject the package.

Rejections are usually done early in the process, before the review process
begins. In rare cases, a package may also not be onboarded into the pyOpenSci
ecosystem after review and revision.

It is ultimately the editor’s decision on whether or not to reject the package
based on how the reviews are addressed.

## Review communication approach

Communication between authors, reviewers, and editors takes place on GitHub.
However, you may contact the editor by email if needed.

When submitting a package, please make sure that your GitHub notification
settings are turned on for the software-submission repository to notify you
when you receive feedback on a review issue.

## Summary of our generative AI policy

We support thoughtful use of Generative AI tools in software development, but we
require transparency and meaningful human oversight for any code or
documentation submitted to our peer review process. Packages should demonstrate
sustained, human-driven design and maintenance, rather than short-lived or
largely machine-generated codebases.

This page provides a high-level overview of our review policies. For detailed
guidance on expectations, disclosure, and examples related to Generative AI and
LLMs, please see our dedicated [generative-ai-policy](generative-ai-policy).

(submission-volume)=
## Submission volume and maintainer overlap

To protect our volunteer peer review team and ensure quality reviews for all
packages, we have policies regarding the volume of simultaneous submissions.

### Unique point of contact requirement

Each submission to pyOpenSci should have one point of contact per package.
Each person listed as a point of contact may have only one submission under
review at a time.

This policy ensures that:

* Review feedback receives appropriate attention from maintainers.
* Maintainers don't become overwhelmed managing multiple concurrent reviews.
* Our volunteer reviewers and editors can focus their efforts effectively.

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

#### Expedited review process

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

(coi)=
## Conflict of interest for reviews and editors

Following criteria are meant to be a guide for what constitutes a conflict of
interest (COI) for an editor or reviewer. The potential editor or reviewer has
a conflict of interest if:

* The authors with a major role are from the potential reviewer/editor's
  institution or institutional component (e.g., department).
* Within the past three years, the potential reviewer/editor has been a
  collaborator or has had any other professional relationship with any person
  on the package who has a major role.
* The potential reviewer/editor serves as a member of the advisory board for
  the project under review.
* The potential reviewer/editor would receive a direct or indirect financial
  benefit if the package is accepted.
* The potential reviewer/editor has significantly contributed to a competitor
  project.
* There is also a lifetime COI for family members, business partners,
  thesis students/advisors, or mentors.

In the case where none of the associate editors can serve as editor, an
external guest editor will be recruited to lead the package review.

(generative-ai-policy)=
## Policy for use of generative AI / LLMs

:::{admonition} How this policy was developed
:class: important

The Generative AI policy below was co-developed by the pyOpenSci community. Its goals are:

* To **acknowledge the widespread use of Generative AI tools** (LLMs) and promote transparency and responsible use that ensures better software outputs that support sound open source development practices.
* **Ensure equitable balance of effort in peer review** — authors are responsible for human review of AI-generated content before submission; our volunteer reviewers are not responsible for identifying and/or correcting machine-generated errors or issues.
* **Protect volunteer reviewers** from being the first line of review for generated code.
* Give reviewers and editors the information they need to make informed decisions about what they choose to review.
* **Support and promote packages that follow sustainable software practices** that enable future discovery and uphold the foundational principles of scientific open source.
* Raise awareness of the broader challenges Generative AI presents to the scientific open source community.
* To promote transparency and privacy in user data

[Please see this GitHub issue for a discussion of the topic.](https://github.com/pyOpenSci/software-peer-review/issues/331)

In generating our Generative AI policy, we acknowledge some of the other policies in the open source ecosystem that inspired our work here, including:

* [FastAPI docs](https://fastapi.tiangolo.com/contributing/#automated-code-and-ai)
* [JOSS AI Policy](https://blog.joss.theoj.org/2026/01/preparing-joss-for-a-generative-ai-future)
* [Scikit-Learn Policy](https://scikit-learn.org/dev/developers/contributing.html#automated-contributions-policy)
* [Melissa Mendonça’s Collection of GenAI Policies](https://github.com/melissawm/open-source-ai-contribution-policies)

:::

## Generative AI and open source development

We understand and support your use of Generative AI tools to improve software development workflows and to make your developer workflows more efficient. We want you to use them thoughtfully and effectively, and in ways that improve both the open source ecosystem and your development trajectory.

We expect that all code and documentation submitted to our peer review process should have meaningful human review, intervention, judgment, and context. We understand that the use of current Generative AI tools is often tightly woven into development workflows, making disclosure challenging. But **we still require disclosure** to support both transparency and to allow reviewers and editors to understand what they are reviewing.

The policies below support adherence to thoughtful open source development best practices. A pyOpenSci package submission should demonstrate both need and sustained value to the research community. **Short-lived, single-use codebases are out of scope for pyOpenSci.**

## Communication in review issues

* We prefer that all communication in our software review issues are written by a human. We embrace the use of LLMs for translation and grammar correction. We prefer honest interactions over ones that prioritize perfect language and grammar. As little aid from an LLM as possible.
* We will block accounts that spam our repositories or burden our volunteers with repeated, automated comments that aren't directly related to and in support of productive conversations in a review.

## Package development and design approach

* **Development History Timeline:** Projects should have at least **3-6 months of public development history**, with evidence of releases, public issues, and pull requests that reflect **iterative, thoughtful development** rather than rapid and recent code generation.
* If the human effort put into the package is less than the effort required to review it, please don't submit the package.
* Software should be developed openly, rather than developed in private and then moved to a public repository with an OSI-approved license to meet minimal open source requirements.
* **Development History Approach:** We encourage thoughtful development history and patterns, including tightly scoped commits with clear commit messages that follow iterative development best practices, rather than large commits that address multiple issues in a package and affect large volumes of files throughout the package. These workflows signal careful design and development, and changes to a codebase that could be reviewed by a human.
* Projects with very short, rapid development timelines (weeks to a few months) will face higher scrutiny by our review teams than those that have a significant development history (more than 6 months)
* **Package Scope & Design:** We value packages with a thoughtful, well-scoped design. When submitting, we will ask you to describe the key design decisions behind your package — the tradeoffs you considered and why you built it the way you did.
* We place greater value on packages that have been adopted or used by a wide user base, since this demonstrates that the package has design and performance characteristics that meet multiple use cases.
* Be sure to situate your package within the broader Python ecosystem: identify related tools, explain how your package differs from them, and explain how it complements, extends, or builds upon them.
* We particularly value **work that builds upon or extends existing tools rather than reinventing solutions** where quality alternatives already exist.

Below is the checklist that you will need to respond to in our submission form:

```{include} ../appendices/gen-ai-checklist.md

```

(telemetry)=
### Telemetry & user-informed consent

Your package should not collect usage analytics without first informing your users about what data are being collected and what is being done with that data. With that in mind, we understand that package-use data can be invaluable for the development process. If the package collects such data, it should do so by prioritizing user-informed consent. This means that before any data are collected, the user understands:

1. What data are collected
2. How the data are collected.
3. What you plan to do with the data
4. How and where the data are stored

Once the user is informed of what will be collected and how that data will be handled, stored and used, you can implement opt-in consent. opt-in means that the user agrees to usage-data collection prior to it being collected (rather than having to opt-out when using your package).

We will evaluate usage data collected by packages on a case-by-case basis and reserve the right not to review a package if the data collection is overly invasive.

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

* Find a new maintainer or
* Archive the tool, depending on what best suits your specific scientific
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

### Requesting package removal from the pyOpenSci ecosystem

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
