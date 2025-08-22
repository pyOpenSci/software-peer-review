# pyOpenSci Software Review Editor Guide

Thank you for your time in serving as an editor for a pyOpenSci package! Below, you will find some
information about the role that editors have in the
pyOpenSci Python open peer review process.

## Experience needed to become an editor

Editors generally should:

- Have completed a review for _at least_ 1 package for pyOpenSci.
- Have some experience with open-source software that supports the scientific
  Python community. This experience could be maintaining or contributing to packages. It could also be experience related to usability of open-source software and/or documentation, tutorials, etc. Alternatively, it could involve participation in the broader scientific Python community in another capacity.

## Two types of editors

There are two types of editors involved in our open peer review process:

- Guest editors and
- Full editors

Both types of editors are considered a part of the editorial board for
pyOpenSci. The significant differences between guest and full editors are:

- A guest editor may only join the board for a single review.
- A guest editor may be new to pyOpenSci's review process and thus require a bit more support in their first review.

### Guest editors

A guest editor is invited to lead a review in the
case where we need specific expertise for a single review. We also consider editors who are
performing their first review as guest editors, as they may require more
guidance or mentorship to complete the review (if they are new to our organization).

New editors who wish to continue as full editors for pyOpenSci may do so
as long as both parties (pyOpenSci and the guest editors) feel like it is a
healthy fit for them and the organization.

### "Full" editors

A full editor is most often someone who has experience with the
pyOpenSci open package review process. A full editor ideally:

- has completed a review for _at least_ 1 package for pyOpenSci
- and/or has submitted and gone through the pyOpenSci package review process
- and/or has experience reviewing for an organization such as JOSS or rOpenSci.

We also appreciate when editors have experience working with or in the
Python open source software community, be it maintaining packages, contributing to
packages, or supporting the community. This is
not a requirement, however if you are interested in getting involved with
pyOpenSci!

```{note}
There could be certain situations when an editor is onboarded with less experience! The above are simply guidelines that we like to follow.
```

## What does an editor do? (Responsibilities)

An editor is usually recruited by the Editor in Chief, other editors on the
board, or the software review lead. [More on recruiting editors can be found here](onboarding-guide.md).

An editor is responsible for:

- Leading the review process for 3-4 packages a year
- Weighing in on group editorial decisions such as whether a package is in scope, and making updates to the pyOpenSci policies.

```{note}
Decisions surrounding policy, updates to peer review guides, and decisions
on package review are generally made in the private `editorial-board` channel in the pyOpenSci Slack organization. Please make sure that you
are comfortable with checking Slack regularly.
```

## Editor support of other reviews

Editors are not charged with tracking other submissions that they are
not leading. However, if you are serving as an editor and notice an
issue with another review, please raise that issue either directly with
the editor for that review. Or you can raise the issue in the `private-editorial-team` Slack
channel.

## Editor-in-Chief rotation

The editorial board normally participates in the Editor in Chief rotation.
You are eligible to enter this rotation after 3 months of serving on the editorial board
and/or after your first review as it makes sense. [Read more about the roles
and responsibilities of the Editor in Chief, here.](editor-in-chief-guide.md)

If the Editor in Chief role feels like too much responsibility, an editor can also decline being a part of this rotation.

## How long does an editor serve on the editorial board?

Ideally, an editor can commit to serving for **at least** one year as an editor
for pyOpenSci. During that year, we expect that you will lead the review of 3-4 packages. However, we understand that in certain situations, an editor
may need to step down before the 1 year time period has ended.

We also understand that life gets busy. You are always welcome to "say no"
to a review during a busy time.

We welcome
editors staying on for longer as long as they are happy serving with us and
they get along well with other members of the editorial board, the software
review lead and the current Editor in Chief.

## Editor checklist: Get Started With Leading a Package Review

Follow the checklist below when serving as an editor for a package submitted to
pyOpenSci for review.

All reviews happen in GitHub issues. The template for the
`yaml` header of a review submission below will be
referenced multiple times in the steps below:

```{include} ../appendices/issue-review-template.md

```

### ✔️ 1. First, tag the submission issue on GitHub & assign yourself to the issue

Once you begin the review process as an editor:

- Tag the submitted GitHub issue with the `1/editor-checks` tag if it hasn't already been tagged by the editor-in-chief.
- Make sure that you are assigned to the issue on GitHub (ie, your name is on the right-hand side of the issue as the person running it).

