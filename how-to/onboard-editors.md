# Onboarding and offboarding editors

pyOpenSci peer review runs on volunteer editors and reviewers. Finding new
volunteers is often the trickiest part of the process, so we've built
resources to help you. This page is for you if you're the Editor in Chief
(EiC) or the Software Review Lead. It walks you through finding, onboarding,
inviting to the board, and offboarding editors.

## How we support you

You don't have to do this alone. Here's what's in place:

* **Your editorial board.** Ask them first. They often know great candidates.
* **Our Community Manager.** They can post open calls, write blog posts, and
  introduce you to people they meet in the community.
* **Our contributor pool.** Past authors, reviewers, and guest editors are
  all people who already know us.
* **Editor mentorship.** New editors without prior experience get paired with
  a seasoned editor for their first review(s).
* **Automated website updates.** Add someone to the right GitHub team, run one
  workflow, and merge the pull request it opens. The website listing updates
  once the data are updated. See [how the website updates](#how-the-website-updates).

## About the editorial board

Our peer review process depends on a well-balanced editorial board. As you
recruit, look for combined expertise in:

* Science domains that fall within the scope of our peer review process
* Python packaging
* Documentation and package usability
* CI and test suites for robust software development

We also work to build a board with people from different backgrounds,
cultures, genders, and domains.

### Types of editors

#### New editors start as guests

A new editor is a guest editor for their first 3 months, or until they
complete their first review. After that review, you and the current
editorial board decide whether they become a full editor.

#### Ad hoc guest editors

An ad hoc editor has the specific skills needed to lead a single review.
You might need one when:

* There's a conflict of interest between a package submitter and the
  editorial team (for example, a close colleague of everyone on the team)
* The editorial board is at capacity with the current review load
* A review needs a very specialized skill set (a one-off situation)

In these cases, try our internal reviewer sign-up list. Someone who signed up
to review may be happy to serve as an editor.

### Experience and mentorship

We prefer editors who have some experience reviewing software, such as a
previous review with pyOpenSci, rOpenSci, or JOSS.

If a volunteer doesn't have that experience, that's okay. Our **mentorship
process** pairs them with an experienced editor who guides them through their
first review(s).

### Who does the recruiting

Recruiting new editors and keeping the board well-balanced is the
responsibility of the
[Software Review Lead](https://www.pyopensci.org/handbook/governance/structure.html#software-review-lead),
with support and advice from the EiC team.

## Find new editors

The Editor in Chief team and Software Review Lead work together to find and
onboard editors, especially in scientific areas where we have gaps.

### Start with your network

Good candidates to be editors can come from:

* Our existing reviewer pool
* Your professional network. You may know people in a specific domain who
  would be a great fit.
* Our
  [contributor pool](https://www.pyopensci.org/our-community/index.html#pyopensci-community-contributors),
  which includes:
  * Package authors and maintainers who have submitted a package for review
  * Reviewers who have led reviews for pyOpenSci
  * Past guest editors
* Colleagues who have reviewed for the Journal of Open Source Software (JOSS)
  or rOpenSci and have Python expertise
* Community members in the pyOpenSci Slack (post a call in
  `#software-review`)

### Ask the editorial board

Post in the `private-editorial-team` Slack channel. Ask whether any
[editors](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board)
can suggest past reviewers or other people who might be a good fit.

If the conversation turns to specific candidates:

* Start a private group message to discuss them. This keeps names out of a
  channel history that a future editor might stumble on (awkward for
  everyone!).
* Ping editors with @here so they get a notification. This is an important
  topic.

**IMPORTANT:** Give editors up to a week to chime in before you onboard a new
editor.

### Ask the Community Manager for help

If those options don't turn up a candidate, our Community Manager can help.
They can:

* Post about the opening on our
  [social media channels](https://www.pyopensci.org/handbook/community/social.html)
  with a link to our editorial board sign-up form
* Write a
  [call for editors blog post](https://www.pyopensci.org/blog/pyos-call-for-editors-may-2024.html)
  about our current needs

:::{note}
[Here's an example of a social post recruiting editors](https://fosstodon.org/@pyOpenSci/112497485980274296).
We've also run a blog post and call-outs in our monthly and weekly
newsletters.
:::

To request this support, post in the public `#software-review` Slack channel
and ping the Community Manager. Include:

* That you're looking for editors
* Any specific domains or technical skills you need, or note that it's a
  general call
* Any specific packages that need an editor (link to the submission the new
  editor would lead, if possible)

:::{tip}
Post in `#software-review` rather than sending a DM. Other editors can see
what expertise you need and that this support exists, and community members
who know potential editors can respond.
:::

The Community Manager also meets people through the broader community and
partner communities who may make great editors or reviewers. When that
happens, they'll pass the names along to you.

pyOpenSci also maintains a database of contributors, and the Community
Manager can help you find people who may be a good fit. Reach out in a private
Slack message or by email at
[media@pyopensci.org](mailto:media@pyopensci.org).

:::{note}
Before onboarding, make sure the new reviewer or editor has filled out the
right form:

* [Reviewer signup form](https://docs.google.com/forms/d/e/1FAIpQLSeVf-L_1-jYeO84OvEE8UemEoCmIiD5ddP_aO8S90vb7srADQ/viewform)
* [Editor signup form](https://docs.google.com/forms/d/17NW0P_h8gpmzf7Fr0cAd8aEbIUWPljPfg4d7Rjs1UIE/edit)
:::

(onboarding-a-new-editor)=
## Onboard a new editor

New editors usually start as guest editors. As a member of the Editor in Chief
team, you work with the Software Review Lead to get them set up. Most of it is
Slack and a warm welcome. GitHub is the only technical part.

### Slack

* If they're new to the pyOpenSci community, send them a Slack invitation (or
  ask the Community Manager to do so).
* Welcome them in Slack and give them access to `#private-editorial-team` and
  any other channels they need.
* Post a welcome message in the editor channel and ping all editors.

### Introduce them to the Community Manager

Message the Community Manager and the new editor in Slack to introduce them.
The Community Manager makes sure new members are welcomed and have what they
need in Slack. They'll also work with the new editor on an introductory blog
post, which gets published on the pyOpenSci blog, shared on social media, and
included in an upcoming newsletter.

### Security

Ask the new editor to turn on
[two-factor authentication (2FA) for GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa)
if they haven't already. It's required to join our GitHub organization.

### GitHub access

You (as the EiC or
[Software Review Lead](https://www.pyopensci.org/handbook/governance/structure.html#software-review-lead))
add editors to our GitHub organization. To do so, you'll need permission to:

* Invite members to the pyOpenSci organization
* Add or remove people on editorial teams
* Run a workflow and merge a pull request on
  [pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io)
  (only needed if you want to update the website listing before the weekly
  run)

GitHub repository access is managed using GitHub teams. Add the person to a
team and they will have access to the repositories that team needs. The
handbook's
[editorial teams](https://www.pyopensci.org/handbook/community/infrastructure/editorial-teams.html)
page has a table of every team, what it grants, and how a guest editor can
join without a team.

**Guest editors** (a new editor during their first review, or an ad hoc
editor for one review):

* Add them to the
  [`editorial-board`](https://github.com/orgs/pyOpenSci/teams/editorial-board)
  team for the duration of their editorial work. The team grants the
  repository access they need and lists them on the website while they're
  editing.
* When that work ends, remove them from the team. Don't add them to an
  emeritus team unless they later serve on the board and then step down.

**Board editors:** add them to every team that matches their role. Being on
the parent
[`peer-review-team`](https://github.com/orgs/pyOpenSci/teams/peer-review-team)
alone doesn't list them.

* [`editorial-board`](https://github.com/orgs/pyOpenSci/teams/editorial-board):
  a current editor
* [`eic-team`](https://github.com/orgs/pyOpenSci/teams/eic-team): a current
  Editor in Chief
* [`peer-review-lead`](https://github.com/orgs/pyOpenSci/teams/peer-review-lead):
  a current Software Review Lead
* [`triage-team`](https://github.com/orgs/pyOpenSci/teams/triage-team): a
  current triage volunteer

If you add someone who isn't already in the organization, GitHub also invites
them. They won't be on the team, or listed on the website, until they accept
the organization invitation.

:::{note}
If someone can't join the organization, add them to
[`data/manual-editorial-roster.yml`](https://github.com/pyOpenSci/pyopensci.github.io/blob/main/data/manual-editorial-roster.yml)
in the website repository instead of a GitHub team. That's the only editorial
file you should ever edit by hand.
:::

### How the website updates

Two workflows in the
[pyopensci.github.io](https://github.com/pyOpenSci/pyopensci.github.io)
repository read the GitHub teams and open a pull request that updates the
editorial YAML files. The website listing changes once you merge that pull
request.

* [**Update editorial board**](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-editorial-board.yml)
  runs every Wednesday. It only checks team membership, so it finishes quickly
  and opens a small pull request.
* [**Update Contribs & reviewers**](https://github.com/pyOpenSci/pyopensci.github.io/actions/workflows/update-contribs-reviews.yml)
  runs every Monday. It also refreshes the editorial files, but only after
  re-scanning every repository and review issue. That makes it slower and its
  pull request much larger.

:::{tip}
After you change a team, don't wait for the next scheduled run. Go to the
**Actions** tab in `pyopensci.github.io`, choose **Update editorial board**,
select **Run workflow**, and merge the pull request it opens. Use this one
rather than **Update Contribs & reviewers**. It's the fast one.
:::

:::{mermaid}
flowchart LR
  Membership[Update GitHub team] --> Cron[Run Update editorial board]
  Cron --> PR[Merge the pull request]
  PR --> Live[Editorial team updated on the website ✨]
:::

Don't hand-edit `editorial-board.yml`, `emeritus-editors.yml`, or editorial
flags in `contributors.yml`. The workflows update them automatically, and hand
edits can be overwritten. For the bigger picture, see
[how pyOpenSci data flows](https://www.pyopensci.org/handbook/community/infrastructure/data-process.html)
and the
[infrastructure overview](https://www.pyopensci.org/handbook/community/infrastructure/intro.html)
in the handbook.

### Check that it worked

Once the person has accepted the organization invitation and you've merged the
pull request, they should appear on the
[editorial board page](https://www.pyopensci.org/about-peer-review/index.html#meet-our-editorial-board).
If they don't, check that they accepted the invite and that they're on the
right team.

## Invite a guest editor to join the board

After 3 months or their first review (whichever comes first), you and the EiC
assess how it went. Invite other editors to weigh in too.

Once you're confident the guest editor is committed to supporting our review
process, email them an invitation to join the editorial board using the
template below.

```
Hi [NAME HERE]:

We would like to formally invite you to join the pyOpenSci editorial board as a full
member. [*SPECIFIC REASONS FOR INVITATION (mention contributions to pyOpenSci)*].
We think you will make a wonderful addition to our pyOpenSci open review team!

[Here is an onboarding document to help you navigate your first weeks in this role.](https://docs.google.com/document/d/1UfG1Fe5wSiEAObvqNMT4etZ5sx7QXzW0f8mozKyK1NE/edit?tab=t.0)

[IF GUEST EDITOR: You are familiar with the editor's role, as you've been a guest editor]. We aim for editors to handle reviews for four packages per year
([IF GUEST EDITOR including the one that you just finished!]).
We ask that editors make an informal commitment to serve for two years and
re-evaluate their participation after that.
On a short-term basis, any editor can decline to handle a package or say,
"I'm pretty busy, I can't handle a new package for a few weeks."

In addition to handling packages, editors weigh in on group editorial decisions,
such as whether a package is in scope, and support updates to our policies.
We generally do this through Slack, which we expect editors to be able to check
regularly. We have editorial board calls annually.

Every 3-6 months, the Editor-in-Chief's responsibilities rotate to a new editor.
You'll have the opportunity to enter this rotation once you have been on the
editorial board for at least 6 months.

OPTIONAL: Some editors also take on bigger projects to support pyOpenSci and
improve the peer-review process. This is entirely optional, but please let us
know if you are interested in additional activities that support the organization.

We hope that you'll join our growing editorial board!

Please give this some thought, ask us any questions you have, and let us know
whether you can join us.

Best,
[your-name-here], on behalf of the pyOpenSci Editorial Board
```

### When they say yes

A guest editor is already on the `editorial-board` team, so promoting them
doesn't require a team change. If they take on a specialty role (Editor in
Chief, Software Review Lead, or triage), add them to the matching team from
[GitHub access](#github-access), then update the website using
[how the website updates](#how-the-website-updates). Announce the good news in
`#private-editorial-team`.

## Offboard an editor

When an editor steps down, thank them for their work first. Then update
Slack, GitHub, and the website.

**Guest editors** who have finished their review:

* Remove them from
  [`editorial-board`](https://github.com/orgs/pyOpenSci/teams/editorial-board).
* Don't add them to an emeritus team. That's only for people who served on
  the board.

**Board editors:**

* Announce that they're stepping down, and thank them, in the `#software-review`
  Slack channel. Then remove them from the `#private-editorial-team` channel.
* Remove them from every active editorial team: `editorial-board`, plus
  `eic-team`, `peer-review-lead`, or `triage-team` if they were on those.
* Add them to
  [`emeritus-editors`](https://github.com/orgs/pyOpenSci/teams/emeritus-editors).
  If they held a specialty role, also add them to the matching emeritus team:
  * [`emeritus-editor-in-chief`](https://github.com/orgs/pyOpenSci/teams/emeritus-editor-in-chief)
  * [`emeritus-peer-review-lead`](https://github.com/orgs/pyOpenSci/teams/emeritus-peer-review-lead)
  * [`emeritus-triage-team`](https://github.com/orgs/pyOpenSci/teams/emeritus-triage-team)

Then update the website the same way as when you add someone. Follow
[how the website updates](#how-the-website-updates): run **Update editorial
board** and merge the pull request.
