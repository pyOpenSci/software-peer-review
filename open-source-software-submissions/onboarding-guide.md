# pyOpenSci Review Guide for Onboarding New Editors and Reviewers

The pyOpenSci open peer review process is supported by volunteer editors and reviewers. Here we will discuss processes for onboarding new editors.

The success of our peer review process is dependent upon a 
well-balanced editorial board. Our board needs to have combined expertise in:

* A suite of specific science domains that fall within the scope of our peer review process
* Technical expertise in Python packaging.
* Awareness of the importance of documentation and package usability. 

## Recruiting new editors

Recruiting new editors and maintaining a sufficient and well-balanced editorial 
board will be the responsibility of the software review lead (position to be 
defined) with support and advice from the editorial board. 

```{note}
pyOpenSci is a newly restructured organization. While we've been performing peer 
review for almost 4 years, we are now beginning to formalize our process given
funding support from the Sloan foundation. In these early months, this software 
review lead role will be overseen by the Executive Director and the Editor in 
Chief. 
```

Steps to discuss a new editor:

* Start a private channel for discussion (so that it does not have a history in 
the editors channel that future editors will join, which could be awkward).
* Ping editors to be sure they get a notification as this is an important topic.
* Wait for a majority of editors to chime in before inviting someone. Provide 
editors one week to respond.

## Where to find new editors

* Consider contributors who have reviewed for pyOpenSci or submitted a package 
to pyOpenSci
* Consider contributors who have served as a guest editor


## Experience required to be an editor 

We prefer that editors have some experience with reviewing software. This experience
could come from a previous review they worked on with pyOpenSci, rOpenSci or JOSS. 

If they do not have experience as may be the case in the early months or establishing 
a robust editorial board, we  offer a "mentorship" process. Editor mentorship 
is where someone with existing editorial experience, mentors the new editor 
through their first review(s).

A new editor will be considered "guest" for the first 3 months or their tenure 
and/or until they have completed their first review. At that time, they can be 
considered to be a full editor as deemed appropriate by the software review lead
and the current editorial board.

# EDIT: Guest editors

<TODO >text here about what a guest editor is... 


## Inviting a new editor
 
* Candidates for the editorial board most often start by being guest editors.
* After 3 months or their first review (which ever comes first) assess how the 
review process went. Allow other editors to provide input as well. 
* Once it is determined that the guest editor is committed to support the pyOpenSci
review process, you can email them to fully participate on the editorial board
using the template below.

```
We would like to invite you to join the pyOpenSci editorial board as a full
member. [*SPECIFIC REASONS FOR INVITATION (mention contributions TO pyOpenSci)*]. 
We think you will make a wonderful addition to our pyOpenSci open review team!

[IF GUEST EDITOR: You are familiar with the editor's role as you've been a guest editor].  We aim for editors to handle reviews for four packages per year 
([IF GUEST EDITOR including the one that you just finished!]).  
We ask that editors make an informal commitment to serve for two years and 
re-evaluate their participation after that.  
On a short-term basis, any editor can decline to handle a package or say, 
"I'm pretty busy, I can't handle a new package for a few weeks."

In addition to handling packages, editors weigh in on group editorial decisions, 
such as whether a package is in-scope, and determining updates to our policies. 
We generally do this through Slack, which we expect editors to be able to check 
regularly. We have editorial board calls annually.  
We also rotate Editor-in-Chief responsibilities (first-pass scope decisions and 
assigning editors) amongst the board about quarterly. 
You'll have the opportunity to enter this rotation once you have been on the 
board for some time, usually at least six months. 
Some of us also take on bigger projects to improve the peer-review process, 
though this is entirely optional. 

We hope that you'll join our growing editorial board!

Please give this some thought, ask us any questions you have, and let us know 
whether you can join us.

Best,
[your-name-here], on behalf of the pyOpenSci Editorial Board
``` 

## Onboarding a new editor

* Inform rOpenSci community manager so that
    * editors are added to the [rOpenSci website](https://github.com/ropensci/roweb3/#team-member).
    * an introduction blog post can be put together.

* If they haven't already done so as guest editors, request that the new editor turn on [two-factor authentication (2FA) for GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa).

* Invite editors to the rOpenSci GitHub organization as member, as a member of the [`editors` team](https://github.com/orgs/ropensci/teams/editors) and the [`data-pkg-editors`](https://github.com/orgs/ropensci/teams/data-pkg-editors) or [`stats-board`](https://github.com/orgs/ropensci/teams/stats-board) sub-team, as appropriate.  This will give them appropriate permissions and allow them to get team-specific notifications. 

* Editors need access to the AirTable database of software review.

* Editors need access to the private editors channel in rOpenSci Slack workspace (and to the Slack workspace in general if they didn't previously, in that case ask rOpenSci community manager).

* Post a welcome message in the channel, pinging all editors.

* In the Slack workspace they need to be added to the editors team so that `@editors` will ping them too.

* We add editors' names to 
    * [dev_guide authors list](https://github.com/ropensci/dev_guide/blob/main/index.Rmd)
    * [dev_guide chapter introducing software review](https://github.com/ropensci/dev_guide/blob/main/softwarereview_intro.Rmd) (at two locations in this file, as editors and a bit below to remove them from the reviewers list)
    * [software-review README](https://github.com/ropensci/software-review/blob/main/README.Rmd) (in two places in this file as well)
Both the dev_guide and software-review README are automatically knit via continuous integration.

* Add editors to https://github.com/orgs/ropensci/teams/editors/members

## Offboarding an editor

* Thank them for their work!

* Remove them from the editors-only channel and the editors Slack team.

* Remove them from https://github.com/orgs/ropensci/teams/editors/members and sub-team.

* Inform rOpenSci community manager or some other staff emember so that they might be moved to alumni team members on the website.

* Remove their access to the Airtable workspace.

* Remove them from
    * [dev_guide chapter introducing software review](https://github.com/ropensci/dev_guide/blob/main/softwarereview_intro.Rmd) (at two locations in this file, as editors and a bit below to remove them from the reviewers list)
    * [software-review README](https://github.com/ropensci/software-review/blob/main/README.Rmd) (in two places in this file as well)
Both the dev_guide and software-review README are automatically knit via continuous integration.