:::{figure-md} assign-editor

<img src="../images/assign-issue.png" alt="Screenshot showing the right-hand side of a GitHub issue with the editor assigned to the issue." width="700px">

Make sure that your name is both listed in the YAML at the top of the issue and also that you are assigned to the issue on GitHub (on the right-hand side of the issue).
:::


- Check the YAML template at top of the submitted GitHub issue, make sure that mandatory parts of the template are filled out.
  - If elements are incomplete, direct the authors toward filling in any missing pieces.

```markdown
Submitting Author: SUBMITTING AUTHOR NAME HERE (Name @github_handle)
All current maintainers: ALL CURRENT MAINTAINERS LISTED HERE (Name @github_handle1, Name @github_handle2)
Package Name: PACKAGE-NAME-HERE
One-Line Description of Package: DESCRIPTION OF THE PACKAGE HERE
Repository Link: REPO-LINK
Version submitted: VERSION-SUBMITTED
```

```{admonition} Editor in Chief checks for structure & scope should be completed first
:class: note

The editor in chief who initially engaged with this review should have already evaluated the package-level Editor Checks section for `Fit`, `Automated Tests`, `Documentation`, `License`, and `Repository`.

They also should have checked whether the package is [in scope for pyOpenSci](../about/package-scope).
And whether there is [functionality overlap with functionality of any other existing Python packages](package-overlap).

However, in some instances, the editor-in-chief may request that an editor
perform these tasks. Be sure to check the issue to ensure the above checks have been implemented before initiating the review.

If the package does not fit the pyOpenSci scope and policies and needs to be
rejected, see
[this section in the editor-in-chief guide](editor-in-chief-guide.md#responding-to-out-of-scope-submissions)
about how to respond.
```

### ✔️ 2. Respond to the submitter in the GitHub issue

Once the above is complete, you are ready to add an editor response to the issue.
This step ensures that the package is ready to be reviewed. It also ensures that
we are using our volunteer reviewer time effectively.

- Add a comment to the issue that contains an **exact** copy of the Editor Response template (see below) filled out with your response to the checks that begin the review.
- Change the label of the issue to `2/seeking-reviewer(s)`
- Note that, at this stage, you likely do not have reviewers yet!

```{include} ../appendices/editor-initial-response-template.md

```

```{important}
**Important: If in the initial checks you find any major gaps in the package's
structure, request changes before assigning reviewers.**
```

### ✔️ 3. Identify reviewers for the Python package

Each review should have at least two reviewers.

- One reviewer should have expertise in both Python and the scientific domain related to the package submitted.
- The second reviewer can be more generally focused on the package's usability, accessibility, and packaging infrastructure. This allows people who are newer to review to get involved while also providing a critical usability check for the package.

A review consisting of a domain expert and a Pythonista is ideal as it provides two distinct perspectives for review. Furthermore, it can often be challenging to find individuals with both the specific domain expertise and packaging expertise.

#### Finding package reviewers

Oftentimes, finding reviewers for a package can be the trickiest part
of the review process. Expect this step to take time and patience. [Check out this page for tips related to finding and onboarding reviewers.](finding-reviewers)

If you can, try to find two people to serve as reviewers within **two weeks
of responding to the issue as the editor**. If it takes longer, as
often does, make a point to keep the author posted on the issue
as you continue your search. You may add language such as:

> Hey, @authorGithubHandle I just wanted to drop in to let you know that I'm searching for reviewers for your package. It may take a bit more time.

This type of communication just lets the author know that the process is
moving forward. Even if it takes longer to find reviews, authors generally
appreciate the communication and understand it's a volunteer-led process.

```{admonition} Diversity in the editorial & reviewer team is important
:class: important

Diversity is core to the pyOpenSci mission. As such, it's important to have an
editorial team comprised of an editor + 2 reviewers from diverse backgrounds.

In your search for reviewers, please ensure that there is diversity
in the team supporting package review. Reviewers should have [different backgrounds and different gender identities](reviewer-diversity) whenever possible. pyOpenSci [supports mentoring new reviewers if needed!](review-mentorship)

[Read our finding reviewers guide for more on finding reviewers.](finding-reviewers)
```

If you'd like to, you can use the email template below to invite reviewers.

```{include} ../appendices/reviewer-request-template.md

```

