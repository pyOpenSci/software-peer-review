# Finding Reviewers

Sometimes the most challenging part of our pyOpenSci open peer review process
is finding reviewers. This page provides tips and tricks to help you find the
right people to review a scientific Python package.

## Where to Look for Reviewers?

As an editor, you can find reviewers through:

* Suggestions made by the submitting package authors. We suggest only using
  one of the suggested reviewers if this is the case.
* Authors of existing [pyOpenSci packages](https://www.pyopensci.org/python-packages/).
* Other [pyOpenSci contributors](https://www.pyopensci.org/our-community/).

When the above doesn't work and you still need to find a reviewer:

* Check our reviewer sign-up spreadsheet for names of people who have already
  volunteered to review for pyOpenSci. The link for this document is pinned to
  the pyOpenSci Slack `#private-editorial-channel`.
* Ping other editors for ideas.
* Post in the pyOpenSci Slack `#software-review` channel.
* Look for users of the package or the data source/upstream service the
  package connects to (via their opening issues in the repository, starring
  it, citing it in papers, talking about it on social media).
* Search for authors/maintainers of related packages on [PyPI](https://pypi.org/search/).
* Coordinate with our Community Manager to post a call for reviewers on our
  pyOpenSci social channels.

:::{important}

If you do a reviewer search, please be sure to have new reviewers first sign
up using our [reviewer signup form](https://docs.google.com/forms/d/e/1FAIpQLSeVf-L_1-jYeO84OvEE8UemEoCmIiD5ddP_aO8S90vb7srADQ/viewform).
:::

## Criteria for Choosing Reviewers

Here are criteria to keep in mind when choosing a reviewer. You might need to
piece this information together by searching `PyPI`, `Conda` / `Conda-forge`
and the potential reviewer’s GitHub page and general online presence (personal
website, social media profiles).

* Has not reviewed a package for us within the last 6 months.
* Some package development / contribution experience.
* Some domain experience in the field of the package or data source.
* No [conflicts of interest](coi).

(reviewer-diversity)=
### Reviewer Diversity Should Be Prioritized

Try to balance your sense of the potential reviewer’s experience against the
complexity of the package.

* **Diversity:** Try to find reviewers from different backgrounds and gender identities. For example, if you have two reviewers, only one should be a cis white male.
* **Openness** - reviewers should also have demonstrated interest in open
  source or Python community activities, although blind emailing is fine.

Each submission should be reviewed by _two_ package reviewers. Although it is
fine for one of them to have less package development experience and more
domain knowledge, the review should not be split into two parts. Both
reviewers need to review the package comprehensively, from their particular
perspectives. In general, at least one reviewer should have prior reviewing
experience, and of course inviting one new reviewer expands our pool of
reviewers.

Reviewers should ideally have some subject matter expertise associated with
the package functionality. It is ok and even welcome if one reviewer has more
technical expertise and the other focuses on usability and is less technical.
Read through the Guidelines for Reviewers Section to learn more about finding
and selecting reviewers.

(review-mentorship)=
## Peer Review Mentorship

pyOpenSci encourages those who are newer to review to become involved in our
open peer review process. As such, we offer a reviewer mentorship program
where we pair a new reviewer with someone in the community that has previous
review experience.

It is useful for reviewers to not only review the technical content of a
package, but also to review the documentation and package installation process
for usability.

If a new reviewer is interested in becoming a reviewer but would like some
support, do the following:

1. The Editor can lead the effort to find mentors for the new reviewers by posting in the `#software-review` Slack channel for help.
2. If the Editor needs support in finding a mentor, they can contact the **EiC** or **peer review lead** for guidance.

### Once a Mentor is Identified

1. Invite the new reviewer to our pyOpenSci Slack.
2. Start a private DM group chat with the new reviewer and the mentor(s) so
   they are introduced.
3. Let the review proceed from there.
