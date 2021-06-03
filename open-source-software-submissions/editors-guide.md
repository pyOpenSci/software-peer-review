# Guide for Editors

Thank you for your time in serving as an editor for a PyOpenSci package! An editor
for pyOpenSci should have the following experience:

* They should have completed a review for *atleast* 1 package for pyOpenSci.
* They should have some experience with the open source software for scientific
Python community be it maintaining or contributing to packages, or being involved
in the community in some way.

## Get Started Checklist

Follow the checklist below when serving as an editor for a package submitted to
pyOpenSci for review.

### 1. Tag the Submission

Once you begin the review process as an editor:

* Tag the submission issue with the `2/seeking-reviewer(s)` tag.
* Check the comment submission by the author to ensure that mandatory parts of submission template are complete.
  - If elements are not complete, direct authors toward filling in any missing pieces.

### 2. Complete Editor Checks

Once the above is complete you are ready to add editor checks to the issue.
The goal of this step is to ensure that the package is ready to be reviewed.
Following through with this step will ensure that we are using our volunteer
reviewer time effectively.

- Add a comment to the issue that contains a copy of the Editor Checks template (see below) filled out with your response to the checks that begin the review.
- In this comment you will add reviewers and the review deadline date once you have reviewers assigned (see below)

```markdown
## Editor checks:

- [ ] **Fit**: The package meets criteria for [fit](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-categories) and [overlap](https://www.pyopensci.org/contributing-guide/open-source-software-peer-review/aims-and-scope.html#package-overlap).
- [ ] **Automated tests:** Package has a testing suite and is tested using CI (e.g. GitHub Actions, Travis-CI, CircleCI, etc).
- [ ] **Documentation:** Package has documentation setup (ReadTheDocs, JupyterBook, website,etc.).
- [ ] **License:** The package has an OSI accepted license
- [ ] **Repository:** The repository link resolves correctly
- [ ] **Archive** Zenodo or JOSS. (may be post-review): The repository DOI resolves correctly
- [ ] **Version** (may be post-review) Does the release version given match the GitHub release (v1.0.0)?

---

## Editor comments
:wave: Hi @reviewer-one and @reviewer-two! Thank you for volunteering to review
for PyOpenSci! <Add any additional banter here that you wish..>

The following resources will help you complete your review:

1. Here is the **[reviewers guide](https://www.pyopensci.org/contributing-guide/open-source-software-submissions/reviewer-guide.html)**. This guide contains all of the steps and information needed to complete your review.
2. Here is the **[review template](https://www.pyopensci.org/contributing-guide/appendices/templates.html#review-template)** that you will need to fill out and submit
here as a comment, once your review is complete.

Please get in touch with any questions or concerns! Your review is due: <Insert deadline DATE HERE>
---

Reviewers:
Due date:
```