When inviting reviewers, include something like "If I don't hear from
you in a week, I'll assume you are unable to review," to give a clear
deadline when you'll move on to looking for someone else to keep the processing
moving.

- Once you have assigned reviewers to the review, you will update the editor response above with:

1. Reviewer GitHub handles and
2. The review deadline date.

:::{tip}
At this point, you can add the following to the **Editor Response to Review** under **Editor Comments**:
`:wave: Hi @reviewer-one and @reviewer-two! Thank you for volunteering to review
for pyOpenSci!`
:::

- Change the label on the issue to `3/reviewer(s)-assigned`

```{warning}
Make sure to ask the reviewers for their preferred means of contact or a reliable way to get in touch with them.
```

### ✔️ 4. Onboard reviewers

Once reviewers have been identified:

- Tag issue with `3/reviewer(s)-assigned` tag.
- Add reviewer names and review due date to the Editor Comment that you left above in step 2.
- Also add the reviewer names to the YAML template at the very top of the issue.

```markdown
Editor: Full Name (@github_username)
Reviewer 1: Full Name (@github_username)
Reviewer 2: Full Name (@github_username)
Archive: Filled out when the review is complete.
Version accepted: Filled out when the review is complete.
```

## Editor responsibilities during the review

During the review process, it is important to check in with the reviewers to
ensure that things are moving smoothly:

- Check in with reviewers and authors occasionally. Offer clarification and help as needed.
- Aim for ~3 weeks for review, 2 weeks for subsequent changes, and 1 week for reviewer approval of changes.
- If a review has not been submitted after 2 weeks, ping the reviewer(s) within the review issue to ensure they are aware of the 3-week deadline.
- If you are waiting for a maintainer to respond to you, be sure to add the label `pending-maintainer-response` to the issue.

### ✔️ 5. What to do when reviews are in

- Once all reviews are submitted, change the review status tag to `4/review-in-awaiting-changes`.

If the author stops responding, refer to [the policies](/our-process/policies) and/or ping the other editors in the Slack channel <_Not available publicly yet_> for discussion.

Once the author has responded to the reviews and made appropriate changes:

- Briefly check to ensure that the changes were indeed made.
- Change the issue status tag to `5/awaiting-reviewer-response`.

```{important}
If you need to stop the review and close the issue for some reason during the process, please be sure to let all parties know (the maintainer and reviewers) before closing the issue.

Be sure to:

* explain why the decision was made
* thank them for their work
* make a note <TBD where this will be documented> to assign the reviewer to another submission with a high chance of smooth
review next time (for example, a package author who has already submitted packages to us).
```

(reviewer-response-time)=
## What to do if reviewers become quiet
In some cases, the reviewers get busy and stop responding to the issue. If a reviewer hasn't responded to a direct ping `@reviewer-user-name` on the issue, try to email them (if an email is available). If email doesn't work and they haven't responded in over a month, do the following:

1. If they have already submitted a review, you can move the review forward by making sure the review comments were addressed by the author yourself.
2. If the reviewer has not yet submitted a review on the issue, leave a note on the review that you will look for a new reviewer. When you find a new reviewer, replace the old reviewer's name with the new reviewer's name in the YAML at the top of the issue.

In some cases, you may be able to find an editor or reviewers in the pyOpenSci Slack community that can help move the review forward.

## Putting a review on hold & handling non-responsive authors

In some cases, an author may need more time to respond to
review comments. In this case, the author can choose to have
their submission put on hold. As an editor, you should apply the `holding label` to the GitHub issue.

The holding status will be revisited every 3 months.

After one year, the issue will be closed if there is no movement towards responding to reviews by the author.

If the author is not responding, the editor should:

- Tag the author (`@author-github-handle`) in an issue comment notifying them that we will close the issue in one month if there is no response.
- Close the issue if two months have passed without a reply.

Before closing the issue, email the author using the email provided in the package metadata file of the package. The email
could be in any of the three files in the package: `setup.py`, `pyproject.toml` (preferred), or `setup.cfg`.

```{important}
If a submission is closed and the author wishes to resubmit, they will have to start a new submission.

If the package is still in scope, the author will have to
respond to the first round of reviews first. After that is
complete, you can begin looking for new reviewers to
evaluate the package. This ensures that none of the review
energy spent in the first review goes to waste.
```

### ✔️ 6. How to accept a package into the pyOpenSci ecosystem

Once the package has been accepted through the review process:

