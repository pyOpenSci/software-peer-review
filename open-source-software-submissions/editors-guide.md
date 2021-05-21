# Guide for Editors

## Get Started Checklist
- Tag issue with `2/seeking-reviewer(s)` tag.
- Add a comment to the issue with your response to the Editor Checks.
  - Use the [editor template](../appendices/templates#editors-template).
  - Fill out the Editor Checks sections for `Fit`, `Automated Tests`, `License`, `Repository`
    - Check against policies for [fit](aims_scope#package-categories) and [overlap](aims_scope#package-overlap). If reject, see [this section](#responding-to-out-of-scope-submissions) about how to respond.
    - `Archive` and `Version` for JOSS may be filled out at the end of the review.
- Check the comment submission by the author to ensure that mandatory parts of submission template are complete.
  - If not, direct authors toward appropriate instructions.
- If initial checks show major gaps, request changes before assigning reviewers.
- Within one week of completing checks, identify two reviewers for the package (see sections below for additional guidance).
- Once reviewers have been identified:
  - Modify the Editor Comments under Editor Checks to add reviewer names and assign due date (typically 2-3 week turnaround).
    - `Reviewers: Full Name  (@github_username) and Full Name (@github_username)`
    - `Due date: Date`
    - Include in your comment to the reviewers:
      - link to guide for reviewers
      - link to review template
  - Edit the original comment submitted by author to fill in the Editor and Reviewer Information:
    - `Editor: Full Name (@github_username)`
    - `Reviewer 1: Full Name (@github_username)`
    - `Reviewer 2: Full Name (@github_username)`
    - `Archive` and `Version accepted` are filled out at the end of the review.
  - Tag issue with `3/reviewer(s)-assigned` tag

## General Guidelines for Editor
- Run automated tests: spelling, linting, etc ... will be filled in later.
- For packages needing continuous integration on multiple platforms ([criteria in this section of the packaging chapter](../authoring/overview#continuous-integration)), make sure the package gets tested on multiple platforms (having the package built on both Travis and AppVeyor for instance).
- Wherever possible when asking for changes, direct authors to automatic tools and online resources.
- If the package raises a new issue for pyOpenSci policy, create an issue on [pyOpenSci's governance repo](https://github.com/pyOpenSci/governance)

## Guidelines For Identifying Reviewers

### Tasks
- Use the [email template](../appendices/templates#review-request-template) if needed to invite reviewers.
    -  When inviting reviewers, include something like "if I don't hear from you in a week, I'll assume you are unable to review," so as to give a clear deadline when you'll move on to looking for someone else.

### Where to Look for Reviewers?

As a (guest) editor, use:
* the potential suggestions made by the submitter(s), (although submitters may have a narrow view of the types of expertise needed.  We suggest not using more than one of suggested reviewers).
* the authors of [pyOpenSci packages](https://github.com/pyOpenSci/).

When these sources of information are not enough:
* ping other editors for ideas.
* look for users of the package or of the data source/upstream service the package connects to (via their opening issues in the repository, starring it, citing it in papers, talking about it on Twitter).
* You can also search for authors/maintainers of related packages on [PyPI](https://pypi.org/search/).

#### Criteria for Choosing Reviewers

Here are criteria to keep in mind when choosing a reviewer. You might need to piece this information together by searching CRAN and the potential reviewer’s GitHub page and general online presence (personal website, Twitter).

* Has not reviewed a package for us within the last 6 months.
* Some package development experience.
* Some domain experience in the field of the package or data source.
* No [conflicts of interest](../open-source-software-peer-review/policies-and-guidelines.html#conflict-of-interest)

https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/policies-and-guidelines.html#conflict-of-interest

      open-source-software-peer-review/policies-and-guidelines.html#conflict-of-interest.
* Try to balance your sense of the potential reviewer’s experience against the complexity of the package.
* Diversity - with two reviewers both shouldn’t be cis white males.
* Some evidence that they are interested in openness or Python community activities, although blind emailing is fine.

Each submission should be reviewed by _two_ package reviewers. Although it is fine for one of them to have less package development experience and more domain knowledge, the review should not be split in two.  Both reviewers need to review the package comprehensively, though from their particular perspective.  In general, at least one reviewer should have prior reviewing experience, and of course inviting one new reviewer expands our pool of reviewers.

## Editor Responsibilities During Review:

-   Check in with reviewers and authors occasionally. Offer clarification and help as needed.
-   In general aim for 3 weeks for review, 2 weeks for subsequent changes, and 1 week for reviewer approval of changes.
-   Upon all reviews being submitted, change the review status tag to `4/review-in-awaiting-changes` to update the reminder bot.
-   If the author stops responding, refer to [the policies](peer_review_proc#review-process-guidelines) and/or ping the other editors in the Slack channel for discussion. Importantly, if a reviewer was assigned to a closed issue, contact them when closing the issue to explain the decision, thank them once again for their work, and make a note in our database to assign them to a submission with high chances of smooth software review next time (e.g. a package author who has already submitted packages to us).
-   Upon changes being made, change the review status tag to `5/awaiting-reviewer-response`.

### Editor Responsibilities After Review:

-   Change the status tag to `6/approved`.
-   You can use the [approval comment template](../appendices/templates#approval-comment-template).
-   Add review/er information to the review database.
-   If package will be migrated to `pyOpenSci`:
    -   Create a two-person team in pyOpenSci's "pyOpenSci" GitHub organization, named for the package, with yourself and the package author as members.
    -   Have the author transfer the repository to `pyOpenSci`
    -   Go to the repository settings in the "pyOpenSci" GitHub organization and give the author "Admin" access to the repository.
- Fill out `Archive` and `Version` for JOSS under Editor Checks comment.
- Fill out `Archive` and `Version accepted` in the original comment submitted by author.
-   Ask author to:
    -  Change any needed links, such those for CI badges
    -  Add pyOpenSci badge: `[![pyOpenSci](https://tinyurl.com/y22nb8up)](link-to-issue)`.
    -   Re-activate CI services
        -  For Travis, activating the project in the pyOpenSci account should be sufficient
        -  For AppVeyor, tell the author to update the GitHub link in their badge, but do not transfer the project: AppVeyor projects should remain under the authors' account. The badge is `[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/pyOpenSci/pkgname?branch=master&svg=true)](https://ci.appveyor.com/project/individualaccount/pkgname)`.
        -  For Codecov, the webhook may need to be reset by the author.
-   Add a "peer-reviewed" topic to the repository.
-   Close the software-review issue.