- Fill out the Editor Checks sections for `Fit`, `Automated Tests`, `Documentation`, `License`, and `Repository`
- Check against policies for [package fit within identified categories for the pyOpenSci ecosystem](../open-source-software-peer-review/aims-and-scope.html#package-categories)
- Check against policies for [package overlap of functionality with other packages](../open-source-software-peer-review/aims-and-scope.html#package-overlap).

If the package does not fit the pyOpenSci scope and policies and needs to be
rejected, see
[this section in the editor in chief guide](editor-in-chief-guide.html#responding-to-out-of-scope-submissions)
about how to respond.

- `Archive` and `Version` within the editor checks for JOSS may be filled out at the end of the review.
  * `Archive` refers to the DOI / citation badge provided through the JOSS
  review. If the package is not submitted to JOSS and has a DOI from another
  source such as ZENODO, then you can reference the url for that DOI in the final
  checks.
  * `Version` refers to the final package version that was accepted by pyOpenSci.
  This is the final version as presented after all feedback from the reviews has
  been considered and implemented.

```{note}
PyOpenSci has a partnership with JOSS where packages that are in-scope for JOSS
can be directly accepted into the JOSS ecosystem through the pyOpenSci review.
The JOSS component of the review happens last after all of the review on the
pyOpenSci side is complete and is begun through direct communication with a
JOSS editor.
```

**Important: If initial checks show major gaps, request changes before assigning reviewers.**

### 3. Identify Reviewers

Within **one week of completing the editor checks**, identify two reviewers for
the package  

If you wish, you can use the [email template](../appendices/templates#review-request-template) to invite reviewers. When inviting reviewers, include something like "if I don't hear from
you in a week, I'll assume you are unable to review," so as to give a clear
deadline when you'll move on to looking for someone else to keep the processing
moving.

#### Where to Look for Reviewers?

As a (guest) editor, you can find reviewers through:
* Suggestions made by the submitter(s), (although submitters may have a narrow view of the types of expertise needed. We suggest not using more than one of suggested reviewers).
* Authors of existing [pyOpenSci packages](https://www.pyopensci.org/python-packages/).
* Other [contributors to pyOpenSci](https://www.pyopensci.org/contributors/)

When these sources of information are not enough:
* ping other editors for ideas.
* look for users of the package or of the data source/upstream service the package connects to (via their opening issues in the repository, starring it, citing it in papers, talking about it on Twitter).
* You can also search for authors/maintainers of related packages on [PyPI](https://pypi.org/search/).
* Post in twitter and ensure pyOpenSci retweets your post.

#### Criteria for Choosing Reviewers

Here are criteria to keep in mind when choosing a reviewer. You might need to
piece this information together by searching `PyPI`, `Conda` / `Conda-forge` and
the potential reviewer’s GitHub page and general online presence (personal
website, Twitter).

* Has not reviewed a package for us within the last 6 months.
* Some package development / contribution experience.
* Some domain experience in the field of the package or data source.
* No [conflicts of interest](../open-source-software-peer-review/policies-and-guidelines.html#conflict-of-interest)

Try to balance your sense of the potential reviewer’s experience against the complexity of the package.

* **Diversity** - if you have two reviewers both shouldn’t be cis white males.
* Reviewers should also have demonstrated interest in openness or Python community activities, although blind emailing is fine.

Each submission should be reviewed by _two_ package reviewers. Although it is
fine for one of them to have less package development experience and more domain
knowledge, the review should not be split in two parts.  Both reviewers need to review
the package comprehensively, though from their particular perspective. In
general, at least one reviewer should have prior reviewing experience, and of
course inviting one new reviewer expands our pool of reviewers.

Reviewers should ideally have some subject matter expertise associated
with the package functionality. It is ok and even welcome if one reviewer has
more technical expertise and the other focuses on usability and is less technical.
Read through the Guidelines for Reviewers Section to learn more about finding and
selecting reviewers.

```{note}
PyOpenSci has been piloting a new reviewer mentorship program where we pair a
new reviewer with someone in the community with previous review experience. If
a new reviewer is interested in this, get in touch with the **editor in chief**.
```


### 4. Onboard Reviewers

Once reviewers have been identified:

- Modify the Editor Comments under Editor Checks to add reviewer names and assign due date (typically a 2-3 week turn around).
- Also add the reviewers to the initial top comment in the issue.


```markdown
Reviewers: Full Name  (@github_username) and Full Name (@github_username)
Due date: Date`
Include in your comment to the reviewers:
      - Link to the reviewer guide for reviewers
      - Link to the review template
```

- Edit the original comment submitted by author to fill in the Editor and Reviewer Information:

```markdown
Editor: Full Name (@github_username)
Reviewer 1: Full Name (@github_username)
Reviewer 2: Full Name (@github_username)
Archive: Filled out when the review is complete.
Version accepted: Filled out when the review is complete.
```

- Tag issue with `3/reviewer(s)-assigned` tag


## Editor Responsibilities During the Review:

During the review process, it is important to check in with the reviewers to
ensure that things are moving smoothly:

-   Check in with reviewers and authors occasionally. Offer clarification and help as needed.
-   In general aim for 3 weeks for review, 2 weeks for subsequent changes, and 1 week for reviewer approval of changes.
- If a review has not been submitted after 2 weeks, ping the reviewer(s) within the review issue to ensure they are aware of the 3 week deadline.
-   Once all reviews are submitted, change the review status tag to `4/review-in-awaiting-changes` to update the reminder bot. <WHAT IS THIS BOT?!>
-   If the author stops responding, refer to [the policies](peer_review_proc#review-process-guidelines) and/or ping the other editors in the Slack channel <*Not available publically yet*> for discussion.

::::{important}
If a reviewer was assigned to a closed issue, contact them when closing the
issue to explain the decision, thank them once again for their work, and make a
note in our database to assign them to a submission with high chances of smooth
software review next time (e.g. a package author who has already submitted packages to us).
::::

-   Upon changes being made, change the review status tag to `5/awaiting-reviewer-response`.

### General Review guidelines

- For packages needing continuous integration on multiple platforms ([criteria in this section of the packaging chapter](../authoring/overview#continuous-integration)), make sure the package gets tested on multiple platforms (e.g. MAC, Windows, Linux).
- Wherever possible when asking for changes in the review process, direct authors to automatic tools and online resources.
  - If the package raises a new issue for pyOpenSci policy, create an issue on [pyOpenSci's governance repo](https://github.com/pyOpenSci/governance)

## Editor Responsibilities After the Review:

Once the package has been accepted through the review process:

- Change the status tag of the issue to `6/pyOS-approved`
- Update the top of the issue with the version of the package that was approved and the doi.


### Instructions for Submitting to JOSS:
If the package fits within the JOSS Scope, once the package has been approved
by pyOpenSci:

* Tag the issue `7/under-joss-review`
* Instruct the author to <a href="https://joss.readthedocs.io/en/latest/submitting.html#what-should-my-paper-contain" target="_blank">read the `paper.md` file requirements</a> for JOSS and ensure that paper is added to the repo.
* Direct the package author to [follow the instructions to submit the package to JOSS](https://joss.readthedocs.io/en/latest/submitting.html).

These instructions loosely include:

1. Login to the JOSS website and fill out the JOSS submission form. When you fill out the form, be sure to mention and link to the approved pyOpenSci review.
2. Wait for a JOSS editor to approve the presubmission (which includes a scope check)


::::{important}
The scope of packages accepted by pyOpenSci is in some cases different from those
accepted by JOSS. Not all pyOpenSci accepted packages will be accepted by JOSS.
Further, packages that have been previously published elsewhere may not be
eligible to published with JOSS unless **significant** changes and improvements
to package functionality have been made.
::::

JOSS will accept the pyOpenSci review and direct the author through the
process of checking their `paper.md` file. Once the package is accepted by JOSS,
the author will be instructed to add the JOSS DOI badge to their package **README** file.

Once the package is accepted by JOSS, and the DOI badge resolves properly:



If the package was accepted by JOSS:

* Fill out `Archive` and `Version` for JOSS under Editor Checks comment.
* Fill out `Archive` and `Version accepted` in the original comment submitted by author.
* Tag the issue with `9/joss-approved`


- You may wish to use the approval template below in the issue. This template
  asks the authors and reviewers to add themselves and the package that was
  approved to the pyOpenSci website. They can do this step regardless of the
  JOSS submission process.

```
----------------------------------------------
🎉 <package-name-here> has been approved by pyOpenSci! Thank you <maintainer-name-here> for submitting <package-name> and many thanks to <reviewer-names-here> for reviewing this package! 😸  

There are a few things left to do to wrap up this submission:
- [ ] Activate Zenodo watching the repo if you haven't already done so.
- [ ] Tag and create a release sto create a Zenodo version and DOI.
- [ ] Add the badge for pyOpenSci peer-review to the README.md of <package-name-here>. The badge should be `[![pyOpenSci](https://tinyurl.com/y22nb8up)](https://github.com/pyOpenSci/software-review/issues/issue-number)`
- [ ] Add <package-name> to the pyOpenSci website. <maintainer-name>, please open a pr to update [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/packages.yml): to add your package and name to the list of contributors
- [ ] <reviewers-and-maintainers> if you have time and are open to being listed on our website, please add yourselves to [this file](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/contributors.yml) via a pr so we can list you on our website as contributors!

<IF JOSS SUBMISSION>
It looks like you would like to submit this package to JOSS. Here are the next steps:

- [ ] Login to the JOSS website and fill out the JOSS submission form using your Zenodo DOI. **When you fill out the form, be sure to mention and link to the approved pyOpenSci review.** JOSS will tag your package for expedited review if it is already pyOpenSci approved.
- [ ] Wait for a JOSS editor to approve the presubmission (which includes a scope check)
- [ ] Once the package is approved by JOSS, you will be given instructions by JOSS about updating the citation information in your README file.
- [ ] When the JOSS review is complete, add a comment to your review in the pyOpenSci software-review repo that it has been approved by JOSS.

🎉 Congratulations! You are now published with both JOSS and pyOpenSci! 🎉
<IF JOSS SUBMISSION/>

All -- if you have any feedback for us about the review process please feel free to share it here. We are always looking to improve our process and our documentation in the [contributing-guide](https://www.pyopensci.org/contributing-guide). We have also been updating our documentation to improve the process so all feedback is appreciated!
```

#### Last Steps Before Closing the Review Issue
Once the review is complete, you can close the issue. Before doing that:

* Be sure that the issue is tagged with `6/pyOS-approved`
* Followup with authors and reviewers to ensure:
    * that the package was properly added [pyOpenSci website](https://www.pyopensci.org/python-packages/) and
    * reviewers and maintainers are listed on the [contributors page](https://www.pyopensci.org/contributors/)
* If the package is approved by JOSS, be sure that the issue is tagged with `7/JOSS-approved` and the archive / doi information is updated before closing the issue.

Congratulations, you have completed a review for pyOpenSci!


#### Optional - Move Package to PyOpenSci Organization (BETA)

rOpenSci packages often live in the rOpenSci organization. PyOpenSci is still
figuring out whether this model fits for the Python community. If an author is
interested in this option, consider doing the following:

-   If package will be migrated to `pyOpenSci`:
    -   Create a two-person team in pyOpenSci's "pyOpenSci" GitHub organization, named for the package, with yourself and the package author as members.
    -   Have the author transfer the repository to `pyOpenSci`
    -   Go to the repository settings in the "pyOpenSci" GitHub organization and give the author "Admin" access to the repository.
-   Ask author to:
    -  Change any needed links, such those for CI badges
    -  Add pyOpenSci badge: `[![pyOpenSci](https://tinyurl.com/y22nb8up)](link-to-issue)`.
    -   Re-activate CI services
        -  For Travis, activating the project in the pyOpenSci account should be sufficient
        -  For AppVeyor, tell the author to update the GitHub link in their badge, but do not transfer the project: AppVeyor projects should remain under the authors' account. The badge is `[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/pyOpenSci/pkgname?branch=main&svg=true)](https://ci.appveyor.com/project/individualaccount/pkgname)`.
        -  For Codecov, the webhook may need to be reset by the author.
-   Add a "peer-reviewed" topic to the repository.