- Use the approval template below in the issue. This template
  asks the authors and reviewers to add themselves and the package that was
  approved to the pyOpenSci website. They can perform this step regardless of the
  JOSS submission process.

```{include} ../appendices/package-approval-template.md

```

- If the package moves on to JOSS - be sure to continue to update the labels to track the JOSS review process (but do NOT remove the `6/pyOS-approved` label).
- Update the YAML at the top of the issue with the:
  - version of the package that was approved,
  - Zenodo DOI for the approved version and
  - the date approved.

```markdown
Archive: UPDATE-THIS-WITH-A-ZENODO-ARCHIVE-BADGE-TBD
Version accepted: UPDATE-THIS-TBD
Date accepted (month/day/year): UPDATE-THIS-TBD
```

- Once the YAML is updated, change the status tag of the issue to `6/pyOS-approved` 🚀🚀🚀`.
  - The [listing on the PyOpenSci website](https://www.pyopensci.org/python-packages.html) is updated by a cron job that parses the YAML in all issues with the tag `6/pyOS-approved` 🚀🚀🚀`, so a new package might take a few days to appear; in particular, if there are formatting errors in the YAML that need to be corrected.
  - Editors can manually trigger the [cron job](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-contribs-reviews.yml) and/or check the output of the last run to see if there are any YAML formatting errors.
  - Other "after review" tasks, like the post-review survey, can be done after the package is accepted; the cron job does not depend on them.

```{note}
* `Archive` refers to an archive created through a release. You can [use Zenodo to create this archive](https://www.pyopensci.org/lessons/package-share-code/publish-share-code/cite-code.html#cite-your-code) and provide the package with a citable DOI. If Zenodo is used, please add the Zenodo link and/or badge link here.

* `Version` refers to the final package version that was accepted by pyOpenSci.
This is the final version as presented after all feedback from the
reviews has been considered and implemented.
```

## Closing notes about the editorial process

- If the package raises a new issue for pyOpenSci policy, create an issue on [pyOpenSci's handbook repo](https://github.com/pyOpenSci/handbook).
- If the package review raises a new issue in our peer review process, please [open an issue in our peer review guide repo.](https://github.com/pyOpenSci/peer-review-guide).

## ✔️ OPTIONAL: Instructions for Submitting to JOSS

If the package fits within the JOSS Scope, once the package has been approved
by pyOpenSci:

- Tag the issue `7/under-joss-review`.
- Instruct the author to <a href="https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain" target="_blank">read the `paper.md` file requirements</a> for JOSS and ensure that paper is added to the repo.
- Direct the package author to [follow the instructions to submit the package to JOSS](https://joss.readthedocs.io/en/latest/submitting.html).

These instructions loosely include:

1. Login to the JOSS website and fill out the JOSS submission form. When you fill out the form, be sure to mention and link to the approved pyOpenSci review.
2. Wait for a JOSS editor to approve the presubmission (which includes a scope check).

```{important}
The scope of packages accepted by pyOpenSci is sometimes different from those
accepted by JOSS. Not all pyOpenSci accepted packages will be accepted by JOSS.
Further, packages that have been previously published elsewhere may not be
eligible to be published with JOSS unless **significant** changes and improvements
to package functionality have been made.
```

JOSS will accept the pyOpenSci review and direct the author to check their `paper.md` file. Once JOSS accepts the package,
the author will be instructed to add the JOSS DOI badge to their package **README** file.

Once the package is accepted by JOSS and the DOI badge resolves properly:

- Tag the issue with `9/joss-approved`. (Please do NOT remove the `pyos-approved` label, instead add the `JOSS-approved` label)

## Last Steps Before Closing the Review Issue

Once the review is complete, you can close the issue. Before doing that:

- Be sure that the issue is correctly tagged with `6/pyOS-approved` (and `9/joss-approved` if authors decided to submit to JOSS and were accepted).

- Check the pyOpenSci website to ensure:

  - The package was added to the [pyOpenSci website](https://www.pyopensci.org/python-packages/).
  - Reviewers and maintainers are listed on the [contributors page](https://www.pyopensci.org/our-community/).
  - Make sure the YAML at the top of the issue is filled out and up to date.

- If JOSS approves the package, be sure that the issue is tagged with `7/JOSS-approved` and that the archive / DOI information at the top is updated with the JOSS archive before closing the issue.

Congratulations, you have completed a review for pyOpenSci!
