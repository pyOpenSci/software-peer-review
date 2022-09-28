# Onboarding New Editors and Reviewers

The pyOpenSci open peer review process is supported by volunteer editors. Here we discuss processes for onboarding new editors.

The success of our peer review process is dependent upon a 
well-balanced editorial board. Our board needs to have combined expertise in:

* A suite of specific science domains that fall within the scope of our peer review process
* Technical expertise in Python packaging.
* Awareness of the importance of documentation and package usability. 
* Awareness of the importance of CI / test suites to ensure robust software development.

## Recruiting new editors

Recruiting new editors and maintaining a sufficient and well-balanced editorial 
board is the responsibility of the software review lead (position to be 
defined) with support and advice from the editorial board. 

```{note}
pyOpenSci is a newly restructured organization. While we've been performing peer 
review for almost 4 years, we are now beginning to formalize our process thanks to
funding support from the Sloan foundation. In these early months, this software 
review lead role will be completed largely by the Executive Director with support from the Editor in 
Chief. In the future we hope to find someone with interest in leading peer review for pyOpenSci
```

## Where to find new editors

As we build our pyOpenSci community our pool of potential editors will grow.
A few options to consider include:
* Contributors who have reviewed for pyOpenSci
* Contributors who have submitted a package to pyOpenSci
* Contributors who have served as a guest editor
* Colleagues that you know who have reviewed for JOSS or rOpenSci who have Python expertise

## Starting the editorial search

To begin, start your search well in advance of when you think you may need new 
editor(s). When you begin your search, start with the existing editorial team. 
See if anyone can identify reviewers who excelled and may be a good editorial candidate. Do this in a private channels on Slack as follows:

* Start a private channel for discussion. This ensures there is not a visible
history in a public channel that a new editor may see in the future (this could
be awkward for someone to see!).
* Ping editors to be sure they get a notification as this is an important topic.
* Wait for a majority of editors to chime in before inviting someone. Provide 
editors one week to respond on slack.

## Experience required to be an editor 

We prefer that editors have some experience with reviewing software. This experience
could come from a previous review they worked on with pyOpenSci, rOpenSci or JOSS. 

If they do not have experience as may be the case in the early months or establishing 
a robust editorial board, we  offer a "mentorship" process. Editor mentorship 
is where someone with existing editorial experience, mentors the new editor 
through their first review(s).

A new editor will be considered "guest" for the first 3 months of their tenure 
and/or until they have completed their first review. Once they have a completed 
a review they can be considered to be a full editor as deemed appropriate by the 
software review lead and the current editorial board.

## Adhoc guest editors

In some cases you may require a guest editor for a single package (a one-off 
type of situation). Examples of when this might happen include:

* if there a conflict of interest between a package submitter and the editorial team (e.g. a close colleague of everyone on the team)
* if the editorial board is at capacity handling the current review load 

In this case, you may consider using our internal reviewer signup list to see
if someone who signed up to be a reviewer might want to serve as an editor. 

## Process for inviting a new editor 
 
* Editorial board candidates most often start as guest editors.
* After 3 months or their first review (which ever comes first) assess how the 
review process went. Allow other editors to provide input as well. 
* Once it is determined that the guest editor is committed to support the pyOpenSci
review process, you can email them to fully participate on the editorial board
using the template below.

```
Hi [NAME HERE]:

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

Every 3-6 months the Editor-in-Chief responsibilities rotate to a new editor. 
You'll have the opportunity to enter this rotation once you have been on the 
editorial board for atleast 6 months. 

OPTIONAL: Some editors also take on bigger projects to support pyOpenSci and 
improve the peer-review process. This is entirely optional but please let us 
know if you are interested in additional activities that support the organization. 

We hope that you'll join our growing editorial board!

Please give this some thought, ask us any questions you have, and let us know 
whether you can join us.

Best,
[your-name-here], on behalf of the pyOpenSci Editorial Board
``` 

## Onboarding a new editor

To onboard a new editor:

* Ask them to add themselves to the [pyOpenSci website](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/contributors.yml) using a pull request. If they are already listed on our website, then they only need to add 
the `title:` yaml element and update `contributor_type:` as see below:

```yaml
- name: FirstName LastName
  sort: 2
  title: "Editor" # Make sure this says Editor
  bio: ''
  organization: ""
  github_username: ghusernamehere
  github_image_id: 11934090 # You can find this value by opening your github profile image
  # in a new browser tab and grabbing the id https://avatars.githubusercontent.com/u/7649194?v=4 <- 
  # in this example 7649194 is the image_id
  contributor_type:
    - current editor # Make sure current editor is added here
    - contributor
  packages-submitted: [""]
  packages-reviewed: ["pystiche"]
  packages-editor: [""]
```


* Next work with the new editor to create a blog post introducing them which will get [posted on the pyOpenSci blog](https://www.pyopensci.org/blog).

* If they haven't already done, ask the new editor turn on [two-factor authentication (2FA) for GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa).

<!-- do we need this?
* Invite editors to the pyOpenSci GitHub organization as member, as a member of the [`editors` team](https://github.com/orgs/pyopensci/teams/editors). 
This will give them appropriate permissions and allow them to get team-specific notifications. 
* Editors need access to the AirTable database of software review.
* * In the Slack workspace they need to be added to the editors team so that `@editors` will ping them too.
 -->
* Add the new editor to the pyOpenSci Slack workspace and specifically the private editors channel.

* Post a welcome message for the new editor in the editor channel, pinging all editors.

<!-- 
This is what ROS does... i need to think this through. it doesn't make sense 
to add names in so many places manually... maybe there is a better way
* We add editors' names to 
    * [dev_guide authors list](https://github.com/ropensci/dev_guide/blob/main/index.Rmd)
    * [dev_guide chapter introducing software review](https://github.com/ropensci/dev_guide/blob/main/softwarereview_intro.Rmd) (at two locations in this file, as editors and a bit below to remove them from the reviewers list)
    * [software-review README](https://github.com/ropensci/software-review/blob/main/README.Rmd) (in two places in this file as well)
Both the dev_guide and software-review README are automatically knit via continuous integration. -->

<!-- * Add editors to https://github.com/orgs/ropensci/teams/editors/members -->

## Offboarding an editor

When it's time for an editor to step down:

* Thank them for their work!

* Remove them from the editors-only channel and the editors Slack team.

* Moved them to alumni-editor on the [pyOpenSci website](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/_data/contributors.yml) as follows:

```yaml
- name: FirstName LastName
  sort: 2
  title: "Emeritus Editor" # Modify this to say Emeritus Editor
  bio: ''
  organization: ""
  github_username: ghusernamehere
  github_image_id: 11934090 # You can find this value by opening your github profile image
  # in a new browser tab and grabbing the id https://avatars.githubusercontent.com/u/7649194?v=4 <- 
  # in this example 7649194 is the image_id
  contributor_type:
    - current editor # Make sure emeritus editor is here
    - contributor
  packages-submitted: [""]
  packages-reviewed: ["pystiche"]
  packages-editor: [""]
```
